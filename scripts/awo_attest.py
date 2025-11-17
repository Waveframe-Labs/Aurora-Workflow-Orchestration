#!/usr/bin/env python3
"""
AWO v3.0 attestation helper.

Usage (from repo root):

    python scripts/awo_attest.py --run-id RUN_ID

Responsibilities:
  - Generate SHA256SUMS.txt with exact coverage for runs/<RUN_ID>/ (excluding SHA256SUMS.txt itself).
  - Enforce:
      * scope/ included when scope_validate op is present in index.json.
      * GNU coreutils format: "<sha256>  ./relative/path".
      * Every file under run dir (except sums itself) is listed; no extras.
      * sqrt(n) re-hash sample, deterministic via RUN_ID.
  - Write governance/attestations/<RUN_ID>/ATTESTATION.txt and ATTESTATION.json
    (the workflow is responsible for calling cosign sign-blob on these).
"""

import argparse
import hashlib
import json
import math
import os
import random
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Tuple, Dict, Any

REPO_ROOT = Path(os.getenv("GITHUB_WORKSPACE", Path.cwd())).resolve()


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _relfmt(run_dir: Path, p: Path) -> str:
    rp = p.resolve().relative_to(run_dir.resolve())
    return "./" + str(rp).replace("\\", "/")


def _walk_files(run_dir: Path, exclude: List[Path]) -> List[Path]:
    excl_abs = {e.resolve() for e in exclude}
    out: List[Path] = []
    for root, _, files in os.walk(run_dir):
        for fn in files:
            fp = Path(root) / fn
            if fp.resolve() in excl_abs:
                continue
            out.append(fp)
    return sorted(out)


def generate_sums(run_id: str) -> Tuple[Path, List[Tuple[str, Path]]]:
    rd = REPO_ROOT / "runs" / run_id
    if not rd.is_dir():
        raise SystemExit(f"run dir not found: {rd}")

    sums_path = rd / "SHA256SUMS.txt"
    files = _walk_files(rd, exclude=[sums_path])
    entries: List[Tuple[str, Path]] = []

    lines: List[str] = []
    for fp in files:
        h = hashlib.sha256()
        with fp.open("rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        digest = h.hexdigest()
        entries.append((digest, fp))
        lines.append(f"{digest}  {_relfmt(rd, fp)}\n")

    sums_path.write_text("".join(lines), encoding="utf-8")
    return sums_path, entries


def verify_exact_coverage(run_id: str, sums_path: Path, entries: List[Tuple[str, Path]]) -> None:
    rd = REPO_ROOT / "runs" / run_id

    # Parse SHA256SUMS
    line_re = re.compile(r"^([a-f0-9]{64})  (\./.+)$")
    parsed: List[Tuple[str, str]] = []
    with sums_path.open("r", encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.rstrip("\n")
            m = line_re.match(line)
            if not m:
                raise SystemExit(f"bad_line_format:{ln}:{line}")
            h, rel = m.group(1), m.group(2)
            if "\\" in rel or ".." in rel:
                raise SystemExit(f"unsafe_path_line:{ln}:{rel}")
            parsed.append((h, rel))

    paths_in_sums = {rel for _, rel in parsed}

    # scope inclusion rule
    has_scope = False
    idx_path = rd / "index.json"
    if idx_path.is_file():
        try:
            idx = json.loads(idx_path.read_text(encoding="utf-8"))
            has_scope = any(
                isinstance(s, dict) and s.get("op") == "scope_validate"
                for s in idx.get("steps", [])
            )
        except Exception:
            has_scope = False
    if has_scope and not (rd / "scope").is_dir():
        raise SystemExit("scope_missing_but_required")

    # Enumerate ALL files except SHA256SUMS.txt
    all_files = set()
    for root, _, files in os.walk(rd):
        for fn in files:
            fp = Path(root) / fn
            if fp.resolve() == sums_path.resolve():
                continue
            all_files.add(_relfmt(rd, fp))

    missing = sorted(all_files - paths_in_sums)
    extra = sorted(paths_in_sums - all_files)
    if missing:
        raise SystemExit("missing_in_sums:" + ",".join(missing))
    if extra:
        raise SystemExit("extra_in_sums:" + ",".join(extra))

    # Deterministic √n rehash sample
    n = len(entries)
    if n == 0:
        return

    k = min(n, min(max(3, int(math.isqrt(n))), 20))
    seed = int(hashlib.sha256(run_id.encode("utf-8")).hexdigest(), 16) & ((1 << 63) - 1)
    rnd = random.Random(seed)
    indices = sorted(rnd.sample(range(n), k))

    for i in indices:
        expected, path = entries[i]
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        got = h.hexdigest()
        if got != expected:
            rel = _relfmt(rd, path)
            raise SystemExit(f"rehash_mismatch:{rel}")


def write_attestation(run_id: str, manifest_sha: str, sums_sha: str) -> Tuple[Path, Path]:
    rd = REPO_ROOT / "runs" / run_id
    gov_dir = REPO_ROOT / "governance" / "attestations" / run_id
    gov_dir.mkdir(parents=True, exist_ok=True)

    repo = os.getenv("GITHUB_REPOSITORY", "")
    run_url = ""
    if repo and os.getenv("GITHUB_RUN_ID"):
        run_url = f"https://github.com/{repo}/actions/runs/{os.getenv('GITHUB_RUN_ID')}"

    try:
        git_sha = (
            (REPO_ROOT / ".git" / "HEAD").read_text().strip()
            if (REPO_ROOT / ".git" / "HEAD").exists()
            else ""
        )
    except Exception:
        git_sha = ""

    now = _ts()
    actor = os.getenv("GITHUB_ACTOR", "")

    txt_path = gov_dir / "ATTESTATION.txt"
    txt = f"""AWO Run Attestation

Run-ID: {run_id}
Repository: {repo}
Commit: {git_sha}
Workflow Run: {run_url}
Actor: {actor}
Timestamp (UTC): {now}

Bindings:
    run_manifest.json  sha256:{manifest_sha}
    SHA256SUMS.txt     sha256:{sums_sha}

Statement:
    This attestation binds the AWO run manifest to the file
    inventory recorded in SHA256SUMS.txt. Any alteration of
    either file will invalidate these hashes.
"""
    txt_path.write_text(txt, encoding="utf-8")

    json_path = gov_dir / "ATTESTATION.json"
    data: Dict[str, Any] = {
        "run_id": run_id,
        "repository": repo,
        "commit": git_sha,
        "workflow_run_url": run_url,
        "actor": actor,
        "timestamp_utc": now,
        "bindings": {
            "run_manifest.json": f"sha256:{manifest_sha}",
            "SHA256SUMS.txt": f"sha256:{sums_sha}",
        },
    }
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return txt_path, json_path


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="AWO v3.0 attestation helper")
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args(argv)

    run_id = args.run_id
    rd = REPO_ROOT / "runs" / run_id
    if not rd.is_dir():
        print(f"[awo_attest] run dir not found: {rd}", file=sys.stderr)
        return 1

    mf = rd / "run_manifest.json"
    if not mf.is_file():
        print(f"[awo_attest] run_manifest.json missing: {mf}", file=sys.stderr)
        return 1

    # 1) Generate sums and enforce coverage
    sums_path, entries = generate_sums(run_id)
    verify_exact_coverage(run_id, sums_path, entries)

    # 2) Compute manifest + sums digests for attestation
    def sha256_file(p: Path) -> str:
        h = hashlib.sha256()
        with p.open("rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()

    manifest_sha = sha256_file(mf)
    sums_sha = sha256_file(sums_path)

    # 3) Write attestation artifacts
    txt_path, json_path = write_attestation(run_id, manifest_sha, sums_sha)

    print("[awo_attest] OK")
    print("  run_dir      :", rd)
    print("  sums         :", sums_path)
    print("  manifest_sha :", manifest_sha)
    print("  sums_sha     :", sums_sha)
    print("  attestation  :", txt_path)
    print("  attestationJ :", json_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

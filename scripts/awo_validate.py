#!/usr/bin/env python3
"""
AWO v3.0 validator.

Usage (from repo root):

    python scripts/awo_validate.py invariants --run-id RUN_ID
    python scripts/awo_validate.py gate2 --run-id RUN_ID --orchestrator ORCH --reviewer REVIEWER --allow-self-approval {0,1}

Writes:
  runs/<RUN_ID>/audit/invariants.json
  governance/logs/<RUN_ID>_independence_<TS>.json
  runs/<RUN_ID>/audit/<RUN_ID>_gate2_verdict.json
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Any

REPO_ROOT = Path(os.getenv("GITHUB_WORKSPACE", Path.cwd())).resolve()


def _ts_for_filename() -> str:
    # Windows-safe (no ':')
    return datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%SZ")


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_invariants(run_id: str) -> int:
    rd = REPO_ROOT / "runs" / run_id
    audit_dir = rd / "audit"
    audit_dir.mkdir(parents=True, exist_ok=True)

    reasons: List[str] = []
    ok = True

    if not rd.is_dir():
        reasons.append(f"run_dir_missing:{rd}")
        ok = False
    else:
        # Required files / dirs
        req_files = ["report.md", "run_manifest.json", "provenance.json", "index.json", "environment.json"]
        req_dirs = ["steps", "artifacts"]

        for name in req_files:
            if not (rd / name).is_file():
                reasons.append(f"missing_file:{name}")
                ok = False

        for name in req_dirs:
            if not (rd / name).is_dir():
                reasons.append(f"missing_dir:{name}")
                ok = False

        # steps/: non-empty, *.json, canonical NN_id.json, mapping to index.json
        steps_dir = rd / "steps"
        if steps_dir.is_dir():
            step_files = sorted(p for p in steps_dir.iterdir() if p.is_file())
            if not step_files:
                reasons.append("steps_empty")
                ok = False

            non_json = [p.name for p in step_files if p.suffix != ".json"]
            if non_json:
                reasons.append("steps_non_json:" + ",".join(non_json))
                ok = False

            bad_names = [
                p.name for p in step_files
                if not re.match(r"^[0-9]{2}_.+\.json$", p.name)
            ]
            if bad_names:
                reasons.append("bad_step_filenames:" + ",".join(bad_names))
                ok = False

            # index.json contract
            idx_path = rd / "index.json"
            if idx_path.is_file():
                try:
                    idx = _load_json(idx_path)
                except Exception as e:
                    reasons.append(f"index_json_error:{e}")
                    ok = False
                else:
                    steps = idx.get("steps")
                    if not isinstance(steps, list) or not steps:
                        reasons.append("index.steps_empty_or_missing")
                        ok = False
                    else:
                        id_pat = re.compile(r"^[A-Za-z0-9._-]{1,80}$")
                        seen_indices = set()
                        expected_files = set()
                        for i, s in enumerate(steps):
                            if not isinstance(s, dict):
                                reasons.append(f"index.steps[{i}]_not_object")
                                ok = False
                                continue
                            for k in ("op", "id", "index"):
                                if k not in s:
                                    reasons.append(f"index.steps[{i}].missing:{k}")
                                    ok = False
                            op = s.get("op")
                            sid = s.get("id")
                            idx_val = s.get("index")
                            if not isinstance(op, str) or not op:
                                reasons.append(f"index.steps[{i}].op_invalid")
                                ok = False
                            if not isinstance(sid, str) or not sid:
                                reasons.append(f"index.steps[{i}].id_invalid")
                                ok = False
                            if not isinstance(idx_val, int):
                                reasons.append(f"index.steps[{i}].index_not_int")
                                ok = False
                            if isinstance(sid, str) and not id_pat.match(sid):
                                reasons.append(f"index.steps[{i}].id_bad_chars:{sid}")
                                ok = False
                            if isinstance(idx_val, int):
                                if idx_val in seen_indices:
                                    reasons.append(f"index.duplicate_index:{idx_val}")
                                    ok = False
                                seen_indices.add(idx_val)
                                expected_files.add(f"{idx_val:02d}_{sid}.json")

                        actual_files = {p.name for p in step_files if p.suffix == ".json"}
                        missing = sorted(expected_files - actual_files)
                        extra = sorted(actual_files - expected_files)
                        if missing:
                            reasons.append("steps.missing_files:" + ",".join(missing))
                            ok = False
                        if extra:
                            reasons.append("steps.unexpected_files:" + ",".join(extra))
                            ok = False
            else:
                reasons.append("index.json_missing")
                ok = False

        # scope/ required if index.json mentions op == "scope_validate"
        idx_path = rd / "index.json"
        if idx_path.is_file():
            try:
                idx = _load_json(idx_path)
                has_scope = any(
                    isinstance(s, dict) and s.get("op") == "scope_validate"
                    for s in idx.get("steps", [])
                )
            except Exception:
                has_scope = False
            if has_scope and not (rd / "scope").is_dir():
                reasons.append("missing_dir:scope")
                ok = False

        # report.md must start with "# AWO Run Report — <RUN_ID>"
        rpt_path = rd / "report.md"
        if rpt_path.is_file():
            if rpt_path.stat().st_size <= 0:
                reasons.append("report_empty")
                ok = False
            else:
                with rpt_path.open("r", encoding="utf-8") as f:
                    first = f.readline().rstrip("\r\n")
                expected = f"# AWO Run Report — {run_id}"
                if first != expected:
                    reasons.append(f"report_heading_mismatch:{first!r}!={expected!r}")
                    ok = False

        # environment.json and provenance.json structural checks
        env_path = rd / "environment.json"
        prov_path = rd / "provenance.json"
        ts_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$")
        sha256_re = re.compile(r"^[a-f0-9]{64}$")

        if env_path.is_file():
            try:
                env = _load_json(env_path)
                for k in ("os", "python", "platform", "git", "runner", "tools"):
                    if k not in env:
                        reasons.append(f"environment.missing:{k}")
                        ok = False
                if not str(env.get("os", "")).strip():
                    reasons.append("environment.os_empty"); ok = False
                if not str(env.get("python", "")).strip():
                    reasons.append("environment.python_empty"); ok = False
                if not str(env.get("platform", "")).strip():
                    reasons.append("environment.platform_empty"); ok = False

                git = env.get("git", {})
                if not isinstance(git, dict):
                    reasons.append("environment.git_not_object"); ok = False
                else:
                    if not str(git.get("commit", "")).strip():
                        reasons.append("environment.git.commit_empty"); ok = False
                    if str(git.get("commit", "")).strip().lower() == "unknown":
                        reasons.append("environment.git.commit_unknown"); ok = False
                    if not str(git.get("branch", "")).strip():
                        reasons.append("environment.git.branch_empty"); ok = False

                runner = env.get("runner", {})
                if not isinstance(runner, dict):
                    reasons.append("environment.runner_not_object"); ok = False
                else:
                    if not str(runner.get("name", "")).strip():
                        reasons.append("environment.runner.name_empty"); ok = False
                    if not str(runner.get("version", "")).strip():
                        reasons.append("environment.runner.version_empty"); ok = False

                tools = env.get("tools", [])
                if not isinstance(tools, list) or not tools:
                    reasons.append("environment.tools_empty"); ok = False
                else:
                    for i, t in enumerate(tools):
                        if not isinstance(t, dict):
                            reasons.append(f"environment.tools[{i}]_not_object"); ok = False; continue
                        if not str(t.get("name", "")).strip():
                            reasons.append(f"environment.tools[{i}].name_empty"); ok = False
                        if not str(t.get("version", "")).strip():
                            reasons.append(f"environment.tools[{i}].version_empty"); ok = False
            except Exception as e:
                reasons.append(f"environment.json_error:{e}")
                ok = False
        else:
            reasons.append("environment.json_missing"); ok = False

        if prov_path.is_file():
            try:
                prov = _load_json(prov_path)
                for k in ("inputs_digest", "code_digest", "runtime", "started", "finished"):
                    if k not in prov:
                        reasons.append(f"provenance.missing:{k}")
                        ok = False

                idg = prov.get("inputs_digest", {})
                if not isinstance(idg, dict) or not idg:
                    reasons.append("provenance.inputs_digest_empty"); ok = False
                else:
                    for k, v in idg.items():
                        if not isinstance(v, str) or not sha256_re.match(v):
                            reasons.append(f"provenance.inputs_digest[{k}]_not_sha256"); ok = False

                cd = prov.get("code_digest", "")
                if not isinstance(cd, str) or not cd.strip():
                    reasons.append("provenance.code_digest_empty"); ok = False
                elif not sha256_re.match(cd.strip()):
                    reasons.append("provenance.code_digest_not_sha256"); ok = False

                rt = prov.get("runtime", {})
                if not isinstance(rt, dict) or not rt:
                    reasons.append("provenance.runtime_empty"); ok = False

                st = prov.get("started", "")
                fn = prov.get("finished", "")
                for key, val in (("started", st), ("finished", fn)):
                    if not isinstance(val, str) or not ts_re.match(val):
                        reasons.append(f"provenance.{key}_bad_ts:{val}")
                        ok = False
                try:
                    if ts_re.match(st) and ts_re.match(fn):
                        t0 = datetime.fromisoformat(st.replace("Z", "+00:00"))
                        t1 = datetime.fromisoformat(fn.replace("Z", "+00:00"))
                        if t1 < t0:
                            reasons.append("provenance.non_monotonic_time")
                            ok = False
                except Exception as e:
                    reasons.append(f"provenance.time_parse_error:{e}")
                    ok = False
            except Exception as e:
                reasons.append(f"provenance.json_error:{e}")
                ok = False
        else:
            reasons.append("provenance.json_missing"); ok = False

        # Volatility / timestamp normalization scan
        key_files = [
            rd / "run_manifest.json",
            rd / "provenance.json",
            rd / "environment.json",
            rd / "index.json",
        ]
        if steps_dir.is_dir():
            key_files.extend(sorted(p for p in steps_dir.glob("*.json")))

        vol_keys = {"pid", "hostname", "container_id", "pod_uid", "instance_id"}

        def scan(obj: Any, path: str = "") -> List[str]:
            out: List[str] = []
            if isinstance(obj, dict):
                for k, v in obj.items():
                    p = f"{path}.{k}" if path else k
                    if k in vol_keys and v not in (None, ""):
                        out.append(f"volatile:{p}")
                    if isinstance(v, str) and k.lower().endswith(("time", "timestamp", "at", "started", "finished")):
                        if not ts_re.match(v):
                            out.append(f"bad_ts:{p}={v}")
                    out.extend(scan(v, p))
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    out.extend(scan(v, f"{path}[{i}]"))
            return out

        for fp in key_files:
            if not fp.is_file():
                continue
            try:
                doc = _load_json(fp)
                problems = scan(doc)
                for p in problems:
                    reasons.append(f"{fp.relative_to(rd)}:{p}")
                    ok = False
            except Exception as e:
                reasons.append(f"{fp.relative_to(rd)}:json_error:{e}")
                ok = False

    invariants = {
        "run_id": run_id,
        "invariants_ok": ok,
        "reasons": reasons,
        "validated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    (rd / "audit").mkdir(parents=True, exist_ok=True)
    out_path = rd / "audit" / "invariants.json"
    out_path.write_text(json.dumps(invariants, indent=2), encoding="utf-8")

    # Always exit 0 so artifacts are preserved; gate2 decides whether to halt.
    print(json.dumps(invariants, indent=2))
    return 0


def gate2_decision(run_id: str, orchestrator: str, reviewer: str, allow_self: bool) -> int:
    rd = REPO_ROOT / "runs" / run_id
    audit_dir = rd / "audit"
    audit_dir.mkdir(parents=True, exist_ok=True)
    gov_dir = REPO_ROOT / "governance" / "logs"
    gov_dir.mkdir(parents=True, exist_ok=True)

    inv_path = rd / "audit" / "invariants.json"
    invariants_ok = False
    inv_reasons: List[str] = []
    if inv_path.is_file():
        try:
            data = _load_json(inv_path)
            invariants_ok = bool(data.get("invariants_ok"))
            inv_reasons = list(data.get("reasons", []))
        except Exception as e:
            invariants_ok = False
            inv_reasons = [f"invariants_read_error:{e}"]
    else:
        inv_reasons = ["invariants_missing"]
        invariants_ok = False

    status = ""
    message = ""

    if not invariants_ok:
        status = "FAILED_INVARIANTS"
        message = "AWO invariant validation failed."
    else:
        if reviewer == orchestrator:
            if allow_self:
                status = "SELF_APPROVED_WITH_OVERRIDE"
                message = "Run approved by orchestrator (override active)."
            else:
                status = "FAILED_SELF_APPROVAL"
                message = "Run halted: orchestrator and reviewer are the same identity."
        else:
            status = "APPROVED_BY_INDEPENDENT_REVIEWER"
            message = "Reviewer is distinct from orchestrator."

    ts = _ts_for_filename()
    verdict = {
        "run_id": run_id,
        "orchestrator": orchestrator,
        "reviewer": reviewer,
        "allow_self_approval": allow_self,
        "status": status,
        "message": message,
        "invariants_ok": invariants_ok,
        "invariants_reasons": inv_reasons,
        "timestamp": ts,
    }

    # Governance log
    gov_path = gov_dir / f"{run_id}_independence_{ts}.json"
    gov_path.write_text(json.dumps(verdict, indent=2), encoding="utf-8")

    # Copy into run audit for local inspection
    audit_verdict = audit_dir / f"{run_id}_gate2_verdict.json"
    audit_verdict.write_text(json.dumps(verdict, indent=2), encoding="utf-8")

    print(json.dumps(verdict, indent=2))

    if status in ("FAILED_INVARIANTS", "FAILED_SELF_APPROVAL"):
        return 1
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="AWO v3.0 validator")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_inv = sub.add_parser("invariants", help="Validate run invariants")
    p_inv.add_argument("--run-id", required=True)

    p_gate = sub.add_parser("gate2", help="Gate2 decision (independence + invariants)")
    p_gate.add_argument("--run-id", required=True)
    p_gate.add_argument("--orchestrator", required=True)
    p_gate.add_argument("--reviewer", required=True)
    p_gate.add_argument("--allow-self-approval", choices=["0", "1"], required=True)

    args = parser.parse_args(argv)

    if args.cmd == "invariants":
        return validate_invariants(args.run_id)
    if args.cmd == "gate2":
        allow_self = args.allow_self_approval == "1"
        return gate2_decision(args.run_id, args.orchestrator, args.reviewer, allow_self)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

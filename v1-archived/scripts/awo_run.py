#!/usr/bin/env python3
"""
AWO multi-model runner (CI/Actions safe).

North Star (echo):
  1) AWO = methodology for transparent, auditable AI–human work.
  2) CRI = tooling that enforces AWO (CI/CD for research).
  3) Falsifiability first, reproducibility by default, human-in-the-loop gates.
  4) Air-gapped by default; adapters optional; user supplies their own API keys.
  5) Positioning: “Git for falsifiable science.” Evolutionary, not messianic.

This runner:
- Emits schema-compliant run_manifest.json (start/update/finalize)
- Emits schema-compliant provenance.json (per step + artifacts)
- Validates with jsonschema (fail-fast)
- Uses deterministic local backends (echo/upper/reverse) by default
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from enum import IntEnum
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

# ---------- required for schema validation (install in CI: pip install jsonschema)
try:
    import jsonschema
except Exception:
    print("[AWO] FATAL: jsonschema not installed. Add `pip install jsonschema` in CI.", file=sys.stderr)
    raise


class ExitCode(IntEnum):
    OK = 0
    ERROR = 2
    PENDING = 78  # widely used by CI to mean "manual review needed"


# ---------------------------- repo-rooted paths ------------------------------
REPO_ROOT = Path(os.getenv("GITHUB_WORKSPACE", Path.cwd())).resolve()
RUNS_ROOT = (REPO_ROOT / "runs").resolve()
SCHEMAS_ROOT = (REPO_ROOT / "schemas").resolve()

RUN_MANIFEST_PATH = "run_manifest.json"
PROVENANCE_PATH = "provenance.json"


def _debug(msg: str) -> None:
    print(f"[AWO] {msg}", file=sys.stdout, flush=True)


# --------------------------------- time --------------------------------------
def ts_rfc3339() -> str:
    """RFC3339/ISO 8601 (valid for jsonschema date-time)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ts_for_dirname() -> str:
    """Filesystem-safe timestamp for run directory name."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")


# --------------------------- deterministic local backends --------------------
class _Echo:
    def generate(self, prompt: str, params=None):
        return {"text": prompt, "meta": {"engine": "fallback:echo", "seed": (params or {}).get("seed", 0)}}


class _Upper:
    def generate(self, prompt: str, params=None):
        return {"text": (prompt or "").upper(), "meta": {"engine": "fallback:upper", "seed": (params or {}).get("seed", 0)}}


class _Reverse:
    def generate(self, prompt: str, params=None):
        return {"text": (prompt or "")[::-1], "meta": {"engine": "fallback:reverse", "seed": (params or {}).get("seed", 0)}}


# --------------------------------- utils -------------------------------------
def sha256_hex_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_hex_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def ensure_run_dir() -> Path:
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    rd = RUNS_ROOT / f"run_{ts_for_dirname()}"
    (rd / "steps").mkdir(parents=True, exist_ok=True)
    (rd / "artifacts").mkdir(parents=True, exist_ok=True)
    if not rd.exists():
        raise RuntimeError(f"Failed to create run dir: {rd}")
    return rd


def breadcrumb(run_dir: Path) -> None:
    """Write runs/LAST_RUN with verification."""
    last_run = RUNS_ROOT / "LAST_RUN"
    write_text(last_run, run_dir.name)
    for _ in range(3):
        try:
            if last_run.read_text(encoding="utf-8").strip() == run_dir.name:
                return
        except Exception:
            pass
        time.sleep(0.05)
    raise RuntimeError(f"Breadcrumb verification failed: {last_run} != {run_dir.name}")


def init_report(run_dir: Path, workflow_path: str) -> List[str]:
    return [
        f"# AWO Run Report — {run_dir.name}",
        "",
        f"- Repo root: {REPO_ROOT}",
        f"- Runs root: {RUNS_ROOT}",
        f"- Workflow: {workflow_path}",
        f"- Started: {ts_rfc3339()}",
        "",
    ]


def record_step(run_dir: Path, idx: int, step_id: str, payload: Dict[str, Any]) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{step_id}.json", payload)


def finalize_report(run_dir: Path, report_lines: List[str]) -> None:
    write_text(run_dir / "report.md", "\n".join(report_lines))


def rel(p: Path) -> str:
    """Relative path from repo root (fallback to absolute string)."""
    try:
        return str(p.resolve().relative_to(REPO_ROOT))
    except Exception:
        return str(p)


def _git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT).decode().strip()
    except Exception:
        return "unknown"


# ------------------------------ schema helpers -------------------------------
def _load_schema(name: str) -> Dict[str, Any]:
    p = (SCHEMAS_ROOT / name).resolve()
    if not p.exists():
        raise FileNotFoundError(f"Schema not found: {p}")
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Invalid JSON in schema {p}: {e}")


RUN_MANIFEST_SCHEMA: Dict[str, Any] | None = None
PROVENANCE_SCHEMA: Dict[str, Any] | None = None


def _ensure_schemas_loaded() -> None:
    global RUN_MANIFEST_SCHEMA, PROVENANCE_SCHEMA
    if RUN_MANIFEST_SCHEMA is None:
        RUN_MANIFEST_SCHEMA = _load_schema("run_manifest.schema.json")
    if PROVENANCE_SCHEMA is None:
        PROVENANCE_SCHEMA = _load_schema("provenance.schema.json")


def _validate_or_die(obj: Dict[str, Any], schema: Dict[str, Any], label: str) -> None:
    try:
        jsonschema.validate(obj, schema)
    except jsonschema.ValidationError as e:
        raise RuntimeError(f"{label} failed schema validation: {e.message}")


# --------------------------- scope validation helpers ------------------------
REQUIRED_CLAIM_FIELDS = ["id", "statement"]


def _problems_for_claim(claim: Dict[str, Any]) -> List[str]:
    probs: List[str] = []
    for f in REQUIRED_CLAIM_FIELDS:
        if f not in claim or claim[f] in (None, "", []):
            probs.append(f"missing field: {f}")
    preds = claim.get("predictions", [])
    tests = claim.get("falsification_tests", [])
    if not preds and not tests:
        probs.append("claim is not testable: no predictions and no falsification_tests")
    for i, p in enumerate(preds or []):
        tol = (p or {}).get("tolerance")
        if not tol:
            probs.append(f"prediction[{i}] missing tolerance")
    for i, t in enumerate(tests or []):
        if not isinstance(t, dict) or not any(k in t for k in ("must_pass", "fail_if")):
            probs.append(f"falsification_tests[{i}] missing must_pass/fail_if")
    return probs


def _load_claims(args: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[str]]:
    loaded: List[Dict[str, Any]] = []
    notes: List[str] = []
    if "claim" in args and isinstance(args["claim"], dict):
        loaded.append(args["claim"])
    glob = args.get("claims_glob")
    if glob:
        for p in REPO_ROOT.glob(glob):
            try:
                loaded.append(json.loads(Path(p).read_text(encoding="utf-8")))
            except Exception as e:
                notes.append(f"failed to parse {p}: {e}")
    return loaded, notes


# --------------------------- manifest/provenance ------------------------------
def _init_run_manifest(run_dir: Path, workflow_path: str, started_at: str) -> Dict[str, Any]:
    """
    IMPORTANT: matches run_manifest.schema.json
      - notes: array of strings
      - env_ref: string pointing to environment snapshot
      - started_at/finished_at: RFC3339 strings
    """
    # Create environment snapshot
    env = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "git_sha": _git_sha(),
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "github_sha": os.getenv("GITHUB_SHA"),
    }
    env_path = run_dir / "environment.json"
    write_json(env_path, env)

    m = {
        "run_id": run_dir.name,
        "workflow": workflow_path,
        "started_at": started_at,
        "finished_at": None,          # set on success/error only
        "status": "running",
        "ops": [],
        "notes": ["env:environment.json"],
        "env_ref": "environment.json",
    }
    _ensure_schemas_loaded()
    _validate_or_die(m, RUN_MANIFEST_SCHEMA, "run_manifest")
    write_json(run_dir / RUN_MANIFEST_PATH, m)
    return m


def _append_manifest_op(run_dir: Path, manifest: Dict[str, Any], idx: int, step_id: str, op: str) -> None:
    manifest["ops"].append({"idx": idx, "id": step_id, "op": op})
    _validate_or_die(manifest, RUN_MANIFEST_SCHEMA, "run_manifest")
    write_json(run_dir / RUN_MANIFEST_PATH, manifest)


def _finalize_manifest(run_dir: Path, manifest: Dict[str, Any], status: str) -> None:
    manifest["status"] = status
    manifest["finished_at"] = ts_rfc3339()
    _validate_or_die(manifest, RUN_MANIFEST_SCHEMA, "run_manifest")
    write_json(run_dir / RUN_MANIFEST_PATH, manifest)


def _init_provenance(run_dir: Path) -> List[Dict[str, Any]]:
    return []


def _write_provenance(run_dir: Path, prov: List[Dict[str, Any]]) -> None:
    _ensure_schemas_loaded()
    for rec in prov:
        _validate_or_die(rec, PROVENANCE_SCHEMA, "provenance")
    write_json(run_dir / PROVENANCE_PATH, prov)


def _prov_record_template(
    run_id: str,
    role: str,
    model_name: str,
    *,
    provider: str | None = None,
    version: str | None = None,
    prompt_id: str | None = None,
    params: Dict[str, Any] | None = None,
    artifacts: List[str] | None = None,
    hashes: Dict[str, str] | None = None,
    started: str | None = None,
    ended: str | None = None,
    notes: str | None = None,
) -> Dict[str, Any]:
    rec: Dict[str, Any] = {
        "run_id": run_id,
        "role": role,
        "model": {
            "name": model_name,
            **({"provider": provider} if provider else {}),
            **({"version": version} if version else {}),
        },
        **({"prompt_id": prompt_id} if prompt_id else {}),
        **({"seed": (params or {}).get("seed")} if (params or {}).get("seed") is not None else {}),
        "tools": {},
        "artifacts": artifacts or [],
        "hashes": hashes or {},
        "started": started or ts_rfc3339(),
        "ended": ended or ts_rfc3339(),
        **({"notes": notes} if notes is not None else {}),
    }
    return rec


# ------------------------------ fatal error path -----------------------------
def _fatal(
    *,
    run_dir: Path,
    manifest: Dict[str, Any],
    report: List[str],
    step_idx: int,
    step_id: str,
    msg: str,
    started_at: str,
    extra_payload: Dict[str, Any] | None = None,
    exit_code: ExitCode = ExitCode.ERROR,
) -> int:
    """Single, consistent fatal path (records step, report, manifest, index)."""
    _append_manifest_op(run_dir, manifest, step_idx, step_id, "fatal_error")
    payload = {"error": "fatal", "message": msg, "ts": ts_rfc3339()}
    if extra_payload:
        payload.update(extra_payload)
    record_step(run_dir, step_idx, step_id, payload)
    report += ["## Error", "", msg, ""]
    finalize_report(run_dir, report)
    _finalize_manifest(run_dir, manifest, "error")
    # Index file mirrors the manifest lifecycle
    idx = {"run_id": run_dir.name, "started_at": started_at, "status": "error", "finished_at": ts_rfc3339()}
    write_json(run_dir / "index.json", idx)
    print(f"[AWO] {msg}", file=sys.stderr)
    return int(exit_code)


# --------------------------------- main --------------------------------------
def update_index(run_dir: Path, *, started_at: str, status: str, finished_at: str | None = None) -> None:
    idx = {"run_id": run_dir.name, "started_at": started_at, "status": status}
    if finished_at:
        idx["finished_at"] = finished_at
    write_json(run_dir / "index.json", idx)


def run(workflow_path: str) -> int:
    # 1) Create run dir + breadcrumb FIRST so CI can always find it.
    run_dir = ensure_run_dir()
    breadcrumb(run_dir)
    started_at = ts_rfc3339()

    # Initialize manifest + provenance
    manifest = _init_run_manifest(run_dir, workflow_path, started_at)
    provenance: List[Dict[str, Any]] = _init_provenance(run_dir)

    _debug(f"Repo root: {REPO_ROOT}")
    _debug(f"Runs root: {RUNS_ROOT}")
    _debug(f"Run dir : {run_dir}")
    _debug(f"Breadcrumb: {(RUNS_ROOT / 'LAST_RUN')}")

    report = init_report(run_dir, workflow_path)
    ctx: Dict[str, Any] = {}

    # 2) Optional local overrides; keep fallbacks if imports fail.
    BACKENDS = {"echo": _Echo(), "upper": _Upper(), "reverse": _Reverse()}
    try:
        from awo.models.local_backend import LocalEcho  # type: ignore
        from awo.models.alt_backend import LocalUpper  # type: ignore
        BACKENDS.update({"echo": LocalEcho(), "upper": LocalUpper()})
    except Exception as e:
        step_idx = 1
        step_id = "backend_info"
        _append_manifest_op(run_dir, manifest, step_idx, step_id, "backend_info")
        record_step(run_dir, step_idx, step_id, {"note": "using_fallback_backends", "detail": str(e), "ts": ts_rfc3339()})

    # 3) Load workflow (safe).
    wf_path = (REPO_ROOT / workflow_path).resolve()
    if not wf_path.exists():
        return _fatal(
            run_dir=run_dir,
            manifest=manifest,
            report=report,
            step_idx=2,
            step_id="init_error",
            msg=f"Workflow file not found: {wf_path}",
            started_at=started_at,
        )

    try:
        wf = json.loads(wf_path.read_text(encoding="utf-8"))
    except Exception as e:
        return _fatal(
            run_dir=run_dir,
            manifest=manifest,
            report=report,
            step_idx=3,
            step_id="init_error",
            msg=f"Failed to parse workflow JSON: {e}",
            started_at=started_at,
            extra_payload={"error": "json_parse"},
        )

    # 4) Freeze workflow used for provenance.
    write_text(run_dir / "workflow_frozen.json", json.dumps(wf, indent=2))

    # 5) Execute steps.
    for step_idx, step in enumerate(wf.get("steps", []), start=4):
        op = step.get("op")
        step_id = step.get("id", f"step_{step_idx}")
        _append_manifest_op(run_dir, manifest, step_idx, step_id, op or "unknown")

        rec: Dict[str, Any] = {"ts": ts_rfc3339(), "id": step_id, "op": op}

        # ------------------------- scope_validate ----------------------------
        if op == "scope_validate":
            args = step.get("args", {})
            claims, notes = _load_claims(args)
            scope_dir = run_dir / "scope"
            (scope_dir / "claims").mkdir(parents=True, exist_ok=True)

            results: List[Dict[str, Any]] = []
            overall_ok = True
            for c in claims:
                problems = _problems_for_claim(c)
                ok = len(problems) == 0
                overall_ok = overall_ok and ok
                cid = c.get("id") or f"claim-{sha256_hex_str(json.dumps(c, ensure_ascii=False))[:12]}"
                write_json(scope_dir / "claims" / f"{cid}.json", c)
                results.append({"id": cid, "ok": ok, "problems": problems})

            summary = {
                "claims_checked": len(claims),
                "overall_ok": overall_ok,
                "details": results,
                "notes": notes,
                "ts": ts_rfc3339(),
            }
            write_json(scope_dir / "summary.json", summary)

            # Provenance (Auditor role)
            summary_p = scope_dir / "summary.json"
            prov = _prov_record_template(
                manifest["run_id"],
                role="Auditor",
                model_name="scope-validator",
                provider="local",
                artifacts=[rel(summary_p)],
                hashes={rel(summary_p): f"sha256:{sha256_hex_bytes(summary_p.read_bytes())}"},
                notes="Scope/testability validation",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

            rec.update({"args": args, "summary": summary})
            record_step(run_dir, step_idx, step_id, rec)
            report += [
                f"## {step_idx}. scope_validate — {step_id}",
                f"- claims_checked: {summary['claims_checked']}",
                f"- overall_ok: {summary['overall_ok']}",
                "",
            ]
            continue

        # ------------------------- assert_contains ---------------------------
        if op == "assert_contains":
            args = step.get("args", {})
            src = args.get("from_step")
            field = args.get("field", "consensus_text")
            musts = [m for m in args.get("must_include", []) if isinstance(m, str)]
            if not src:
                return _fatal(
                    run_dir=run_dir,
                    manifest=manifest,
                    report=report,
                    step_idx=step_idx,
                    step_id=step_id,
                    msg="assert_contains: 'from_step' is required",
                    started_at=started_at,
                    extra_payload={"error": "missing_from_step"},
                )

            source = ctx.get(src)
            hay = ""
            if isinstance(source, dict) and field in source:
                hay = str(source[field])
            elif isinstance(source, list):
                hay = "\n".join([str(o.get("text", "")) for o in source])
            elif source is not None:
                hay = json.dumps(source, ensure_ascii=False)

            missing = [m for m in musts if m.lower() not in hay.lower()]
            ok = len(missing) == 0

            rec.update(
                {"from_step": src, "field": field, "must_include": musts, "missing": missing, "ok": ok, "sample": hay[:400]}
            )
            record_step(run_dir, step_idx, step_id, rec)

            # Provenance (Auditor)
            prov = _prov_record_template(
                manifest["run_id"],
                role="Auditor",
                model_name="assert-contains",
                provider="local",
                notes=f"must_include={musts}; missing={missing}",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

            if not ok:
                return _fatal(
                    run_dir=run_dir,
                    manifest=manifest,
                    report=report,
                    step_idx=step_idx,
                    step_id=step_id,
                    msg=f"assert_contains failed; missing: {missing}",
                    started_at=started_at,
                )

            report += [f"## {step_idx}. assert_contains — {step_id}", f"- ok: {ok}", ""]
            continue

        # ------------------------------ core ops -----------------------------
        if op == "fanout_generate":
            prompt = step["prompt"]
            models = step.get("models", ["echo", "upper", "reverse"])
            params = step.get("params", {"seed": 0})

            outs: List[Dict[str, Any]] = []
            for m in models:
                if m not in BACKENDS:
                    return _fatal(
                        run_dir=run_dir,
                        manifest=manifest,
                        report=report,
                        step_idx=step_idx,
                        step_id=step_id,
                        msg=f"Unknown model backend: {m}",
                        started_at=started_at,
                        extra_payload={"error": "unknown_backend"},
                    )
                step_started = ts_rfc3339()
                out = BACKENDS[m].generate(prompt, params=params)
                step_ended = ts_rfc3339()
                outs.append({"model": m, "text": out["text"], "meta": out["meta"]})

                # Provenance per model generation (Proposer)
                prov = _prov_record_template(
                    manifest["run_id"],
                    role="Proposer",
                    model_name=m,
                    provider="local",
                    version="fallback",
                    prompt_id=f"sha256:{sha256_hex_str(prompt)}",
                    params=params,
                    started=step_started,
                    ended=step_ended,
                    notes="fanout_generate",
                )
                provenance.append(prov)

            _write_provenance(run_dir, provenance)

            rec.update({"prompt": prompt, "models": models, "params": params, "outputs": outs})
            ctx[step_id] = outs
            record_step(run_dir, step_idx, step_id, rec)

            # ----------- report rendering (no backslashes inside f-expr) -----
            report += [
                f"## {step_idx}. fanout_generate — {step_id}",
                f"Prompt (sha256={sha256_hex_str(prompt)}):",
                "",
                "```",
                prompt,
                "```",
                "",
                "Outputs:",
            ]
            for o in outs:
                cleaned_text = o["text"].replace("\n", " ")[:200]
                report.append(f"- **{o['model']}** → {cleaned_text}")
            report.append("")

        elif op == "consensus_vote":
            src = step["inputs_from"]
            items = ctx.get(src, [])
            if not items:
                return _fatal(
                    run_dir=run_dir,
                    manifest=manifest,
                    report=report,
                    step_idx=step_idx,
                    step_id=step_id,
                    msg=f"consensus_vote: no inputs from '{src}'",
                    started_at=started_at,
                    extra_payload={"error": "missing_inputs"},
                )

            buckets: Dict[str, List[str]] = {}
            for o in items:
                k = norm_text(o["text"])
                buckets.setdefault(k, []).append(o["model"])

            ranked = sorted(buckets.items(), key=lambda kv: (len(kv[1]), len(kv[0])), reverse=True)
            if ranked:
                consensus_norm, voters = ranked[0]
                representative = next(o for o in items if norm_text(o["text"]) == consensus_norm)["text"]
            else:
                consensus_norm, voters, representative = "", [], ""

            rec.update(
                {
                    "inputs_from": src,
                    "total_candidates": len(items),
                    "voter_count": len(voters),
                    "voters": voters,
                    "consensus_norm": consensus_norm,
                    "consensus_text": representative,
                    "agreement_ratio": (len(voters) / max(1, len(items))),
                }
            )
            ctx[step_id] = rec
            record_step(run_dir, step_idx, step_id, rec)

            # Provenance (Consensus)
            prov = _prov_record_template(
                manifest["run_id"],
                role="Consensus",
                model_name="majority-vote",
                provider="local",
                notes=f"voters={voters}, agreement_ratio={rec['agreement_ratio']:.2f}",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

            report += [
                f"## {step_idx}. consensus_vote — {step_id}",
                f"- inputs_from: {src}",
                f"- voters: {', '.join(voters) if voters else '(none)'}",
                f"- agreement_ratio: {rec['agreement_ratio']:.2f}",
                "",
                "```",
                representative[:300],
                "```",
                "",
            ]

        elif op == "write_text":
            args = step.get("args", {})
            path = args["path"]
            text: Union[str, None] = args.get("text")
            from_step = args.get("from_step")
            field = args.get("field", "consensus_text")

            if text is None and from_step:
                source = ctx.get(from_step)
                if source is None:
                    return _fatal(
                        run_dir=run_dir,
                        manifest=manifest,
                        report=report,
                        step_idx=step_idx,
                        step_id=step_id,
                        msg=f"write_text: source step '{from_step}' not found",
                        started_at=started_at,
                        extra_payload={"error": "missing_source", "args": args},
                    )
                if isinstance(source, list):
                    text = "\n\n".join([str(o.get("text", "")) for o in source])
                elif isinstance(source, dict) and field in source:
                    text = str(source[field])
                else:
                    text = json.dumps(source, indent=2, ensure_ascii=False)

            if text is None:
                text = ""

            out_path = run_dir / "artifacts" / path
            write_text(out_path, text)
            file_hash = f"sha256:{sha256_hex_bytes(out_path.read_bytes())}"

            rec.update({"wrote": str(out_path), "from_step": from_step, "field": field if from_step else None})
            record_step(run_dir, step_idx, step_id, rec)
            report += [f"## {step_idx}. write_text — {step_id}", f"- wrote: {out_path}", ""]

            # Provenance (Editor)
            prov = _prov_record_template(
                manifest["run_id"],
                role="Editor",
                model_name="write-text",
                provider="local",
                artifacts=[rel(out_path)],
                hashes={rel(out_path): file_hash},
                notes="emit artifact",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

        elif op == "audit_gate":
            checklist = step.get("args", {}).get("checklist", "templates/audit-checklist.md")
            rec.update({"gate": {"status": "pending", "checklist": checklist, "ts": ts_rfc3339()}})
            record_step(run_dir, step_idx, step_id, rec)

            write_text(
                run_dir / "gate_decision.yml",
                f"status: pending\nchecklist: {checklist}\ncreated_at: {ts_rfc3339()}\n",
            )

            # Provenance (Auditor placeholder)
            prov = _prov_record_template(
                manifest["run_id"],
                role="Auditor",
                model_name="human-gate",
                provider="local",
                notes=f"checklist={checklist}",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

            # Mark manifest as pending_review BUT DO NOT finalize (no finished_at here)
            manifest["status"] = "pending_review"
            _validate_or_die(manifest, RUN_MANIFEST_SCHEMA, "run_manifest")
            write_json(run_dir / RUN_MANIFEST_PATH, manifest)
            update_index(run_dir, started_at=started_at, status="pending_review")
            finalize_report(
                run_dir,
                report
                + [
                    f"## {step_idx}. audit_gate — {step_id}",
                    f"- checklist: {checklist}",
                    "",
                    "> Run halted for human review.",
                    "",
                ],
            )
            breadcrumb(run_dir)
            _debug(f"Run created at: {run_dir}")
            return int(ExitCode.PENDING)

        else:
            return _fatal(
                run_dir=run_dir,
                manifest=manifest,
                report=report,
                step_idx=step_idx,
                step_id=step_id,
                msg=f"Unknown op: {op}",
                started_at=started_at,
                extra_payload={"error": "unknown_op"},
            )

    # Finished without hitting the gate → success
    finalize_report(run_dir, report)
    _finalize_manifest(run_dir, manifest, "succeeded")
    update_index(run_dir, started_at=started_at, status="succeeded", finished_at=ts_rfc3339())
    breadcrumb(run_dir)
    _debug(f"Run created at: {run_dir}")
    return int(ExitCode.OK)


# --------------------------------- CLI ---------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)
    try:
        sys.exit(run(sys.argv[1]))
    except Exception as e:
        # Leave a breadcrumb + minimal artifacts so CI can still find and package the run
        rd = ensure_run_dir()
        try:
            breadcrumb(rd)
        except Exception:
            pass

        write_json(
            rd / "steps" / "00_unhandled_error.json",
            {"error": "unhandled", "message": str(e), "ts": ts_rfc3339()},
        )
        write_text(
            rd / "report.md",
            f"# AWO Run Report — {rd.name}\n\n## Error\n\n{e}\n",
        )

        # Minimal manifest so downstream steps don’t break
        try:
            _ensure_schemas_loaded()
            m = {
                "run_id": rd.name,
                "workflow": "(unknown)",
                "started_at": ts_rfc3339(),
                "finished_at": ts_rfc3339(),
                "status": "error",
                "ops": [],
                "notes": [],
            }
            _validate_or_die(m, RUN_MANIFEST_SCHEMA, "run_manifest")
            write_json(rd / RUN_MANIFEST_PATH, m)
        except Exception:
            pass

        update_index(rd, started_at=ts_rfc3339(), status="error", finished_at=ts_rfc3339())
        print(f"[AWO] ERROR: {e}", file=sys.stderr)
        sys.exit(1)

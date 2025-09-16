#!/usr/bin/env python3
"""
AWO multi-model runner (CI/Actions safe).

Changes in this version:
- Emits schema-compliant run_manifest.json (start/update/finalize)
- Emits schema-compliant provenance.json (per step + artifacts)
- Validates both with jsonschema (fail-fast)
- Deterministic local backends (echo/upper/reverse) by default
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

# --- required for schema validation (install in CI): pip install jsonschema ---
try:
    import jsonschema
except Exception:
    print("[AWO] FATAL: jsonschema not installed. Add `pip install jsonschema` in CI.", file=sys.stderr)
    raise

EXIT_PENDING = 78  # conventional code to indicate "needs human review"

# ---------------------------- repo-rooted paths ------------------------------
REPO_ROOT = Path(os.getenv("GITHUB_WORKSPACE", Path.cwd())).resolve()
RUNS_ROOT = (REPO_ROOT / "runs").resolve()
SCHEMAS_ROOT = (REPO_ROOT / "schemas").resolve()

RUN_MANIFEST_PATH = "run_manifest.json"
PROVENANCE_PATH = "provenance.json"

def _debug(msg: str) -> None:
    print(f"[AWO] {msg}", file=sys.stdout, flush=True)

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

# ------------------------------- small utils ---------------------------------
def now_safe() -> str:
    """Filename-safe UTC timestamp (used for directory names)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

def now_rfc3339() -> str:
    """RFC3339 timestamp for schema `date-time` fields."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def sha12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())

def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")

def nonnull(d: Dict[str, Any]) -> Dict[str, Any]:
    """Drop any keys whose value is None (schemas reject null for many strings)."""
    return {k: v for k, v in d.items() if v is not None}

def ensure_run_dir() -> Path:
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    rd = RUNS_ROOT / f"run_{now_safe()}"
    (rd / "steps").mkdir(parents=True, exist_ok=True)
    (rd / "artifacts").mkdir(parents=True, exist_ok=True)
    if not rd.exists():
        raise RuntimeError(f"Failed to create run dir: {rd}")
    return rd

def breadcrumb(run_dir: Path) -> None:
    """Write runs/LAST_RUN and verify."""
    last_run = RUNS_ROOT / "LAST_RUN"
    write_text(last_run, run_dir.name)
    for _ in range(3):
        try:
            val = last_run.read_text(encoding="utf-8").strip()
            if val == run_dir.name:
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
        f"- Started: {now_rfc3339()}",
        "",
    ]

def record_step(run_dir: Path, idx: int, step_id: str, payload: Dict[str, Any]) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{step_id}.json", payload)

def finalize_report(run_dir: Path, report_lines: List[str]) -> None:
    write_text(run_dir / "report.md", "\n".join(report_lines))

# ------------------------------ schema helpers -------------------------------
def _load_schema(name: str) -> Dict[str, Any]:
    p = (SCHEMAS_ROOT / name).resolve()
    if not p.exists():
        raise FileNotFoundError(f"Schema not found: {p}")
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Invalid JSON in schema {p}: {e}")

RUN_MANIFEST_SCHEMA = None
PROVENANCE_SCHEMA = None

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
    m = nonnull({
        "run_id": run_dir.name,
        "workflow": workflow_path,
        "started_at": started_at,
        "finished_at": None,           # allowed to be null per schema
        "status": "running",
        "ops": [],
        "notes": [],
    })
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
    manifest["finished_at"] = now_rfc3339()
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
        "model": {"name": model_name},
        # prompt_id is OPTIONAL — DO NOT include if None
        "seed": (params or {}).get("seed"),
        "artifacts": artifacts or [],
        "hashes": hashes or {},
        "started": started or now_rfc3339(),
        "ended": ended or now_rfc3339(),
        # notes optional
    }
    if provider:
        rec["model"]["provider"] = provider
    if version:
        rec["model"]["version"] = version
    if prompt_id is not None:
        rec["prompt_id"] = prompt_id
    if notes is not None:
        rec["notes"] = notes
    # drop any residual Nones
    return nonnull(rec)

# --------------------------------- main --------------------------------------
def update_index(run_dir: Path, *, started_at: str, status: str, finished_at: str | None = None) -> None:
    idx = nonnull({"run_id": run_dir.name, "started_at": started_at, "status": status, "finished_at": finished_at})
    write_json(run_dir / "index.json", idx)

def run(workflow_path: str) -> int:
    # 1) Create run dir + breadcrumb FIRST so CI can always find it.
    run_dir = ensure_run_dir()
    breadcrumb(run_dir)
    started_at = now_rfc3339()

    # Initialize manifest + provenance
    manifest = _init_run_manifest(run_dir, workflow_path, started_at)
    provenance: List[Dict[str, Any]] = _init_provenance(run_dir)

    _debug(f"Repo root: {REPO_ROOT}")
    _debug(f"Runs root: {RUNS_ROOT}")
    _debug(f"Run dir : {run_dir}")
    _debug(f"Breadcrumb: {(RUNS_ROOT / 'LAST_RUN')}")

    report = init_report(run_dir, workflow_path)
    step_idx = 0
    ctx: Dict[str, Any] = {}

    # 2) Optional local overrides; keep fallbacks if imports fail.
    BACKENDS = {"echo": _Echo(), "upper": _Upper(), "reverse": _Reverse()}
    try:
        from awo.models.local_backend import LocalEcho  # type: ignore
        from awo.models.alt_backend import LocalUpper  # type: ignore
        BACKENDS.update({"echo": LocalEcho(), "upper": LocalUpper()})
    except Exception as e:
        step_idx += 1
        step_id = "backend_info"
        _append_manifest_op(run_dir, manifest, step_idx, step_id, "backend_info")
        record_step(run_dir, step_idx, step_id, {"note": "using_fallback_backends", "detail": str(e), "ts": now_rfc3339()})

    # 3) Load workflow (safe).
    wf_path = (REPO_ROOT / workflow_path).resolve()
    if not wf_path.exists():
        msg = f"Workflow file not found: {wf_path}"
        step_idx += 1
        step_id = "init_error"
        _append_manifest_op(run_dir, manifest, step_idx, step_id, "init_error")
        record_step(run_dir, step_idx, step_id, {"error": "workflow_missing", "message": msg, "ts": now_rfc3339()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        _finalize_manifest(run_dir, manifest, "error")
        update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    try:
        wf = json.loads(wf_path.read_text(encoding="utf-8"))
    except Exception as e:
        msg = f"Failed to parse workflow JSON: {e}"
        step_idx += 1
        step_id = "init_error"
        _append_manifest_op(run_dir, manifest, step_idx, step_id, "init_error")
        record_step(run_dir, step_idx, step_id, {"error": "json_parse", "message": str(e), "ts": now_rfc3339()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        _finalize_manifest(run_dir, manifest, "error")
        update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    # 4) Freeze workflow used for provenance.
    write_text(run_dir / "workflow_frozen.json", json.dumps(wf, indent=2))

    # 5) Execute steps.
    for step in wf.get("steps", []):
        step_idx += 1
        op = step.get("op")
        step_id = step.get("id", f"step_{step_idx}")
        _append_manifest_op(run_dir, manifest, step_idx, step_id, op or "unknown")

        rec: Dict[str, Any] = {"ts": now_rfc3339(), "id": step_id, "op": op}

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
                cid = c.get("id") or f"claim-{sha12(json.dumps(c, ensure_ascii=False))}"
                write_json(scope_dir / "claims" / f"{cid}.json", c)
                results.append({"id": cid, "ok": ok, "problems": problems})

            summary = {"claims_checked": len(claims), "overall_ok": overall_ok, "details": results, "notes": notes, "ts": now_rfc3339()}
            write_json(scope_dir / "summary.json", summary)

            # Provenance (Auditor)
            prov = _prov_record_template(
                manifest["run_id"],
                role="Auditor",
                model_name="scope-validator",
                provider="local",
                artifacts=[str(scope_dir / "summary.json")],
                hashes={str(scope_dir / "summary.json"): f"sha256:{sha256_hex((scope_dir / 'summary.json').read_bytes())}"},
                notes="Scope/testability validation",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

            rec.update({"args": args, "summary": summary})
            record_step(run_dir, step_idx, step_id, rec)
            report += [f"## {step_idx}. scope_validate — {step_id}", f"- claims_checked: {summary['claims_checked']}", f"- overall_ok: {summary['overall_ok']}", ""]
            continue

        # ------------------------- assert_contains ---------------------------
        if op == "assert_contains":
            args = step.get("args", {})
            src = args.get("from_step")
            field = args.get("field", "consensus_text")
            musts = [m for m in args.get("must_include", []) if isinstance(m, str)]
            if not src:
                msg = "assert_contains: 'from_step' is required"
                rec.update({"error": "missing_from_step"})
                record_step(run_dir, step_idx, step_id, rec)
                report += ["## Error", "", msg, ""]
                finalize_report(run_dir, report)
                _finalize_manifest(run_dir, manifest, "error")
                update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
                print(f"[AWO] {msg}", file=sys.stderr)
                return 2

            source = ctx.get(src)
            hay = ""
            if isinstance(source, dict) and field in source:
                hay = str(source[field])
            elif isinstance(source, list):  # e.g., fanout outputs
                hay = "\n".join([str(o.get("text", "")) for o in source])
            elif source is not None:
                hay = json.dumps(source, ensure_ascii=False)

            missing = [m for m in musts if m.lower() not in hay.lower()]
            ok = len(missing) == 0

            rec.update({"from_step": src, "field": field, "must_include": musts, "missing": missing, "ok": ok, "sample": hay[:400]})
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
                msg = f"assert_contains failed; missing: {missing}"
                report += ["## Error", "", msg, ""]
                finalize_report(run_dir, report)
                _finalize_manifest(run_dir, manifest, "error")
                update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
                print(f"[AWO] {msg}", file=sys.stderr)
                return 2

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
                    msg = f"Unknown model backend: {m}"
                    rec.update({"error": "unknown_backend", "message": msg})
                    record_step(run_dir, step_idx, step_id, rec)
                    report += ["## Error", "", msg, ""]
                    finalize_report(run_dir, report)
                    _finalize_manifest(run_dir, manifest, "error")
                    update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
                    print(f"[AWO] {msg}", file=sys.stderr)
                    return 2
                step_started = now_rfc3339()
                out = BACKENDS[m].generate(prompt, params=params)
                step_ended = now_rfc3339()
                outs.append({"model": m, "text": out["text"], "meta": out["meta"]})

                # Provenance per model generation (Proposer)
                prov = _prov_record_template(
                    manifest["run_id"],
                    role="Proposer",
                    model_name=m,
                    provider="local",
                    version="fallback",
                    prompt_id=f"sha256:{sha12(prompt)}",
                    params=params,
                    notes="fanout_generate",
                    started=step_started,
                    ended=step_ended,
                )
                provenance.append(prov)

            _write_provenance(run_dir, provenance)

            rec.update({"prompt": prompt, "models": models, "params": params, "outputs": outs})
            ctx[step_id] = outs
            record_step(run_dir, step_idx, step_id, rec)

            report += [
                f"## {step_idx}. fanout_generate — {step_id}",
                f"Prompt (sha12={sha12(prompt)}):",
                "",
                "```",
                prompt,
                "```",
                "",
                "Outputs:",
            ]
            for o in outs:
                report.append(f"- **{o['model']}** → {o['text'].replace('\\n',' ')[:200]}")
            report.append("")

        elif op == "consensus_vote":
            src = step["inputs_from"]
            items = ctx.get(src, [])
            if not items:
                msg = f"consensus_vote: no inputs from '{src}'"
                rec.update({"error": "missing_inputs", "message": msg})
                record_step(run_dir, step_idx, step_id, rec)
                report += ["## Error", "", msg, ""]
                finalize_report(run_dir, report)
                _finalize_manifest(run_dir, manifest, "error")
                update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
                print(f"[AWO] {msg}", file=sys.stderr)
                return 2

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

            rec.update({
                "inputs_from": src,
                "total_candidates": len(items),
                "voter_count": len(voters),
                "voters": voters,
                "consensus_norm": consensus_norm,
                "consensus_text": representative,
                "agreement_ratio": (len(voters) / max(1, len(items))),
            })
            ctx[step_id] = rec
            record_step(run_dir, step_idx, step_id, rec)

            # Provenance (Consensus) — no prompt_id
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
                    msg = f"write_text: source step '{from_step}' not found"
                    rec.update({"error": "missing_source", "message": msg, "args": args})
                    record_step(run_dir, step_idx, step_id, rec)
                    report += ["## Error", "", msg, ""]
                    finalize_report(run_dir, report)
                    _finalize_manifest(run_dir, manifest, "error")
                    update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
                    print(f"[AWO] {msg}", file=sys.stderr)
                    return 2

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

            # Compute file hash for provenance
            h = f"sha256:{sha256_hex(out_path.read_bytes())}"

            rec.update({"wrote": str(out_path), "from_step": from_step, "field": field if from_step else None})
            record_step(run_dir, step_idx, step_id, rec)
            report += [f"## {step_idx}. write_text — {step_id}", f"- wrote: {out_path}", ""]

            # Provenance (Editor)
            prov = _prov_record_template(
                manifest["run_id"],
                role="Editor",
                model_name="write-text",
                provider="local",
                artifacts=[str(out_path)],
                hashes={str(out_path): h},
                notes="emit artifact",
            )
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

        elif op == "audit_gate":
            checklist = step.get("args", {}).get("checklist", "templates/audit-checklist.md")
            rec.update({"gate": {"status": "pending", "checklist": checklist, "ts": now_rfc3339()}})
            record_step(run_dir, step_idx, step_id, rec)

            write_text(run_dir / "gate_decision.yml", f"status: pending\nchecklist: {checklist}\ncreated_at: {now_rfc3339()}\n")

            # Provenance (Auditor placeholder)
            prov = _prov_record_template(manifest["run_id"], role="Auditor", model_name="human-gate", provider="local", notes=f"checklist={checklist}")
            provenance.append(prov)
            _write_provenance(run_dir, provenance)

            report += [
                f"## {step_idx}. audit_gate — {step_id}",
                f"- checklist: {checklist}",
                "",
                "> Run halted for human review.",
                "",
            ]
            finalize_report(run_dir, report)
            _finalize_manifest(run_dir, manifest, "pending_review")
            update_index(run_dir, started_at=started_at, status="pending_review")
            breadcrumb(run_dir)
            _debug(f"Run created at: {run_dir}")
            return EXIT_PENDING

        else:
            msg = f"Unknown op: {op}"
            rec.update({"error": "unknown_op", "message": msg})
            record_step(run_dir, step_idx, step_id, rec)
            report += ["## Error", "", msg, ""]
            finalize_report(run_dir, report)
            _finalize_manifest(run_dir, manifest, "error")
            update_index(run_dir, started_at=started_at, status="error", finished_at=now_rfc3339())
            print(f"[AWO] {msg}", file=sys.stderr)
            return 2

    # Finished without hitting the gate
    finalize_report(run_dir, report)
    _finalize_manifest(run_dir, manifest, "succeeded")
    update_index(run_dir, started_at=started_at, status="succeeded", finished_at=now_rfc3339())
    breadcrumb(run_dir)
    _debug(f"Run created at: {run_dir}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)
    try:
        sys.exit(run(sys.argv[1]))
    except Exception as e:
        # Last-ditch safety: still produce a run, breadcrumb, index, and report.
        rd = ensure_run_dir()
        try:
            breadcrumb(rd)
        except Exception:
            pass
        write_json(rd / "steps" / "00_unhandled_error.json", {"error": "unhandled", "message": str(e), "ts": now_rfc3339()})
        write_text(rd / "report.md", f"# AWO Run Report — {rd.name}\n\n## Error\n\n{e}\n")
        try:
            _ensure_schemas_loaded()
            m = nonnull({
                "run_id": rd.name,
                "workflow": "(unknown)",
                "started_at": now_rfc3339(),
                "finished_at": now_rfc3339(),
                "status": "error",
                "ops": [],
                "notes": ["unhandled_error"],
            })
            _validate_or_die(m, RUN_MANIFEST_SCHEMA, "run_manifest")
            write_json(rd / RUN_MANIFEST_PATH, m)
        except Exception:
            pass
        update_index(rd, started_at=now_rfc3339(), status="error", finished_at=now_rfc3339())
        print(f"[AWO] ERROR: {e}", file=sys.stderr)
        sys.exit(1)

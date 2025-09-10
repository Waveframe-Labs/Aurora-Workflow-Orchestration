#!/usr/bin/env python3
"""
AWO multi-model runner (stdlib only, CI/Actions safe).

Adds:
- index.json in each run root with {run_id, started_at, status, finished_at?}
- third simulated backend "reverse" for clearer multi-model fan-out
- dynamic write_text (from_step / field) and CI-safe breadcrumbs
- NEW: scope_validate op that enforces testable (falsifiable) claims

Statuses written to index.json:
  running  -> set when run starts
  pending_review -> audit_gate hit (exit 78)
  succeeded -> finished without gate
  error -> any failure path
"""

from __future__ import annotations
import json, re, sys, hashlib, shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Union, Tuple

EXIT_PENDING = 78

# ------------------------ tiny fallback backends ------------------------------
class _Echo:
    def generate(self, prompt: str, params=None):
        return {"text": prompt, "meta": {"engine": "fallback:echo", "seed": (params or {}).get("seed", 0)}}

class _Upper:
    def generate(self, prompt: str, params=None):
        return {"text": (prompt or "").upper(), "meta": {"engine": "fallback:upper", "seed": (params or {}).get("seed", 0)}}

class _Reverse:
    def generate(self, prompt: str, params=None):
        return {"text": (prompt or "")[::-1], "meta": {"engine": "fallback:reverse", "seed": (params or {}).get("seed", 0)}}

# ------------------------------- utils ---------------------------------------
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

def sha12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())

def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def write_json(p: Path, obj: Any) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")

def ensure_run_dir() -> Path:
    Path("runs").mkdir(exist_ok=True)
    rd = Path("runs") / f"run_{now_iso()}"
    (rd / "steps").mkdir(parents=True, exist_ok=True)
    (rd / "artifacts").mkdir(parents=True, exist_ok=True)
    return rd

def breadcrumb(run_dir: Path) -> None:
    write_text(Path("runs") / "LAST_RUN", run_dir.name)

def init_report(run_dir: Path, workflow_path: str) -> List[str]:
    return [
        f"# AWO Run Report — {run_dir.name}", "",
        f"- Workflow: {workflow_path}", f"- Started: {now_iso()}", ""
    ]

def record_step(run_dir: Path, idx: int, step_id: str, payload: Dict[str, Any]) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{step_id}.json", payload)

def finalize_report(run_dir: Path, report_lines: List[str]) -> None:
    write_text(run_dir / "report.md", "\n".join(report_lines))

def write_index(run_dir: Path, *, started_at: str, status: str, finished_at: str | None = None) -> None:
    idx = {"run_id": run_dir.name, "started_at": started_at, "status": status}
    if finished_at:
        idx["finished_at"] = finished_at
    write_json(run_dir / "index.json", idx)

# ----------------------------- scope helpers ---------------------------------
REQUIRED_CLAIM_FIELDS = ["id", "statement"]
REQUIRED_TESTABILITY = ["predictions", "falsification_tests"]  # at least one non-empty

def _problems_for_claim(claim: Dict[str, Any]) -> List[str]:
    probs: List[str] = []
    for f in REQUIRED_CLAIM_FIELDS:
        if f not in claim or claim[f] in (None, "", []):
            probs.append(f"missing field: {f}")
    # At least one of the testability buckets must be non-empty
    preds = claim.get("predictions", [])
    tests = claim.get("falsification_tests", [])
    if not preds and not tests:
        probs.append("claim is not testable: no predictions and no falsification_tests")
    # If predictions exist, require tolerances
    for i, p in enumerate(preds or []):
        tol = (p or {}).get("tolerance")
        if not tol:
            probs.append(f"prediction[{i}] missing tolerance")
    # If tests exist, require a recognizable shape
    for i, t in enumerate(tests or []):
        if not isinstance(t, dict) or not any(k in t for k in ("must_pass", "fail_if")):
            probs.append(f"falsification_tests[{i}] missing must_pass/fail_if")
    return probs

def _load_claims(args: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[str]]:
    loaded: List[Dict[str, Any]] = []
    notes: List[str] = []
    # Inline claim
    if "claim" in args and isinstance(args["claim"], dict):
        loaded.append(args["claim"])
    # Glob claims
    glob = args.get("claims_glob")
    if glob:
        for p in Path(".").glob(glob):
            try:
                loaded.append(json.loads(Path(p).read_text(encoding="utf-8")))
            except Exception as e:
                notes.append(f"failed to parse {p}: {e}")
    return loaded, notes

# ------------------------------- main ----------------------------------------
def run(workflow_path: str) -> int:
    # 1) Create run dir + breadcrumb FIRST so CI can always find it.
    run_dir = ensure_run_dir()
    breadcrumb(run_dir)
    started_at = now_iso()
    write_index(run_dir, started_at=started_at, status="running")

    report = init_report(run_dir, workflow_path)
    step_idx = 0
    ctx: Dict[str, Any] = {}

    # 2) Optional backends; if imports fail, keep fallbacks (echo/upper/reverse).
    BACKENDS = {"echo": _Echo(), "upper": _Upper(), "reverse": _Reverse()}
    try:
        from awo.models.local_backend import LocalEcho
        from awo.models.alt_backend import LocalUpper
        BACKENDS.update({"echo": LocalEcho(), "upper": LocalUpper()})
    except Exception as e:
        record_step(run_dir, step_idx, "backend_info",
                    {"note": "using_fallback_backends", "detail": str(e), "ts": now_iso()})

    # 3) Load workflow safely.
    wf_file = Path(workflow_path)
    if not wf_file.exists():
        msg = f"Workflow file not found: {workflow_path}"
        record_step(run_dir, step_idx, "init_error", {"error": "workflow_missing", "message": msg, "ts": now_iso()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        write_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    try:
        wf = json.loads(wf_file.read_text(encoding="utf-8"))
    except Exception as e:
        msg = f"Failed to parse workflow JSON: {e}"
        record_step(run_dir, step_idx, "init_error", {"error": "json_parse", "message": str(e), "ts": now_iso()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        write_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    # 4) Freeze the workflow used.
    write_text(run_dir / "workflow_frozen.json", json.dumps(wf, indent=2))

    # 5) Execute steps.
    for step in wf.get("steps", []):
        step_idx += 1
        op = step.get("op")
        step_id = step.get("id", f"step_{step_idx}")
        rec: Dict[str, Any] = {"ts": now_iso(), "id": step_id, "op": op}

        # ----- NEW: scope_validate -------------------------------------------
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
                # copy each claim into the run for provenance
                cid = c.get("id") or f"claim-{sha12(json.dumps(c))}"
                write_json(scope_dir / "claims" / f"{cid}.json", c)
                results.append({"id": cid, "ok": ok, "problems": problems})

            summary = {
                "claims_checked": len(claims),
                "overall_ok": overall_ok,
                "details": results,
                "notes": notes,
                "ts": now_iso(),
            }
            write_json(scope_dir / "summary.json", summary)
            # Human-friendly markdown for quick review
            md = [f"# Scope Check — {run_dir.name}", ""]
            if not claims:
                md += ["**No claims found.** Gate will likely block.", ""]
            for r in results:
                md += [f"## {r['id']} — {'OK' if r['ok'] else 'PROBLEMS'}", ""]
                if r["problems"]:
                    md += [f"- {p}" for p in r["problems"]] + [""]
            md += [f"**OVERALL:** {'OK' if overall_ok else 'NOT OK'}"]
            write_text(scope_dir / "README.md", "\n".join(md))

            rec.update({"args": args, "summary": summary})
            record_step(run_dir, step_idx, step_id, rec)
            report += [f"## {step_idx}. scope_validate — {step_id}",
                       f"- claims_checked: {summary['claims_checked']}",
                       f"- overall_ok: {summary['overall_ok']}", ""]
            continue

        # ----- existing ops --------------------------------------------------
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
                    write_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
                    print(f"[AWO] {msg}", file=sys.stderr)
                    return 2
                out = BACKENDS[m].generate(prompt, params=params)
                outs.append({"model": m, "text": out["text"], "meta": out["meta"]})
            rec.update({"prompt": prompt, "models": models, "params": params, "outputs": outs})
            ctx[step_id] = outs
            record_step(run_dir, step_idx, step_id, rec)
            report += [
                f"## {step_idx}. fanout_generate — {step_id}",
                f"Prompt (sha12={sha12(prompt)}):", "", "```", prompt, "```", "",
                "Outputs:",
            ] + [f"- **{o['model']}** → {o['text'].replace('\n',' ')[:200]}" for o in outs] + [""]

        elif op == "consensus_vote":
            src = step["inputs_from"]
            items = ctx.get(src, [])
            if not items:
                msg = f"consensus_vote: no inputs from '{src}'"
                rec.update({"error": "missing_inputs", "message": msg})
                record_step(run_dir, step_idx, step_id, rec)
                report += ["## Error", "", msg, ""]
                finalize_report(run_dir, report)
                write_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
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
            report += [
                f"## {step_idx}. consensus_vote — {step_id}",
                f"- inputs_from: {src}",
                f"- voters: {', '.join(voters) if voters else '(none)'}",
                f"- agreement_ratio: {rec['agreement_ratio']:.2f}",
                "", "```", representative[:300], "```", ""
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
                    write_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
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
            rec.update({"wrote": str(out_path), "from_step": from_step, "field": field if from_step else None})
            record_step(run_dir, step_idx, step_id, rec)
            report += [f"## {step_idx}. write_text — {step_id}", f"- wrote: {out_path}", ""]

        elif op == "audit_gate":
            checklist = step.get("args", {}).get("checklist", "templates/audit-checklist.md")
            rec.update({"gate": {"status": "pending", "checklist": checklist, "ts": now_iso()}})
            record_step(run_dir, step_idx, step_id, rec)
            write_text(run_dir / "gate_decision.yml",
                       f"status: pending\nchecklist: {checklist}\ncreated_at: {now_iso()}\n")
            report += [f"## {step_idx}. audit_gate — {step_id}",
                       f"- checklist: {checklist}", "", "> Run halted for human review.", ""]
            finalize_report(run_dir, report)
            write_index(run_dir, started_at=started_at, status="pending_review")
            breadcrumb(run_dir)
            print(f"[AWO] Run created at: {run_dir}")
            return EXIT_PENDING

        else:
            msg = f"Unknown op: {op}"
            rec.update({"error": "unknown_op", "message": msg})
            record_step(run_dir, step_idx, step_id, rec)
            report += ["## Error", "", msg, ""]
            finalize_report(run_dir, report)
            write_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
            print(f"[AWO] {msg}", file=sys.stderr)
            return 2

    # Finished without gate
    finalize_report(run_dir, report)
    write_index(run_dir, started_at=started_at, status="succeeded", finished_at=now_iso())
    breadcrumb(run_dir)
    print(f"[AWO] Run created at: {run_dir}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)
    try:
        sys.exit(run(sys.argv[1]))
    except Exception as e:
        rd = ensure_run_dir()
        breadcrumb(rd)
        write_json(rd / "steps" / "00_unhandled_error.json",
                   {"error": "unhandled", "message": str(e), "ts": now_iso()})
        write_text(rd / "report.md", f"# AWO Run Report — {rd.name}\n\n## Error\n\n{e}\n")
        write_index(rd, started_at=now_iso(), status="error", finished_at=now_iso())
        print(f"[AWO] ERROR: {e}", file=sys.stderr)
        sys.exit(1)

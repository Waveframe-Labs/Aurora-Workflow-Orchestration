#!/usr/bin/env python3
"""
AWO multi-model runner (stdlib only, CI/Actions safe).

Features
- Deterministic local "backends": echo / upper / reverse (no external APIs)
- fanout_generate, consensus_vote, write_text, audit_gate
- scope_validate: block unfalsifiable claims early
- assert_contains: simple content gate for sanity checks
- Provenance per-run:
    runs/
      run_YYYY-MM-DDTHH-MM-SSZ/
        index.json            # {run_id, started_at, status[, finished_at]}
        workflow_frozen.json  # exact JSON executed
        report.md             # human-readable run report
        steps/*.json          # machine-readable step records
        artifacts/...         # any files emitted by write_text
        scope/claims/*.json   # (optional) copied claims checked
        scope/summary.json    # (optional) scope validation summary
- Breadcrumb for CI:
    runs/LAST_RUN -> run directory name

Statuses in index.json:
  running         -> set when run starts
  pending_review  -> audit_gate hit (exit 78)
  succeeded       -> finished without gate
  error           -> any failure path
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

EXIT_PENDING = 78  # conventional code to indicate "needs human review"

# ---------------------------- repo-rooted paths ------------------------------
REPO_ROOT = Path(os.getenv("GITHUB_WORKSPACE", Path.cwd())).resolve()
RUNS_ROOT = (REPO_ROOT / "runs").resolve()

def _debug(msg: str) -> None:
    print(f"[AWO] {msg}", file=sys.stdout, flush=True)

# --------------------------- deterministic local backends --------------------
class _Echo:
    def generate(self, prompt: str, params=None):
        return {
            "text": prompt,
            "meta": {"engine": "fallback:echo", "seed": (params or {}).get("seed", 0)},
        }

class _Upper:
    def generate(self, prompt: str, params=None):
        return {
            "text": (prompt or "").upper(),
            "meta": {"engine": "fallback:upper", "seed": (params or {}).get("seed", 0)},
        }

class _Reverse:
    def generate(self, prompt: str, params=None):
        return {
            "text": (prompt or "")[::-1],
            "meta": {"engine": "fallback:reverse", "seed": (params or {}).get("seed", 0)},
        }

# ------------------------------- small utils ---------------------------------
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

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

def ensure_run_dir() -> Path:
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    rd = RUNS_ROOT / f"run_{now_iso()}"
    (rd / "steps").mkdir(parents=True, exist_ok=True)
    (rd / "artifacts").mkdir(parents=True, exist_ok=True)
    # verify directory exists
    if not rd.exists():
        raise RuntimeError(f"Failed to create run dir: {rd}")
    return rd

def breadcrumb(run_dir: Path) -> None:
    """Write runs/LAST_RUN with verification (absolute repo path)."""
    last_run = RUNS_ROOT / "LAST_RUN"
    write_text(last_run, run_dir.name)
    # fsync/verify write in CI environments
    for _ in range(3):
        try:
            # Re-read to verify
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
        f"- Started: {now_iso()}",
        "",
    ]

def record_step(run_dir: Path, idx: int, step_id: str, payload: Dict[str, Any]) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{step_id}.json", payload)

def finalize_report(run_dir: Path, report_lines: List[str]) -> None:
    write_text(run_dir / "report.md", "\n".join(report_lines))

def update_index(run_dir: Path, *, started_at: str, status: str, finished_at: str | None = None) -> None:
    idx = {"run_id": run_dir.name, "started_at": started_at, "status": status}
    if finished_at:
        idx["finished_at"] = finished_at
    write_json(run_dir / "index.json", idx)

# --------------------------- scope validation helpers ------------------------
REQUIRED_CLAIM_FIELDS = ["id", "statement"]

def _problems_for_claim(claim: Dict[str, Any]) -> List[str]:
    probs: List[str] = []
    # Required fields
    for f in REQUIRED_CLAIM_FIELDS:
        if f not in claim or claim[f] in (None, "", []):
            probs.append(f"missing field: {f}")
    # Testability: at least one of predictions / falsification_tests present and non-empty
    preds = claim.get("predictions", [])
    tests = claim.get("falsification_tests", [])
    if not preds and not tests:
        probs.append("claim is not testable: no predictions and no falsification_tests")
    # If predictions exist, require a tolerance block
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
    # Glob claims from the repo (e.g., claims/*.json)
    glob = args.get("claims_glob")
    if glob:
        for p in REPO_ROOT.glob(glob):
            try:
                loaded.append(json.loads(Path(p).read_text(encoding="utf-8")))
            except Exception as e:
                notes.append(f"failed to parse {p}: {e}")
    return loaded, notes

# --------------------------------- main --------------------------------------
def run(workflow_path: str) -> int:
    # 1) Create run dir + breadcrumb FIRST so CI can always find it.
    run_dir = ensure_run_dir()
    breadcrumb(run_dir)
    started_at = now_iso()
    update_index(run_dir, started_at=started_at, status="running")

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
        record_step(
            run_dir,
            step_idx,
            "backend_info",
            {"note": "using_fallback_backends", "detail": str(e), "ts": now_iso()},
        )

    # 3) Load workflow (safe).
    wf_path = (REPO_ROOT / workflow_path).resolve()
    if not wf_path.exists():
        msg = f"Workflow file not found: {wf_path}"
        record_step(run_dir, step_idx, "init_error", {"error": "workflow_missing", "message": msg, "ts": now_iso()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    try:
        wf = json.loads(wf_path.read_text(encoding="utf-8"))
    except Exception as e:
        msg = f"Failed to parse workflow JSON: {e}"
        record_step(run_dir, step_idx, "init_error", {"error": "json_parse", "message": str(e), "ts": now_iso()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    # 4) Freeze workflow used for provenance.
    write_text(run_dir / "workflow_frozen.json", json.dumps(wf, indent=2))

    # 5) Execute steps.
    for step in wf.get("steps", []):
        step_idx += 1
        op = step.get("op")
        step_id = step.get("id", f"step_{step_idx}")
        rec: Dict[str, Any] = {"ts": now_iso(), "id": step_id, "op": op}

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

            summary = {
                "claims_checked": len(claims),
                "overall_ok": overall_ok,
                "details": results,
                "notes": notes,
                "ts": now_iso(),
            }
            write_json(scope_dir / "summary.json", summary)

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
                msg = "assert_contains: 'from_step' is required"
                rec.update({"error": "missing_from_step"})
                record_step(run_dir, step_idx, step_id, rec)
                report += ["## Error", "", msg, ""]
                finalize_report(run_dir, report)
                update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
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

            rec.update(
                {"from_step": src, "field": field, "must_include": musts, "missing": missing, "ok": ok, "sample": hay[:400]}
            )
            record_step(run_dir, step_idx, step_id, rec)

            if not ok:
                msg = f"assert_contains failed; missing: {missing}"
                report += ["## Error", "", msg, ""]
                finalize_report(run_dir, report)
                update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
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
                    update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
                    print(f"[AWO] {msg}", file=sys.stderr)
                    return 2
                out = BACKENDS[m].generate(prompt, params=params)
                outs.append({"model": m, "text": out["text"], "meta": out["meta"]})

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
                report.append(f"- **{o['model']}** → {o['text'].replace('\n',' ')[:200]}")
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
                update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
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
                    update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
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

            write_text(
                run_dir / "gate_decision.yml",
                f"status: pending\nchecklist: {checklist}\ncreated_at: {now_iso()}\n",
            )

            report += [
                f"## {step_idx}. audit_gate — {step_id}",
                f"- checklist: {checklist}",
                "",
                "> Run halted for human review.",
                "",
            ]
            finalize_report(run_dir, report)
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
            update_index(run_dir, started_at=started_at, status="error", finished_at=now_iso())
            print(f"[AWO] {msg}", file=sys.stderr)
            return 2

    # Finished without hitting the gate
    finalize_report(run_dir, report)
    update_index(run_dir, started_at=started_at, status="succeeded", finished_at=now_iso())
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
        write_json(rd / "steps" / "00_unhandled_error.json",
                   {"error": "unhandled", "message": str(e), "ts": now_iso()})
        write_text(rd / "report.md", f"# AWO Run Report — {rd.name}\n\n## Error\n\n{e}\n")
        update_index(rd, started_at=now_iso(), status="error", finished_at=now_iso())
        print(f"[AWO] ERROR: {e}", file=sys.stderr)
        sys.exit(1)

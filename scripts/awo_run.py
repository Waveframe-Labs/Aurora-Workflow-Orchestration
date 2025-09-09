#!/usr/bin/env python3
"""
AWO multi-model runner (stdlib only, CI-safe).

Guarantees
- Creates runs/run_YYYY-MM-DDTHH-MM-SSZ immediately and writes runs/LAST_RUN.
- On any failure (missing workflow, bad JSON, unknown op), writes an ERROR
  record + report.md inside the run, then exits nonzero.
- On audit_gate, writes report.md and exits with code 78 (pending human review).

Ops supported
  - fanout_generate
  - consensus_vote
  - write_text
  - audit_gate
"""

from __future__ import annotations
import json, re, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

# ---- deterministic local backends (no external APIs) ------------------------
from awo.models.local_backend import LocalEcho
from awo.models.alt_backend import LocalUpper

BACKENDS = {"echo": LocalEcho(), "upper": LocalUpper()}
EXIT_PENDING = 78

# ---- utilities ---------------------------------------------------------------
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
    """Create a new run folder and record pointers *up front*."""
    runs_root = Path("runs")
    runs_root.mkdir(parents=True, exist_ok=True)
    run_id = f"run_{now_iso()}"
    rd = runs_root / run_id
    (rd / "steps").mkdir(parents=True, exist_ok=True)
    (rd / "artifacts").mkdir(parents=True, exist_ok=True)
    # Pointers that make CI robust:
    write_text(runs_root / "LAST_RUN", run_id)
    write_text(rd / "RUN_ID", run_id)
    return rd

def init_report(run_dir: Path, workflow_path: str) -> List[str]:
    return [
        f"# AWO Run Report — {run_dir.name}", "",
        f"- Workflow: {workflow_path}",
        f"- Started: {now_iso()}",
        ""
    ]

def record_step(run_dir: Path, idx: int, step_id: str, payload: Dict[str, Any]) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{step_id}.json", payload)

def finalize_report(run_dir: Path, report_lines: List[str]) -> None:
    write_text(run_dir / "report.md", "\n".join(report_lines))

# ---- main logic --------------------------------------------------------------
def run(workflow_path: str) -> int:
    # Always create a run directory first so CI can find it.
    run_dir = ensure_run_dir()
    report = init_report(run_dir, workflow_path)
    step_idx = 0
    ctx: Dict[str, Any] = {}

    # Load workflow (with helpful errors recorded into the run)
    wf_file = Path(workflow_path)
    if not wf_file.exists():
        msg = f"Workflow file not found: {workflow_path}"
        record_step(run_dir, step_idx, "init_error",
                    {"error": "workflow_missing", "message": msg, "ts": now_iso()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    try:
        wf = json.loads(wf_file.read_text(encoding="utf-8"))
    except Exception as e:
        msg = f"Failed to parse workflow JSON: {e}"
        record_step(run_dir, step_idx, "init_error",
                    {"error": "json_parse", "message": str(e), "ts": now_iso()})
        report += ["## Error", "", msg, ""]
        finalize_report(run_dir, report)
        print(f"[AWO] {msg}", file=sys.stderr)
        return 2

    # Freeze workflow for provenance
    write_text(run_dir / "workflow_frozen.json", json.dumps(wf, indent=2))

    # Execute steps
    try:
        for step in wf.get("steps", []):
            step_idx += 1
            op = step.get("op")
            step_id = step.get("id", f"step_{step_idx}")
            rec: Dict[str, Any] = {"ts": now_iso(), "id": step_id, "op": op}

            if op == "fanout_generate":
                prompt = step["prompt"]
                models = step.get("models", ["echo", "upper"])
                params = step.get("params", {"seed": 0})

                outs: List[Dict[str, Any]] = []
                for m in models:
                    if m not in BACKENDS:
                        raise RuntimeError(f"Unknown model backend: {m}")
                    out = BACKENDS[m].generate(prompt, params=params)
                    outs.append({"model": m, "text": out["text"], "meta": out["meta"]})

                rec.update({"prompt": prompt, "models": models, "params": params, "outputs": outs})
                ctx[step_id] = outs
                record_step(run_dir, step_idx, step_id, rec)

                # keep the report readable; show a hash of the prompt and truncated outputs
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
                    report.append(f"- **{o['model']}** → {o['text'].replace(chr(10),' ')[:200]}")
                report.append("")

            elif op == "consensus_vote":
                src = step["inputs_from"]
                items = ctx.get(src, [])
                if not items:
                    raise RuntimeError(f"consensus_vote: no inputs from '{src}'")

                buckets: Dict[str, List[str]] = {}
                for o in items:
                    k = norm_text(o["text"])
                    buckets.setdefault(k, []).append(o["model"])

                ranked = sorted(buckets.items(),
                                key=lambda kv: (len(kv[1]), len(kv[0])),
                                reverse=True)
                if ranked:
                    consensus_norm, voters = ranked[0]
                    representative = next(o for o in items
                                          if norm_text(o["text"]) == consensus_norm)["text"]
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
                    "",
                    "```",
                    representative[:300],
                    "```",
                    "",
                ]

            elif op == "write_text":
                path = step["args"]["path"]
                text = step["args"]["text"]
                out_path = run_dir / "artifacts" / path
                write_text(out_path, text)
                rec.update({"wrote": str(out_path)})
                record_step(run_dir, step_idx, step_id, rec)
                report += [f"## {step_idx}. write_text — {step_id}",
                           f"- wrote: {out_path}", ""]

            elif op == "audit_gate":
                checklist = step.get("args", {}).get("checklist", "templates/audit-checklist.md")
                rec.update({"gate": {"status": "pending", "checklist": checklist, "ts": now_iso()}})
                record_step(run_dir, step_idx, step_id, rec)

                write_text(run_dir / "gate_decision.yml",
                           f"status: pending\nchecklist: {checklist}\ncreated_at: {now_iso()}\n")

                report += [
                    f"## {step_idx}. audit_gate — {step_id}",
                    f"- checklist: {checklist}",
                    "",
                    "> Run halted for human review.",
                    "",
                ]
                finalize_report(run_dir, report)
                print(f"[AWO] Run created at: {run_dir}")
                return EXIT_PENDING

            else:
                raise RuntimeError(f"Unknown op: {op}")

    except Exception as e:
        # Per-step error handling with visible artifact
        record_step(run_dir, step_idx, "step_error",
                    {"error": "step_failed", "message": str(e), "ts": now_iso()})
        report += ["## Error during execution", "", str(e), ""]
        finalize_report(run_dir, report)
        print(f"[AWO] ERROR: {e}", file=sys.stderr)
        return 1

    # Normal completion (no audit gate)
    finalize_report(run_dir, report)
    print(f"[AWO] Run created at: {run_dir}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)
    try:
        sys.exit(run(sys.argv[1]))
    except Exception as e:
        # Absolute last-resort safety: still leave a usable run folder.
        rd = ensure_run_dir()
        record_step(rd, 0, "unhandled_error",
                    {"error": "unhandled", "message": str(e), "ts": now_iso()})
        finalize_report(rd, [f"# AWO Run Report — {rd.name}", "",
                             "## Error", "", str(e), ""])
        print(f"[AWO] UNHANDLED ERROR: {e}", file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env python3
"""
AWO multi-model runner (stdlib only).

Executes a JSON workflow with the following ops:
  - fanout_generate: send the same prompt to multiple model backends
  - consensus_vote:  pick a consensus text (simple normalized majority)
  - write_text:      write an artifact file into the run
  - audit_gate:      stop and require human approval (exit code 78)

Outputs (immutable):
  runs/
    run_YYYY-MM-DDTHH-MM-SSZ/
      workflow_frozen.json
      steps/NN_<id>.json
      artifacts/<any files created>
      report.md
    LAST_RUN      <-- breadcrumb for CI to pick up the latest run

No external APIs (uses deterministic local backends).
"""

from __future__ import annotations
import json
import os
import re
import sys
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

# ---- deterministic local backends -------------------------------------------
# These should already exist in your repo per previous steps.
from awo.models.local_backend import LocalEcho
from awo.models.alt_backend import LocalUpper

BACKENDS = {
    "echo": LocalEcho(),   # echoes + small deterministic transform
    "upper": LocalUpper(), # uppercase + deterministic meta
}

EXIT_PENDING = 78  # signal for "needs human approval"

# ---- small utilities ---------------------------------------------------------
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

def sha12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def norm_text(s: str) -> str:
    """Very simple normalization for voting (case + whitespace collapse)."""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s

def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def ensure_run_dir() -> Path:
    run_id = f"run_{now_iso()}"
    run_dir = Path("runs") / run_id
    (run_dir / "steps").mkdir(parents=True, exist_ok=True)
    (run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
    return run_dir

def record_step(run_dir: Path, idx: int, step_id: str, payload: Dict[str, Any]) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{step_id}.json", payload)

def breadcrumb(run_dir: Path) -> None:
    """Write runs/LAST_RUN so CI can capture the ID reliably."""
    write_text(Path("runs") / "LAST_RUN", run_dir.name)

# ---- main runner -------------------------------------------------------------
def run(workflow_path: str) -> int:
    wf_path = Path(workflow_path)
    if not wf_path.exists():
        print(f"[AWO] Workflow file not found: {workflow_path}", file=sys.stderr)
        return 2

    wf = json.loads(wf_path.read_text(encoding="utf-8"))
    run_dir = ensure_run_dir()

    # Freeze the workflow that was executed
    write_text(run_dir / "workflow_frozen.json", json.dumps(wf, indent=2))
    breadcrumb(run_dir)  # breadcrumb early so CI can still find the folder if we halt at the gate

    ctx: Dict[str, Any] = {}
    report: List[str] = []
    report += [f"# AWO Run Report — {run_dir.name}", ""]
    report += [f"- Workflow: {workflow_path}", f"- Started: {now_iso()}", ""]

    step_index = 0
    for step in wf.get("steps", []):
        step_index += 1
        op = step.get("op")
        step_id = step.get("id", f"step_{step_index}")
        rec: Dict[str, Any] = {"ts": now_iso(), "id": step_id, "op": op}

        # ----- fanout_generate -------------------------------------------------
        if op == "fanout_generate":
            prompt = step["prompt"]
            models = step.get("models", ["echo", "upper"])
            params = step.get("params", {"seed": 0})

            outputs: List[Dict[str, Any]] = []
            for m in models:
                if m not in BACKENDS:
                    raise RuntimeError(f"Unknown model backend: {m}")
                out = BACKENDS[m].generate(prompt, params=params)
                outputs.append({"model": m, "text": out["text"], "meta": out["meta"]})

            rec.update({"prompt": prompt, "models": models, "params": params, "outputs": outputs})
            ctx[step_id] = outputs
            record_step(run_dir, step_index, step_id, rec)

            report += [
                f"## {step_index}. fanout_generate — {step_id}",
                "",
                f"Prompt (sha12={sha12(prompt)}):",
                "",
                "```",
                prompt,
                "```",
                "",
                "Outputs:",
            ]
            for o in outputs:
                preview = o["text"].replace("\n", " ")[:200]
                report.append(f"- **{o['model']}** → {preview}")

            report.append("")

        # ----- consensus_vote --------------------------------------------------
        elif op == "consensus_vote":
            src = step["inputs_from"]
            candidates = ctx.get(src, [])
            if not candidates:
                raise RuntimeError(f"consensus_vote: no inputs found from '{src}'")

            buckets: Dict[str, List[str]] = {}
            for o in candidates:
                k = norm_text(o["text"])
                buckets.setdefault(k, []).append(o["model"])

            # pick the normalized text with max supporters; break ties by length
            ranked = sorted(buckets.items(), key=lambda kv: (len(kv[1]), len(kv[0])), reverse=True)
            if ranked:
                consensus_norm, voters = ranked[0]
                representative = next(o for o in candidates if norm_text(o["text"]) == consensus_norm)["text"]
            else:
                consensus_norm, voters, representative = "", [], ""

            rec.update({
                "inputs_from": src,
                "total_candidates": len(candidates),
                "voter_count": len(voters),
                "voters": voters,
                "consensus_norm": consensus_norm,
                "consensus_text": representative,
                "agreement_ratio": (len(voters) / max(1, len(candidates))),
            })
            ctx[step_id] = rec
            record_step(run_dir, step_index, step_id, rec)

            report += [
                f"## {step_index}. consensus_vote — {step_id}",
                f"- inputs_from: {src}",
                f"- voters: {', '.join(voters) if voters else '(none)'}",
                f"- agreement_ratio: {rec['agreement_ratio']:.2f}",
                "",
                "**Consensus text (first 300 chars):**",
                "",
                "```",
                representative[:300],
                "```",
                "",
            ]

        # ----- write_text ------------------------------------------------------
        elif op == "write_text":
            path = step["args"]["path"]
            text = step["args"]["text"]
            out_path = run_dir / "artifacts" / path
            write_text(out_path, text)

            rec.update({"wrote": str(out_path)})
            record_step(run_dir, step_index, step_id, rec)

            report += [
                f"## {step_index}. write_text — {step_id}",
                f"- wrote: {out_path}",
                ""
            ]

        # ----- audit_gate ------------------------------------------------------
        elif op == "audit_gate":
            checklist = step.get("args", {}).get("checklist", "templates/audit-checklist.md")
            gate = {"status": "pending", "checklist": checklist, "ts": now_iso()}
            rec.update({"gate": gate})
            record_step(run_dir, step_index, step_id, rec)

            # a tiny YAML for humans to review/edit if desired
            write_text(
                run_dir / "gate_decision.yml",
                f"status: pending\nchecklist: {checklist}\ncreated_at: {now_iso()}\n",
            )

            report += [
                f"## {step_index}. audit_gate — {step_id}",
                f"- checklist: {checklist}",
                "",
                "> Run halted for human review.",
                ""
            ]

            # finalize report and return 78 to signal the CI gate
            write_text(run_dir / "report.md", "\n".join(report))
            breadcrumb(run_dir)  # ensure CI can read the run id
            print(f"[AWO] Run created at: {run_dir}")
            return EXIT_PENDING

        # ----- unknown op ------------------------------------------------------
        else:
            raise RuntimeError(f"Unknown op: {op}")

    # normal completion (no gate encountered)
    write_text(run_dir / "report.md", "\n".join(report))
    breadcrumb(run_dir)
    print(f"[AWO] Run created at: {run_dir}")
    return 0


# ---- CLI ---------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)
    try:
        sys.exit(run(sys.argv[1]))
    except Exception as e:
        # Fail loudly with a clear message (useful in Actions logs)
        print(f"[AWO] ERROR: {e}", file=sys.stderr)
        sys.exit(1)

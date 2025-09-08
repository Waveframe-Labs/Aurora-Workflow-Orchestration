#!/usr/bin/env python3
"""
Minimal AWO runner (no secrets, no model calls).
- Reads a simple workflow JSON (steps with 'name' and 'prompt' strings).
- Creates runs/<timestamp>/ with immutable logs.
- Writes a gate_decision.yml with status: pending (human approval needed).
- Exits 78 to signal "pending gate" to GitHub Actions, which keeps artifacts.
"""

import json, os, sys, hashlib, time, textwrap
from datetime import datetime, timezone
from pathlib import Path

EXIT_PENDING = 78  # conventional “needs human” exit

def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)

    wf_path = Path(sys.argv[1])
    if not wf_path.exists():
        print(f"Workflow file not found: {wf_path}", file=sys.stderr)
        sys.exit(2)

    # Load workflow
    with wf_path.open("r", encoding="utf-8") as f:
        wf = json.load(f)

    # Prepare run dir
    run_id = f"run_{now_iso()}"
    run_dir = Path("runs") / run_id
    (run_dir / "steps").mkdir(parents=True, exist_ok=True)

    # Save a frozen copy of the workflow used
    with (run_dir / "workflow_frozen.json").open("w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)

    # Minimal “execution”: echo back prompts deterministically (no external calls)
    steps = wf.get("steps", [])
    records = []
    for i, step in enumerate(steps, start=1):
        name = step.get("name", f"step_{i}")
        prompt = step.get("prompt", "")
        # deterministic “response”: reverse + hash tail
        echoed = prompt[::-1]
        digest = sha256(prompt)
        response = f"[SIMULATED-RESPONSE] {echoed}\n\n(hash:{digest})"

        rec = {
            "index": i,
            "name": name,
            "prompt": prompt,
            "response": response,
            "meta": {
                "engine": "simulator:v0",
                "seed": 0,
                "timestamp": now_iso(),
                "prompt_hash": sha256(prompt),
            },
        }
        records.append(rec)

        # write per-step record
        with (run_dir / "steps" / f"{i:02d}_{name}.json").open("w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2, ensure_ascii=False)

    # Write a compact summary
    summary = {
        "run_id": run_id,
        "started_at": now_iso(),
        "workflow_source": str(wf_path),
        "num_steps": len(records),
        "artifacts": [f"steps/{i:02d}_{r['name']}.json" for i, r in enumerate(records, start=1)]
    }
    with (run_dir / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # Produce a Markdown report skeleton
    md = [f"# AWO Run Report — {run_id}\n"]
    md.append("This is a runnable, audit-ready stub without external model calls.\n")
    md.append("## Steps\n")
    for rec in records:
        md.append(f"### {rec['index']}. {rec['name']}\n")
        md.append("**Prompt**\n")
        md.append("```text\n" + rec["prompt"] + "\n```\n")
        md.append("**Response (simulated)**\n")
        md.append("```text\n" + rec["response"] + "\n```\n")

    md.append("## Gate\n")
    md.append("Status: **PENDING** — requires human review.\n")
    md.append("Edit `gate_decision.yml` to approve/reject, then re-run the Report workflow.\n")

    with (run_dir / "report.md").open("w", encoding="utf-8") as f:
        f.write("\n".join(md))

    # Create a pending human gate
    gate = textwrap.dedent("""\
        status: pending
        reason: "Initial run: awaiting human approval."
        reviewer: null
        reviewed_at: null
        """)
    with (run_dir / "gate_decision.yml").open("w", encoding="utf-8") as f:
        f.write(gate)

    print(f"Run created at: {run_dir}")
    # Exit 78 so the workflow can surface “needs human”
    sys.exit(EXIT_PENDING)

if __name__ == "__main__":
    main()

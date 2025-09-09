#!/usr/bin/env python3
"""
AWO multi-model runner (stdlib only, phone-friendly).

Ops supported (from the workflow JSON):
  - fanout_generate : send the same prompt to multiple models
  - consensus_vote  : pick a consensus (simple normalized majority)
  - write_text      : write an artifact file into the run
  - audit_gate      : stop for human approval (exit code 78)

Contract with GitHub Actions:
  - Always creates a new folder runs/run_YYYY-MM-DDTHH-MM-SSZ/
  - Writes step logs to runs/<id>/steps/*.json
  - Writes a human report to runs/<id>/report.md
  - Exits 0 on normal completion
  - Exits 78 to signal “pending human review”
"""

import json, os, sys, hashlib, re, textwrap
from datetime import datetime, timezone
from pathlib import Path

# ---- backends (deterministic local simulators) -------------------------------
# These should already exist in your repo from earlier steps.
from awo.models.local_backend import LocalEcho
from awo.models.alt_backend   import LocalUpper

BACKENDS = {
    "echo":  LocalEcho(),
    "upper": LocalUpper(),
}

EXIT_PENDING = 78  # signal to the workflow that a manual gate is required


# ----------------------------- helpers ----------------------------------------
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

def sha12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def norm_text(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")

def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def ensure_run_dir() -> Path:
    run_id  = f"run_{now_iso()}"
    run_dir = Path("runs") / run_id
    (run_dir / "steps").mkdir(parents=True, exist_ok=True)
    (run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
    return run_dir

def step_record(run_dir: Path, idx: int, name: str, payload: dict) -> None:
    write_json(run_dir / "steps" / f"{idx:02d}_{name}.json", payload)


# ------------------------------- runner ---------------------------------------
def run(workflow_path: str) -> int:
    wf_path = Path(workflow_path)
    if not wf_path.exists():
        print(f"Workflow file not found: {workflow_path}", file=sys.stderr)
        return 2

    wf = json.loads(wf_path.read_text(encoding="utf-8"))
    run_dir = ensure_run_dir()

    # Freeze inputs for reproducibility
    freeze = {
        "workflow_file": str(wf_path),
        "workflow_hash": sha12(wf_path.read_text(encoding="utf-8")),
        "started_at":    now_iso(),
        "env": {
            "GITHUB_SHA": os.getenv("GITHUB_SHA", ""),
            "GITHUB_REF": os.getenv("GITHUB_REF", ""),
        },
    }
    write_json(run_dir / "workflow_frozen.json", wf)
    write_json(run_dir / "run.json", freeze)

    ctx = {}  # scratch to pass data between steps
    idx = 0
    report = [f"# AWO Run Report — {run_dir.name}", "", f"- Workflow: `{workflow_path}`", f"- Started: {freeze['started_at']}", ""]

    for step in wf.get("steps", []):
        idx += 1
        op   = step.get("op")
        name = step.get("id", f"step_{idx}")
        rec  = {"ts": now_iso(), "id": name, "op": op}

        if op == "fanout_generate":
            prompt = step["prompt"]
            models = step.get("models", ["echo", "upper"])
            params = step.get("params", {"seed": 0})
            outputs = []
            for m in models:
                if m not in BACKENDS:
                    raise RuntimeError(f"Unknown model backend: {m}")
                out = BACKENDS[m].generate(prompt, params=params)
                outputs.append({"model": m, "text": out["text"], "meta": out["meta"]})
            rec.update({"prompt": prompt, "models": models, "outputs": outputs})
            ctx[name] = outputs
            step_record(run_dir, idx, name, rec)

            report += [f"## {idx}. fanout_generate — {name}", "", f"Prompt: `{prompt}`", "Outputs:"]
            for o in outputs:
                report.append(f"- **{o['model']}** → {o['text'][:160]}")
            report.append("")

        elif op == "consensus_vote":
            src = step["inputs_from"]
            items = ctx.get(src, [])
            bucket = {}
            for o in items:
                k = norm_text(o["text"])
                bucket.setdefault(k, []).append(o["model"])
            winners = sorted(bucket.items(), key=lambda kv: (len(kv[1]), len(kv[0])), reverse=True)
            if winners:
                consensus_norm, voters = winners[0]
                representative = next(o for o in items if norm_text(o["text"]) == consensus_norm)["text"]
            else:
                consensus_norm, voters, representative = "", [], ""

            rec.update({
                "inputs_from": src,
                "voters": voters,
                "consensus_text": representative,
                "consensus_norm": consensus_norm,
                "voter_count": len(voters),
                "total_candidates": len(items),
                "agreement_ratio": (len(voters) / max(1, len(items))),
            })
            ctx[name] = rec
            step_record(run_dir, idx, name, rec)

            report += [
                f"## {idx}. consensus_vote — {name}",
                f"- inputs_from: {src}",
                f"- voters: {', '.join(voters) if voters else '(none)'}",
                f"- agreement_ratio: {rec['agreement_ratio']:.2f}",
                "",
                f"**Consensus:** {representative[:300]}",
                "",
            ]

        elif op == "write_text":
            path = step["args"]["path"]
            text = step["args"]["text"]
            out_path = run_dir / "artifacts" / path
            write_text(out_path, text)
            rec.update({"wrote": str(out_path)})
            step_record(run_dir, idx, name, rec)

            report += [f"## {idx}. write_text — {name}", f"- wrote: `{out_path}`", ""]

        elif op == "audit_gate":
            checklist = step.get("args", {}).get("checklist", "templates/audit-checklist.md")
            gate_yaml = textwrap.dedent(f"""\
                status: pending
                checklist: {checklist}
                created_at: {now_iso()}
            """)
            write_text(run_dir / "gate_decision.yml", gate_yaml)
            rec.update({"gate": {"status": "pending", "checklist": checklist}})
            step_record(run_dir, idx, name, rec)

            report += [
                f"## {idx}. audit_gate — {name}",
                f"- checklist: {checklist}",
                "",
                "> Run halted for human review.",
                "",
            ]

            # finalize report and signal the gate
            write_text(run_dir / "report.md", "\n".join(report))
            print(f"Run created at: {run_dir}")
            return EXIT_PENDING

        else:
            raise RuntimeError(f"Unknown op: {op}")

    # normal completion (no audit gate triggered)
    write_text(run_dir / "report.md", "\n".join(report))
    print(f"Run created at: {run_dir}")
    return 0


# ------------------------------ CLI entry -------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/awo_run.py <workflow.json>", file=sys.stderr)
        sys.exit(2)
    sys.exit(run(sys.argv[1]))

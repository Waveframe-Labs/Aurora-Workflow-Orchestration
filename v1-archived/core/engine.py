import os, json, time, pathlib
from .lockfile import snapshot

def _write_jsonl(path, rec):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def _read_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))

def run(workflow_path: str, backend):
    wf = _read_json(workflow_path)
    run_id = time.strftime("%Y-%m-%dT%H-%M-%SZ")
    run_dir = pathlib.Path("runs") / run_id
    (run_dir / "steps").mkdir(parents=True, exist_ok=True)
    snapshot(run_dir, workflow_path, wf)

    outputs = []
    for i, step in enumerate(wf.get("steps", [])):
        sid = step.get("id", f"step_{i:03d}")
        op  = step.get("op")
        rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ"), "id": sid, "op": op}

        if op == "llm_map":
            prompt = step["prompt"]
            params = step.get("params", {})
            out = backend.generate(prompt, params=params)
            rec.update({"prompt": prompt, "output": out})
            outputs.append(out["text"])

        elif op == "write_text":
            path = step["args"]["path"]
            text = step["args"]["text"]
            out_path = run_dir / "artifacts" / path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(text, encoding="utf-8")
            rec.update({"wrote": str(out_path)})

        elif op == "audit_gate":
            # mark pending gate & exit with a special non-zero code
            gate_id = step.get("id", "gate")
            gate_info = {
                "run_id": run_id,
                "gate_id": gate_id,
                "status": "pending",
                "checklist": step.get("args", {}).get("checklist", "")
            }
            (run_dir / "gate_pending.json").write_text(json.dumps(gate_info, indent=2), encoding="utf-8")
            _write_jsonl(run_dir / "steps" / f"{i:03d}_{sid}.jsonl", {**rec, "gate": gate_info})
            _write_report(run_dir, workflow_path, backend.name, outputs, pending_gate=gate_info)
            os._exit(78)  # signals 'needs human review'

        _write_jsonl(run_dir / "steps" / f"{i:03d}_{sid}.jsonl", rec)

    _write_report(run_dir, workflow_path, backend.name, outputs, pending_gate=None)
    return str(run_dir)

def _write_report(run_dir, workflow_path, backend_name, outputs, pending_gate):
    report = [
        f"# Run Report — {run_dir.name}",
        "",
        f"- Workflow: {workflow_path}",
        f"- Backend: {backend_name}",
        f"- Steps executed: {len(list((run_dir/'steps').glob('*.jsonl')))}",
    ]
    if pending_gate:
        report += [
            "",
            "## Audit Gate (Pending)",
            f"- Gate ID: {pending_gate['gate_id']}",
            f"- Checklist: {pending_gate.get('checklist','')}",
            "",
            "This run intentionally stopped for human review."
        ]
    if outputs:
        report += ["", "## Sample Outputs", *[f"- {t[:200]}" for t in outputs[:3]]]
    (run_dir / "report.md").write_text("\n".join(report), encoding="utf-8")

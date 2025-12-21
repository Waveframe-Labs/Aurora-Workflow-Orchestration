import hashlib, json, pathlib, time

def _sha256_text(s: str) -> str:
    return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()

def snapshot(run_dir: pathlib.Path, workflow_path: str, wf_dict: dict):
    run_dir.mkdir(parents=True, exist_ok=True)
    # snapshot workflow json
    wf_text = pathlib.Path(workflow_path).read_text(encoding="utf-8")
    (run_dir / "workflow.snapshot.json").write_text(wf_text, encoding="utf-8")
    # minimal lock snapshot (hash prompts only for now)
    prompts = {}
    for step in wf_dict.get("steps", []):
        if "prompt" in step:
            pid = step.get("id", "prompt")
            prompts[pid] = _sha256_text(step["prompt"])
    lock = {
        "frozen_at": time.strftime("%Y-%m-%dT%H-%M-%SZ"),
        "prompts": prompts
    }
    (run_dir / "lock.snapshot.json").write_text(json.dumps(lock, indent=2), encoding="utf-8")

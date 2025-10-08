---
filetype: core_module
version: 1.0.1
updated: 2025-10-08
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Core — Execution Layer

**Purpose**  
Implements the minimal runtime for Aurora Workflow Orchestration (AWO).  
`engine.py` executes a JSON workflow, emits an auditable run folder, and halts at audit gates.  
`lockfile.py` snapshots the workflow and writes a prompt-hash lock for integrity.

---

## Modules

### `engine.py`
Entry points and helpers:
- `run(workflow_path: str, backend) -> str`  
  Executes steps from a JSON workflow file and returns the run directory path.
- `_write_report(...)` — renders a `report.md` summary.
- `_write_jsonl(path, rec)` / `_read_json(path)` — append/read utilities.

**Supported operations (`op`):**
- `llm_map`  
  - Inputs: `prompt` (str), optional `params` (dict)  
  - Behavior: calls `backend.generate(prompt, params=...)` and records `output`; captures `.text` in an outputs list.
- `write_text`  
  - Inputs: `args.path` (str), `args.text` (str)  
  - Behavior: writes to `runs/<id>/artifacts/<path>`.
- `audit_gate`  
  - Inputs: `args.checklist` (optional str)  
  - Behavior: writes `gate_pending.json`, logs the gate event, finalizes a partial report, and exits with code **78** to require human approval.

**Run outputs (under `runs/<timestamp>/`):**
- `steps/` — per-step JSONL logs (timestamp, id, op, details)
- `artifacts/` — files written by `write_text`
- `report.md` — human-readable summary (backend, step count, sample outputs, pending gate info)
- From `lockfile.snapshot(...)`:
  - `workflow.snapshot.json` — verbatim copy of the workflow JSON
  - `lock.snapshot.json` — prompt hash lock (`sha256:<hash>`) with `frozen_at` timestamp
- For pending gates: `gate_pending.json`

**Exit codes:**
- `0` — normal completion
- `78` — run intentionally paused for human review (audit gate)

**Backend interface (expected):**
- Method: `backend.generate(prompt: str, params: dict) -> dict` with `["text"]`
- Attribute: `backend.name` (string for reporting)

### `lockfile.py`
- `snapshot(run_dir: Path, workflow_path: str, wf_dict: dict)`  
  Creates immutable snapshots:
  - `workflow.snapshot.json` — exact workflow content
  - `lock.snapshot.json` — hashes of all `prompt` fields by step id, plus `frozen_at`

---

## Minimal Workflow Schema (JSON)

```json
{
  "steps": [
    { "id": "s1", "op": "llm_map", "prompt": "Summarize: The battery lasts all day", "params": {"temperature": 0.3} },
    { "id": "note", "op": "write_text", "args": { "path": "notes/summary.txt", "text": "Draft note" } },
    { "id": "gate_review", "op": "audit_gate", "args": { "checklist": "templates/audit-checklist.md" } }
  ]
}
```

## Usage (Python)

from core.engine import run

class DummyBackend:
    name = "dummy"
    def generate(self, prompt, params=None):
        return {"text": f"[echo] {prompt}"}

run_dir = run("workflows/minimal.json", backend=DummyBackend())
print("Run created:", run_dir)

This will create runs/<timestamp>/ with steps/, artifacts/, report.md, and lock snapshots.
If the workflow includes audit_gate, the process exits with code 78 after writing gate_pending.json.

## Relation to AWO / CRI  
	•	AWO defines the method (claims, audits, gates).  
	•	This core executes it: step logging, artifacts, report, and gate pause.  
	•	CRI-CORE can call engine.run(...) inside CI to produce standardized evidence packages.  

⸻

## Maintenance Policy  
	•	Changes that alter outputs or lock format must be noted in CHANGELOG.md.  
	•	Do not remove or rename snapshot files; downstream audits depend on them.  
	•	Any new op types should be documented here and covered by schema/tests.  

⸻

## Contact

Waveframe Labs
swright@waveframelabs.org

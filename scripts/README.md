---
filetype: tooling
version: 1.0.1
updated: 2025-10
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---
# Scripts — Orchestration & Validation

**Purpose**  
Command-line helpers that execute workflows and validate outputs.

**Typical scripts**
- `awo_run.py` — executes a workflow JSON, writes `runs/<id>/`, halts at audit gates.
- `validate_run.py` — checks `run_manifest.json`, `provenance.json`, and related files against schemas.
- Utilities for hashing, environment capture, and reporting.

**Conventions**
- Python 3.11+ recommended.
- Minimal external deps; pin versions in `requirements.txt`.
- Fail fast on schema errors; exit **78** to pause for human review.

**Contact**  
Waveframe Labs — swright@waveframelabs.org

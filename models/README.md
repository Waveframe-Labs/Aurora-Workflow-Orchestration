---
filetype: model_backends
version: 1.1.0
updated: 2025-10-08
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Model Backends — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory defines lightweight, deterministic backend classes used to simulate model behavior in AWO workflows.  
They serve as reproducible stand-ins for real LLM or inference APIs, ensuring the orchestration engine (`/core/engine.py`) can be validated offline.

---

## Contents

| File | Description |
|------|--------------|
| **base.py** | Defines the abstract interface class `ModelBackend`. Establishes a consistent method signature for all backends via `generate(prompt, params)` and a `name` identifier. |
| **local_backend.py** | Implements `LocalEcho`, a deterministic echo-style backend. Returns the input prompt prefixed with `[ECHO]`, using a hash of the prompt and seed to ensure stable reproducibility. |
| **alt_backend.py** | Implements `LocalUpper`, a secondary deterministic backend that uppercases the prompt and appends a stable hash tail to emulate an alternate model output. Useful for fan-out and consensus testing. |

---

## Interface Contract
Every backend must subclass `ModelBackend` and implement:

```
python
def generate(self, prompt: str, *, params: dict) -> dict:
    """Return structured output: {"text": <str>, "usage": {}, "meta": {...}}"""
```

•	text — main model output (string)  
•	usage — placeholder for token or cost tracking (optional)  
•	meta — must include backend name and parameter context  

The interface ensures all backends can be swapped seamlessly inside the AWO orchestration engine.

---

## Reproducibility

These backends are deterministic:  
	•	They use prompt-specific SHA-256 hashes and a seed value to reproduce identical results across runs.  
	•	This allows validation of orchestration logic (run manifests, gate checkpoints, logging schema) without stochastic model behavior.

---

## Integration  
   •	Used directly by /core/engine.py during workflow execution (backend.generate(...)).  
   •	Provide reproducibility baselines for AWO’s audit-gate and consensus validation steps.  
   •	Serve as local fallbacks when real AI backends are unavailable.  

---

## Contact  

Waveframe Labs
swright@waveframelabs.org

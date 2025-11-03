# ADR-0018 — Model Drift & Fingerprinting
**Status:** Accepted  
**Date:** 2025-11-02  
**Applies to:** AWO v1.2.1+ (all runs)  
**Owner:** Orchestrator; enforced by Auditor / CRI-CORE (future)

## Context
AI models mutate over time (vendor updates, hidden training deltas, routing changes). Freezing config is not enough; we must freeze **behavior** and **inputs** and detect drift deterministically.

## Decision
1) **Model Fingerprint (MF)** is **MUST** for every run:
   - Captured to `/runs/<RUN_ID>/workflow_frozen.json#model_fingerprint` at execution start.
   - Same object echoed in `/runs/<RUN_ID>/approval.json#model_fingerprint`.

2) **Prompt/Context Hashing** is **MUST**:
   - Hash the full serialized inference request (system+tools+user+files) → `prompt_serialization_hash`.

3) **Behavior Canaries (Goldens)** are **SHOULD**:
   - Maintain a private, fixed eval set; store scores and deltas in `/logs/audits/<date>_drift_report.json`.

4) **Drift Policy** is **MUST**:
   - A run **fails attestation** if `drift_decision == "fail"` in the associated drift report (when present).

5) **Cross-echo**:
   - `model_fingerprint` and `drift_report` entries are referenced in `SHA256SUMS.txt`.

## Details
- **Minimal MF fields (normative)**  
  `provider, model_id, endpoint, engine_build, created_at, context_window, temperature, top_p, max_output_tokens, seed, stop_tokens[], system_prompt_hash, tool_schema_hash, prompt_serialization_hash, sdk_name, sdk_version, runtime_env (python,node), hardware_hint, privacy_mode`
- **Optional MF fields (advisory)**  
  `top_k, frequency_penalty, presence_penalty, tool_plugins[], cost_estimate, latency_ms`

- **Drift report (normative)** must include:  
  `baseline_id, eval_suite_id, item_count, metrics{}, deltas{}, logits_divergence (if available), decision (pass|fail), created_at`

- **Redaction**: when inputs/outputs are sensitive, store **hashes + policy pointers** only (see `redaction_pointer.schema.json`).

## Consequences
- Deterministic reconstruction of requests is possible.
- Attestation gates can block merges/releases on detectable drift.

## Compliance
- **MUST** include `model_fingerprint` in `workflow_frozen.json` and `approval.json`.
- **MUST** include `prompt_serialization_hash`.
- **SHOULD** produce a `drift_report.json` for repos declaring “Standard” or “Full” compliance.

## Security & Privacy
- Never store secrets or raw sensitive payloads—store **hashes** and **redaction pointers**.
- MF can include a `privacy_mode` flag to indicate routing through private endpoints.

## Backwards Compatibility
- Missing MF in legacy runs sets compliance to **Conditional**; future runs must comply.

## References
- AWO §1.6 Neurotransparency; §6 Artifacts; §9 Attestation.

## Changelog
- 2025-11-02: Initial acceptance.

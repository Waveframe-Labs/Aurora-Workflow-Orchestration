# ADR-0018 — Model Drift & Fingerprinting  
**Status:** Accepted (Revised v1.1 — 2025-11-03)  
**Supersedes:** ADR-0018 (v1.0)  
**Applies to:** AWO v1.2.1+ (all runs)  
**Owner:** Orchestrator; enforced by Auditor / CRI-CORE (future)

---

## Context
AI model behavior can change without notice. Configuration freezing alone doesn’t guarantee reproducibility when model weights, routing, or SDK logic drift.  
We require a formal fingerprint and behavioral reference to detect those changes deterministically and proportionally.

---

## Decision

### 1. Model Fingerprinting (unchanged)
Each run **MUST** record a `model_fingerprint` object in `/runs/<RUN_ID>/workflow_frozen.json` and echo it in `/runs/<RUN_ID>/approval.json`.

### 2. Prompt Serialization Hash (unchanged)
Each inference request **MUST** produce a SHA-256 hash of the full serialized context (`system + tools + user`), stored as `prompt_serialization_hash`.

### 3. Tiered Behavioral Canaries (new)
AWO adopts a **three-tier “Goldens” model** for behavioral stability testing.

| Tier | Description | Typical Count | Trigger | Purpose |
|------|--------------|---------------|----------|----------|
| 🟢 Tier 1 | Smoke tests (basic CI) | ~5 | Every push | Rapid regression signal |
| 🟡 Tier 2 | Drift suite | ~20 | Daily or on model update | Detect subtle semantic drift |
| 🔴 Tier 3 | Edge coverage / regression guard | 30–50 + | Major releases or tagged runs | Full behavioral assurance |

- Each golden test is a prompt–response pair stored under `/goldens/<tier>/`.  
- Evaluation output is written to `/logs/audits/<date>_tierX_report.json`.  
- Failure thresholds are defined in `/docs/drift_policy.yml` (or JSON equivalent).

**Attestation Rule:**  
If the active tier’s drift report yields `decision: fail`, attestation **MUST** be blocked until an updated baseline is accepted via a new ADR.

### 4. Drift Report (clarified)
`/logs/audits/<date>_drift_report.json` conforms to `schemas/drift_report.schema.json`.  
The `decision` field (pass | fail) governs attestation gating.

### 5. Cross-Echo & Checksum (unchanged)
`model_fingerprint` and `drift_report` entries **MUST** be referenced in `SHA256SUMS.txt`.

---

## Rationale
Tiering keeps evaluation proportional to intent:
- 🟢 CI speed for routine commits.  
- 🟡 Daily guardrails for ambient drift.  
- 🔴 Deep verification for archival releases.

This turns behavioral monitoring into a continuous signal rather than a one-time ritual, aligning AWO’s falsifiability principle with ongoing model mutability.

---

## Compliance Summary
| Requirement | Level |
|--------------|-------|
| Fingerprint + prompt hash recorded | **MUST** |
| At least Tier 1 goldens maintained | **MUST** |
| Tier 2 suite executed weekly or on model change | **SHOULD** |
| Tier 3 suite executed pre-release | **MUST** |
| Drift decision integrated into attestation gate | **MUST** |

---

## Security & Privacy
Goldens may contain sensitive prompts. If so, store only **hashes + redaction pointers** per `redaction_pointer.schema.json`.  
Raw content may live in private mirrors with matching proof hashes.

---

## Backwards Compatibility
Older runs without goldens remain valid but are **Compliance = Conditional**.  
Future AWO releases expect at least Tier 1 tests.

---

## References
- AWO §1.6 Neurotransparency  
- AWO §6 Artifacts  
- AWO §9 Attestation  
- Schemas: `model_fingerprint.schema.json`, `drift_report.schema.json`, `redaction_pointer.schema.json`

---

## Changelog
- **2025-11-03:** Added tiered behavioral canaries, clarified attestation gating.  
- **2025-11-02:** Initial acceptance (v1.0).

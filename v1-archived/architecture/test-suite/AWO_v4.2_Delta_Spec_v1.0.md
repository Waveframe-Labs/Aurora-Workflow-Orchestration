# AWO v4.2 — Delta Specification (v1.0.0)

**Diff Base:** v4.1  
**Target Version:** v4.2  
**Taxonomy Version:** 1.1  
**Effective Scope:** Governance, Integrity, Attestation, Determinism, Provenance

---

## 0. Rationale Summary

AWO v4.2 introduces the enforcement layer required to transform AWO from a primarily procedural workflow into a verifiable scientific-governance engine.

Primary goals:

- Enforce self-approval prohibitions.
- Guarantee deterministic artifact structure.
- Add machine-verifiable integrity checks.
- Introduce formal attestation binding.
- Prepare the system for the v4.2 test suite (S1–S3).

This document describes **only the changes** from v4.1 → v4.2. All unspecified behavior is inherited from v4.1.

---

## 1. Python Layer Deltas

### 1.1 Integrity Verifier

**+ Added:** `scripts/awo_integrity.py verify --run-id <RUN_ID>`

Required behavior:

- Validate file-set equality between:
  - recorded `SHA256SUMS.txt`, and
  - files present under `runs/<RUN_ID>/`.
- Validate per-file SHA256 hashes.
- Emit taxonomy codes on failure:
  - `INT-001` — hash mismatch
  - `INT-002` — file-set mismatch
- Exit non-zero on any failure.

**! Enforcement:**  
Integrity verification MUST be executed successfully before final commit or signing.

---

### 1.2 Canonical JSON Writer

**+ Added helper function:**

```python
def dump_json_canonical(path, data):
    import json
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(
            data,
            fp,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
```
Required usage:

This helper MUST be used for:
- runs/<RUN_ID>/approval.json
- governance independence logs
- runs/<RUN_ID>/run_manifest.json
- provenance/index.json
- other governance JSON artifacts

Goal: ensure deterministic JSON encoding for all governance-critical structures.

⸻

### 1.3 Timestamp Isolation

± Modified behavior:
- All non-essential timestamps MUST be moved into:
```
runs/<RUN_ID>/timestamps/
```

- Timestamp files and directories MUST be excluded from:
- deterministic SHA256SUMS calculation
- canonical tarball content used for attestation

**! Enforcement:**  
Timestamps MUST NOT participate in hash-based identity for a run.

⸻

### 1.4 Attestation Binding Script

- Added: scripts/awo_attest.py bind --run-id <RUN_ID>

Required behavior:
- Bind:
- reviewer identity (or hash)
- SHA256 root for runs/<RUN_ID>
- signature metadata (time, actor, workflow run)
- Write attestation payload into:
```
governance/attestations/<RUN_ID>/ATTESTATION.txt
```

- Use canonical, deterministic structure for the attestation file.

Location rule:

All attestations for a given run MUST live under:
```
governance/attestations/<RUN_ID>/
```

⸻

### 1.5 Gate2 Expansion (Governance Enforcement)

**! Enforcement change:**

Gate2 validation logic (in scripts/awo_validate.py gate2) MUST:
- Enforce self-approval rule:
```
if orchestrator == reviewer and allow_self_approval != "1":
    exit with code GOV-001
```

- Validate:
- independence log presence and structure
- identity checks for orchestrator vs reviewer
- correct handling of explicit overrides (allow_self_approval="1")

On violation, Gate2 MUST:
- Emit taxonomy code GOV-001.
- Exit non-zero.

⸻

### 1.6 Taxonomy Expansion

± Modified taxonomy version: 1.0 → 1.1

+ Added codes:
	•	INT-002 — file-set mismatch
	•	ATT-002 — hash binding failure

Existing codes (for reference):
	•	GOV-001 — self-approval violation
	•	GOV-002 — invariant failure
	•	INT-001 — hash mismatch
	•	ATT-001 — role mismatch
	•	REP-001 — replay detected
	•	STR-001 — orphan run

All codes MUST appear in error logs and governance reports where applicable.

⸻

## 2. Workflow YAML Deltas (GitHub Actions)

These changes apply to the AWO Run v4.2 workflow file.

### 2.1 Integrity Check in finalize

+ Added step in finalize job, after SHA256SUMS generation:

python scripts/awo_integrity.py verify --run-id "${RUN_ID}"

**! Blocking rule:**  
- All subsequent steps in finalize (attestation, signing, commit) MUST only execute if this step succeeds.

⸻

### 2.2 cosign Gated on Integrity

**! Enforcement:**  
- cosign signing steps (tarball and attestation) MUST only run if:
- awo_integrity.py verify completed successfully, and
- awo_validate.py chain (see §2.3) succeeded.

If integrity verification fails, cosign MUST NOT be invoked.

⸻

### 2.3 Chain Validator

+ Added:

A final governance chain validator call in finalize:
```
python scripts/awo_validate.py chain --run-id "${RUN_ID}"
```
Required checks:
- Integrity verification completed (no INT-* failures).
- Gate2 passed (no GOV-* violations).
- approval.json exists and is canonical.
- Attestation files exist under governance/attestations/<RUN_ID>/.
- Independence logs exist under governance logs.
- provenance/index.json updated for <RUN_ID>.

Failure in any of the above MUST:
- Exit non-zero.
- Block commit.
- Emit corresponding taxonomy code (GOV-002, ATT-*, INT-*, STR-*).

⸻

### 2.4 Provenance Index Update

+ Added step in finalize before commit:
```
python scripts/awo_provenance.py update-index --run-id "${RUN_ID}"
```
Required behavior:
- Append or merge run-level metadata for <RUN_ID> into:
```
provenance/index.json
```

- Use dump_json_canonical for deterministic ordering.

The index MUST contain at minimum:
- run_id
- commit
- workflow_run_url
- approved_by
- attestation_path

⸻

### 2.5 Attestation Directory Convention

± Modified behavior:
	•	All attestation artifacts for a run MUST live under:
```
governance/attestations/<RUN_ID>/
```

- Workflow steps MUST reference this path when:
- writing attestation files,
- signing with cosign,
- uploading artifacts.

Any prior ad-hoc locations for attestations are deprecated for v4.2 and MUST NOT be used going forward.

⸻

### 2.6 Timestamp Handling Before Hashing

**! Enforcement:**

Before generating runs/<RUN_ID>/SHA256SUMS.txt, timestamps MUST be relocated out of the deterministic region.

Example pattern:
```
mkdir -p "runs/${RUN_ID}/timestamps"
# Move any timestamp or transient time-based files out of the hash scope
# (exact file names are implementation-specific)
```  
Timestamps MUST NOT appear in the SHA256 inventory used for identity binding.

⸻

## 3. Repository Structure Deltas

### 3.1 Provenance Directory

+ Added:

A new top-level directory:
```
provenance/
  index.json
```
Used by:
- awo_provenance.py update-index
- governance test suite scenarios S1–S3
- external auditors for run discovery.

provenance/index.json MUST be canonical JSON (sorted keys, stable structure).

⸻

## 4. Deprecations

For AWO v4.2:  
- Deprecated: non-deterministic JSON outputs for governance artifacts.
- Deprecated: ad-hoc attestation file locations outside:
```
governance/attestations/<RUN_ID>/
```

- Deprecated: any finalize flow that does not invoke:
- awo_integrity.py verify
- awo_validate.py chain
- awo_provenance.py update-index

These behaviors MUST NOT be used in new runs, but older runs may retain legacy structure in archival form.

⸻

## 5. Backward Compatibility
- Backward Compatible: NO
- Migration Required: YES (for v4.1 → v4.2)

Reasons:
- Integrity and determinism rules will break previous SHA expectations.
- v4.1 runs lack required provenance index and canonical attestation layout.
- Governance enforcement (Gate2) is stricter and may reclassify previously “passing” behavior as non-conformant.

Existing v4.1 runs remain valid as historical artifacts but are not considered v4.2-compliant.

⸻

## 6. Signed-Off  
```
	•	Author: Shawn C. Wright
	•	Institution: Waveframe Labs / Aurora Research Initiative
	•	Version: 1.0.0
	•	Signed At (UTC): 2025-xx-xxTxx:xx:xxZ
	•	Hash: (to be filled by attestation pipeline)
```

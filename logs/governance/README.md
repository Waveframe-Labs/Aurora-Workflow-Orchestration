---
filetype: governance_logs
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Governance Logs — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory contains formal governance records documenting all verifiable actions that affect repository integrity, compliance, or release state.  
Each entry serves as an immutable audit event under AWO’s Attestation and Accountability framework.

---

## Structure

| File / Folder | Description |
|----------------|-------------|
| **2025-10-31_root-sha256sums.md** | Record of the first automated generation of the root integrity registry (`SHA256SUMS.txt`). |
| **attestation_failures/** | (Optional) Logs of attestation or approval anomalies detected by validation workflows. |
| **role_attestations/** | Signed declarations by human or synthetic participants affirming their roles and responsibilities under AWO. |
| **release_governance/** | Historical release governance entries aligned to CHANGELOG and version tags. |
| **integrity_events/** | Machine or workflow-generated logs related to validation or integrity enforcement. |

---

## Logging Policy

Each file **MUST** include the following metadata fields:

| Field | Requirement | Description |
|--------|--------------|-------------|
| **Date** | Required | UTC timestamp of the governance event. |
| **Actor (Role)** | Required | Role identifier (e.g., Orchestrator, Auditor, Critic). |
| **Scope** | Required | The repository subsystem or process affected. |
| **Summary** | Required | Human-readable summary of the event. |
| **Artifacts** | Required | List of affected or generated artifacts (files, tags, or reports). |
| **Linked ADRs** | Optional | Reference to relevant ADRs in `/decisions/`. |
| **Verdict** | Required | Outcome or status (Approved, Rejected, Deferred, etc.). |

---

## Integration
- Governance logs are read by compliance and attestation validators.  
- CRI-CORE will use these entries to verify governance continuity and enforce non-repudiation.  
- Events recorded here are **immutable** once committed and versioned.

---

## Contact  

Waveframe Labs  
swright@waveframelabs.org

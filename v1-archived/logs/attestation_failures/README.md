---
filetype: attestation_failures
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Attestation Failures — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory stores structured records of failed or incomplete attestations detected during verification workflows.  
Each entry documents the conditions, affected artifacts, and corrective actions required to restore compliance.

---

## Structure

| File / Folder | Description |
|----------------|-------------|
| **YYYY-MM-DD_failed_attestation_<run_id>.md** | Detailed failure report for a specific run. Includes role, reason, and impact analysis. |
| **summary_index.json** | (Optional) Machine-readable index aggregating all attestation failure events for CRI-CORE ingestion. |

---

## Logging Schema

Each attestation failure entry **MUST** include the following metadata fields:

| Field | Requirement | Description |
|--------|--------------|-------------|
| **Date** | Required | UTC timestamp of the attestation failure. |
| **Run ID** | Required | Identifier of the affected workflow run. |
| **Actor (Role)** | Required | The responsible or reporting participant. |
| **Failure Type** | Required | Classification (e.g., signature mismatch, missing artifact, invalid manifest). |
| **Artifacts** | Required | List of files or evidence objects involved in the failure. |
| **Linked ADRs** | Optional | Decision records related to attestation policy or enforcement. |
| **Resolution** | Optional | Corrective actions or verification steps pending. |
| **Status** | Required | One of: `Unresolved`, `Resolved`, or `Waived`. |

---

## Enforcement

- All attestation failures **MUST** be logged before a run can proceed to archival or release.  
- CRI-CORE will scan this folder automatically to flag unresolved failures in the Compliance Summary.  
- Failure logs are immutable and serve as part of AWO’s falsifiability and accountability guarantees.

---

## Contact  

Waveframe Labs  
swright@waveframelabs.org

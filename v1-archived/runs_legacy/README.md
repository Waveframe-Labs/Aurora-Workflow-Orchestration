---
filetype: run_archive
version: 1.2.1
updated: 2025-10-30
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Legacy Runs Archive — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory contains **pre-compliance research runs** created before the adoption of the AWO v1.2.1 specification.  
They are preserved for **provenance, traceability, and historical continuity**, but are **excluded** from current reproducibility validation, integrity checks, and CRI-CORE compliance workflows.

---

## Scope

Each subfolder within `/runs_legacy/` represents a distinct execution event under earlier AWO prototypes.  
These folders may include partial or outdated artifacts such as:

| File | Description |
|------|--------------|
| `workflow_frozen.json` | Captures execution parameters and environment context. |
| `report.md` | Partial run summaries or experimental metrics. |
| `approval.json` | Early-stage manual validation or sign-off records. |
| `SHA256SUMS.txt` | Legacy or incomplete checksum ledgers (non-authoritative). |

These artifacts predate AWO v1.2.1’s finalized schema and do not satisfy current falsifiability or attestation requirements.

---

## Compliance Status

Legacy runs within this folder are:
- **Excluded** from the root integrity ledger (`/SHA256SUMS.txt`)  
- **Omitted** from automated CI/CD build validation  
- **Incompatible** with CRI-CORE’s schema enforcement  

Only runs under `/runs/` are valid for compliance and audit under AWO v1.2.1 and later.

---

## Preservation Policy

These runs **must not be modified or deleted**, except for archival compression or relocation.  
They serve as a historical record of the methodology’s evolution from early orchestration tests to full procedural reproducibility.  

Retaining these runs ensures continuity and transparent provenance across the Aurora Research Initiative’s lifecycle.

---

## References

| Document | Purpose |
|-----------|----------|
| `docs/AWO_Method_Spec_v1.2.1.md` | Canonical procedural rules and governance framework. |
| `docs/AWO_Whitepaper_v1.1.1.md` | Conceptual and theoretical foundation of AWO. |
| `logs/governance/` | Oversight, attestation, and audit records. |

---

## Contact  

Waveframe Labs  
Aurora Research Initiative  
swright@waveframelabs.org  
[https://waveframelabs.org](https://waveframelabs.org)

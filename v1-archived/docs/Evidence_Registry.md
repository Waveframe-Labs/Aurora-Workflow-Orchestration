---
filetype: documentation
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Evidence Registry — Aurora Workflow Orchestration (AWO)

## Purpose
The **Evidence Registry** serves as a living index of falsifiability, provenance, and attestation artifacts recorded under AWO.  
It complements ADR-0002 (*Evidence Registry Architecture Decision*) and provides a human-readable summary of all evidence objects referenced across runs, ADRs, and governance files.

Each entry links a **claim**, **artifact**, and **verification record**, establishing a traceable chain of custody for reproducible research.

---

## Registry Structure

| Field | Description | Source |
|-------|--------------|--------|
| **Evidence ID** | Unique hash or run-scoped identifier | Generated per run |
| **Claim / Hypothesis** | The proposition under evaluation | Falsifiability Manifest |
| **Artifact Path** | File containing empirical or reasoning evidence | `/runs/<id>/` |
| **SHA-256 Hash** | Integrity checksum of the artifact | `SHA256SUMS.txt` |
| **Origin Role** | Role responsible for producing the evidence | Run manifest |
| **Verification Role** | Role confirming validity | `approval.json` |
| **Status** | Pass / Fail / Pending | Attestation log |
| **Linked ADRs** | Relevant decision records | `/decisions/` |
| **Timestamp (UTC)** | When evidence was registered | Run metadata |

---

## Example Entry

```yaml
evidence_id: EVD_2025-10-31_001
claim: "Entropy growth predicts horizon expansion"
artifact_path: runs/run_2025-10-31T00-00-42Z/report.md
sha256: "ce8d3ac26f97f391f00a61223b034cdc822d114e23ba381b70ee7601de9e9206"
origin_role: Synthesizer
verification_role: Auditor
status: PASS
linked_adrs: [0002, 0012, 0015]
timestamp: 2025-10-31T03:12:00Z

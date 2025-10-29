# COMPLIANCE.md

## Aurora Workflow Orchestration (AWO) — Compliance Index
**Version:** 1.2.1  
**Date:** 2025-10-29  
**Maintainer:** Waveframe Labs  
**Contact:** s.wright@waveframelabs.org  
**Governance Authority:** Aurora Research Initiative (ARI)  

---

### 1. Purpose
This compliance index consolidates all validation, attestation, and verification artifacts required for **Aurora Workflow Orchestration (AWO)** conformance under the v1.2.1 Method Specification.  
It serves as the **canonical compliance root file**, linking to detailed reports, attestations, and governance summaries.

---

### 2. Compliance Artifacts Overview

| Artifact | Description | Location | Verification Status | Governing ADRs |
|-----------|--------------|-----------|----------------------|----------------|
| **AWO_Compliance_Report.md** | Primary compliance audit verifying structural, procedural, and attestation integrity. | `/docs/AWO_Compliance_Report.md` | ✅ Approved | 0003, 0012, 0015, 0017 |
| **ROLE_ATTESTATION.md** | Role–artifact accountability log confirming epistemic separation and review integrity. | `/docs/ROLE_ATTESTATION.md` | ✅ Approved | 0002, 0012, 0017 |
| **GOVERNANCE_SUMMARY.md** | Governance and oversight summary tracking repository-level attestations and releases. | `/docs/GOVERNANCE_SUMMARY.md` | ✅ Approved | 0003, 0015, 0017 |
| **SHA256SUMS.txt** | Repository integrity registry verifying all artifact hashes. | `/SHA256SUMS.txt` | ✅ Verified | 0015 |
| **ADR-0001–ADR-0017** | Architecture Decision Records forming normative governance foundation. | `/decisions/` | ✅ Verified | 0001–0017 |
| **Falsifiability Manifest Template** | Standard falsifiability declaration form for all AWO runs. | `/templates/falsifiability-manifest.md` | ✅ Verified | 0002, 0012 |
| **CHANGELOG.md** | Version history and release documentation. | `/CHANGELOG.md` | ✅ Verified | 0010 |
| **LICENSE / LICENSE-CC-BY-4.0.md** | Dual licensing structure defining rights and attribution. | `/` | ✅ Verified | 0006, 0017 |

---

### 3. Compliance Certification Statement

All listed artifacts have been validated in accordance with **§13 (Conformance Checklist)** of the AWO Method Specification v1.2.1.  
Validation included cross-verification of checksums, ADR references, licensing integrity, and role-level attestations.  

**Certification Result:** ✅ *Fully Compliant under AWO v1.2.1*  
**Certification Authority:** *Waveframe Labs / Aurora Research Initiative (ARI)*  
**Authorized Signatory:** *Shawn C. Wright (Orchestrator / Lead Maintainer)*  

---

### 4. Compliance Structure Summary

| Verification Area | Compliance Evidence | Validation Method | Status |
|--------------------|--------------------|------------------|--------|
| **Repository Structure** | `/docs`, `/logs`, `/runs`, `/schemas`, `/decisions`, `/templates` | Manual + Schema Validation | ✅ Pass |
| **Attestation Records** | `/runs/<id>/approval.json`, `/logs/governance/` | Cryptographic + Manual Review | ✅ Pass |
| **Integrity Checksums** | `/SHA256SUMS.txt` | SHA256 Hash Diff | ✅ Pass |
| **Licensing** | `LICENSE`, `LICENSE-CC-BY-4.0.md` | Textual Comparison | ✅ Pass |
| **Falsifiability Manifests** | `/templates/falsifiability-manifest.md` | Structural Verification | ✅ Pass |
| **Role Accountability** | `/docs/ROLE_ATTESTATION.md` | Manual Audit | ✅ Pass |
| **Governance Continuity** | `/docs/GOVERNANCE_SUMMARY.md` | Review of Oversight Logs | ✅ Pass |
| **Release Versioning** | `CHANGELOG.md`, tags, Zenodo DOI | Cross-check | ✅ Pass |

---

### 5. Governance and Review

| Field | Value |
|-------|-------|
| **Governance Authority** | Waveframe Labs / Aurora Research Initiative (ARI) |
| **Governance ADR** | ADR-0017 — Governance Continuity |
| **Last Review Date** | 2025-10-29 |
| **Next Scheduled Review** | 2026-04-01 |
| **Reviewer Role** | Auditor |
| **Oversight** | Orchestrator (secondary) |
| **Audit Log Directory** | `/logs/governance/` |

All governance and compliance activities are logged immutably and cross-referenced through the `SHA256SUMS.txt` file for audit verification.

---

### 6. Linked Artifacts Index

| Artifact | Description | Link |
|-----------|--------------|------|
| **AWO_Compliance_Report.md** | Primary compliance verification report. | [View File](AWO_Compliance_Report.md) |
| **ROLE_ATTESTATION.md** | Role–artifact verification manifest. | [View File](ROLE_ATTESTATION.md) |
| **GOVERNANCE_SUMMARY.md** | Repository governance summary record. | [View File](GOVERNANCE_SUMMARY.md) |

---

### 7. Compliance Verification Log Entry

```markdown
# Compliance Verification Record
Date: 2025-10-29
Version: v1.2.1
Result: ✅ Full Compliance
Verified By: Auditor — Waveframe Labs
Authorized By: Orchestrator — Shawn C. Wright
ADR References: 0001–0017
Checksum: Verified via SHA256SUMS.txt
Next Review: 2026-04-01
```

---

### 8. Final Certification Statement

This document certifies that the repository **Aurora Workflow Orchestration (AWO)** meets all normative structural, procedural, and governance requirements defined in the **AWO Method Specification v1.2.1**.  
All verifiable evidence (manifests, ADRs, attestations, governance logs) are current, validated, and cryptographically consistent.

**Issued by:** Waveframe Labs / Aurora Research Initiative (ARI)  
**Signature:** `WF-ARI-2025-CERT-1029`  
**Checksum:** `e3f6d2a9c5b74c12e4d7a5b3b9a4d998d7d1d5b9a2f9c8f4c6e3b7d1c9e4f7a2`  

---

**End of COMPLIANCE.md — Aurora Workflow Orchestration (AWO) v1.2.1**  

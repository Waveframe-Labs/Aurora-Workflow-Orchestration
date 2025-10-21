---
filetype: decision_records
version: 1.1.1
updated: 2025-10-20
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Architectural Decision Records (ADRs)

**Purpose**  
This directory contains the formal governance log of the **Aurora Workflow Orchestration (AWO)** framework.  
Each ADR documents a permanent methodological or structural decision affecting reproducibility, auditing, or implementation standards.

---

## Contents
Each file follows the format `ADR-####-<topic>.md` and includes:
- **Context:** Background or problem statement motivating the decision.  
- **Decision:** The rule, policy, or structural change adopted.  
- **Status:** Accepted, Superseded, or Deprecated.  
- **Consequences:** Downstream effects on documentation, templates, or schema.

---

## Core ADR Index
| ID | Topic | Summary |
|----|--------|----------|
| ADR-0001 | Flagship Positioning | Establishes AWO as the primary reproducibility method within Waveframe Labs. |
| ADR-0002 | Evidence Registry | Defines how artifacts and citations link to falsifiable claims. |
| ADR-0003 | Audit Gates | Introduces mandatory human-approval checkpoints for all releases. |
| ADR-0004 | Logging Schema | Standardizes required log fields and JSONL formatting. |
| ADR-0005 | Portability | Specifies cross-domain transferability and schema neutrality. |
| ADR-0006 | Licensing | Formalizes dual license (Apache 2.0 + CC BY 4.0). |
| ADR-0007 | CRI-CORE Handoff | Outlines transition from method (AWO) to infrastructure (CRI-CORE). |
| ADR-0008 | Whitepaper as Artifact | Defines the AWO whitepaper as a reproducible, citable artifact. |
| ADR-0009 | Case Studies | Establishes Waveframe and Simulator as canonical method applications. |
| ADR-0010 | Release Governance | Defines DOI minting, changelog policy, and archival protocol. |
| ADR-0011 | Template Usage | Standardizes folder templates and audit forms. |
| ADR-0012 | Human-in-Loop Validation | Ensures human oversight in each critical merge decision. |
| ADR-0013 | Audit Types Expansion | Defines multi-layer audit logic: logic, data, and peer review. |
| ADR-0014 | Repository Hardening and Organizational Transfer | Standardized folder documentation, unified metadata and contact info, resolved .github override, and formalized AWO’s migration under Waveframe Labs for long-term reproducibility governance. |   
| ADR-0015 | Attestation Integration & Cryptographic Signing | Adds cryptographic attestation and OIDC signing to bind manifests and checksums, replacing manual audits. |  
| ADR-0016 | Automated PDF Build Integration | Integrate automated PDF generation directly into the repository using GitHub Actions and Pandoc + XeLaTeX. |  
| ADR-0017 | Documentation Governance under Aurora Research Initiative | All AWO documentation, specifications, and workflow outputs are now governed under the **Aurora Research Initiative (ARI)**. |  
  
## Relation to AWO
- ADRs ensure **traceable governance** — every methodological rule has an origin record.  
- Whitepaper citations and schema updates must link to at least one ADR ID.  
- Superseded ADRs remain archived to preserve epistemic continuity.

---

## Maintenance Policy
- ADR numbers are sequential and immutable.  
- Superseded ADRs must reference their replacements.  
- All new ADRs require a changelog entry and inclusion in Zenodo release metadata.

---

## Contact
Waveframe Labs  
swright@waveframelabs.org

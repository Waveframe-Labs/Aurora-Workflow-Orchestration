---
filetype: index
version: 1.1.1
updated: 2025-10-12
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Aurora Workflow Orchestration — Repository Index

This index provides structured navigation for the **Aurora Workflow Orchestration (AWO)** repository.  
Each section links to verified, versioned artifacts that define the framework’s design, governance, and execution.

---

## 1. Core Documentation

| Document | Description |
|-----------|--------------|
| [`README.md`](../README.md) | Primary overview and orientation for AWO. |
| [`docs/AWO_Method_Spec_v1.1.md`](../docs/AWO_Method_Spec_v1.1.md) | Formal specification of the AWO methodology (citable reference). |
| [`docs/AWO_Whitepaper_v1.0.md`](../docs/AWO_Whitepaper_v1.0.md) | Theoretical and epistemological foundation of the orchestration framework. |
| [`docs/CHANGELOG.md`](../docs/CHANGELOG.md) | Chronological record of repository updates and releases. |
| [`logs/WORKFLOW_LOG.md`](../logs/WORKFLOW_LOG.md) | Audited development timeline of AWO with verified entries per release. |

---

## 2. Governance & Provenance

| Directory | Purpose |
|------------|----------|
| [`decisions/`](../decisions) | Architecture Decision Records (ADRs) documenting key governance events. |
| [`schemas/`](../schemas) | JSON schemas defining reproducibility and falsifiability standards. |
| [`templates/`](../templates) | Official templates for logs, manifests, ADRs, and validation reports. |
| [`runs/`](../runs) | Signed and hashed workflow runs with full provenance records. |

---

## 3. Automation & Execution

| File / Folder | Description |
|----------------|--------------|
| [`workflows/`](../workflows) | GitHub Actions and orchestration workflows for AWO execution. |
| [`scripts/`](../scripts) | Supporting automation scripts for validation, attestation, and report generation. |
| [`requirements.txt`](../requirements.txt) | Environment dependencies for reproducible execution. |

---

## 4. Reference & Citation

| File | Description |
|------|--------------|
| [`CITATION.cff`](../CITATION.cff) | Machine-readable citation metadata. |
| [`citation.bib`](../citation.bib) | BibTeX reference for scholarly citation. |
| [`.zenodo.json`](../.zenodo.json) | Zenodo metadata configuration (concept DOI linkage). |
| [`LICENSE`](../LICENSE) | Apache 2.0 license for source code. |
| [`LICENSE-CC-BY-4.0.md`](../LICENSE-CC-BY-4.0.md) | CC BY 4.0 license for documentation and text materials. |

---

## 5. Supporting Files

| File / Folder | Purpose |
|----------------|----------|
| [`figures/`](../figures) | Visual diagrams, process schematics, and banners. |  
| [`index.json`](../index.json) | Machine-readable summary of repository structure. |

---

## Current Repository State

**Version:** v1.1.1  
**Release Date:** 2025-10-12  
**Focus:** Repository Hardening · Organizational Transfer to Waveframe Labs · Attestation Integration  
**Related ADRs:**  
- ADR-0014 — Repository Hardening & Organizational Transfer  
- ADR-0015 — Attestation Integration & Cryptographic Signing  

---

*This index is maintained as part of the AWO provenance layer. Each section corresponds to an auditable component of the repository’s epistemic and operational design.*

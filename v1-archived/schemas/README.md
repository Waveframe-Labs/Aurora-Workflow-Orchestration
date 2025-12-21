# Aurora Workflow Orchestration (AWO)
## Schema Directory — v1.2.2  
Maintainer: Waveframe Labs  
Version: 1.2.2  
Revision Date: 2025-11-04  
License: CC BY 4.0  

---

### Purpose
This directory contains the **canonical schema definitions** governing all Aurora Workflow Orchestration (AWO) artifacts.  
Schemas formalize the structure, metadata, and validation rules for reproducible AI-assisted research workflows.  

These files define **what valid AWO artifacts look like** — not how they are executed.  
Runtime enforcement and automated validation belong to **CRI-CORE** (forthcoming).

---

### Scope
The schemas herein cover static method-level artifacts:
- Research claims and falsifiability manifests  
- Provenance and lineage records  
- Workflow logs and environment snapshots  
- Neurotransparency references and evidence pointers  

These files are **normative** within AWO; all AWO-compliant repositories MUST conform to them unless explicitly superseded by later governance.

---

### File Index

| File | Description | Status | Notes |
|------|--------------|---------|-------|
| `claim.schema.json` | Structure for formal research claims and falsifiability criteria. | ✅ Active | Defines minimal claim format for AWO manifests. |
| `environment.schema.json` | Defines environmental and dependency metadata for reproducibility. | ✅ Active | Must be included in every run folder. |
| `neurotransparency.schema.json` | Governs attribution and traceability of reasoning steps (§1.6). | ✅ Active | Core to AWO’s epistemic integrity. |
| `provenance.schema.json` | Specifies lineage and evidence relationships between artifacts. | ✅ Active | Mandatory for all runs (§6.4). |
| `run_manifest.schema.json` | Canonical structure for falsifiability manifests. | ✅ Active | Used by all run records. |
| `workflow_schema.json` | Defines event and log record format for AWO lifecycle phases. | ✅ Active | References ADR-0004 and ADR-0012. |  

---

### Compliance
All schema files are version-locked to **AWO v1.2.2** and SHOULD NOT be modified post-freeze.  
Future schema extensions (e.g., for model drift or data redaction enforcement) will reside under CRI-CORE.  

Repositories claiming AWO compliance MUST validate manifests, logs, and approvals against the active schemas in this directory prior to attestation.

---

### Governance References
- **ADR-0002** — Falsifiability Manifest Standard  
- **ADR-0003** — Audit and Attestation Requirements  
- **ADR-0004** — Logging and Provenance  
- **ADR-0012** — Human-in-the-Loop Validation  
- **ADR-0015** — Cryptographic Signatures and Checksum Policy  
- **ADR-0017** — Governance Continuity (Aurora Research Initiative)     

---

### License
All schema files are distributed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.  
Use, adaptation, and redistribution are permitted with proper attribution to:  
**Waveframe Labs / Aurora Research Initiative**  
Author: *Shawn C. Wright (ORCID: 0009-0006-6043-9295)*

---

**End of Document — /schemas/README.md (AWO v1.2.2)**

---  

<p align="center">
  <sub>© 2025 Waveframe Labs · Independent Open-Science Research Entity</sub>
</p>  

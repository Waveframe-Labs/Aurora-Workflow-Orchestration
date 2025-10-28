# Aurora Workflow Orchestration (AWO)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17013612.svg)](https://doi.org/10.5281/zenodo.17013612)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0.md)  
[![Cite this repo](https://img.shields.io/badge/Cite-CITATION.cff-important.svg)](CITATION.cff)  
![Last Commit](https://img.shields.io/github/last-commit/Waveframe-Labs/Aurora-Workflow-Orchestration/main)

![AURORA WORKFLOW ORCHESTRATION](figures/awo_banner_cri.PNG)

---

## AWO v1.2 — Finalized Methodology under Waveframe Labs Governance

**Aurora Workflow Orchestration (AWO)** defines the reproducible research and audit-first methodology now implemented in **CRI-CORE**.  
AWO v1.2 formalized the method specification, attestation system, and documentation pipeline now extended under CRI-CORE, which operationalizes the methodology as executable governance infrastructure.

> **AWO defines the rules. CRI enforces them.**

This repository is now **complete and stable**.  
Future runtime and enforcement work continues in [**CRI-CORE**](https://github.com/Waveframe-Labs/CRI-CORE).

---

### DOI Clarification

Two provisional DOIs (`10.5281/zenodo.17401760` and `10.5281/zenodo.17402459`) exist due to a Zenodo account linkage issue.  
The authoritative concept DOI for all AWO versions remains:  
**[10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)**  
When Zenodo merges the linked accounts, the canonical version DOI will update accordingly.

---

## Core Documents

- **Whitepaper** — [`/docs/AWO_Whitepaper_v1.1.md`](docs/AWO_Whitepaper_v1.1.md)  
- **Method Specification** — [`/docs/AWO_Method_Spec_v1.2.md`](docs/AWO_Method_Spec_v1.2.md)  
- **Concept DOI** — [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)

---

## Overview

Aurora Workflow Orchestration (AWO) turns AI-assisted research into **auditable, reproducible workflows**.  
Each execution produces a **signed provenance record**, binding data, logic, and human oversight into a single verifiable artifact.

AWO isn’t just a *theory of reproducibility*. It’s a working reference system written to prove that governance itself can be encoded.  
You can read the papers — or you can run them.

> AWO provides the governance method. CRI-CORE provides the runtime.

---

## Why It Exists

AI accelerates discovery faster than verification can follow.  
**AWO** closes that gap through four governing principles:

1. **Falsifiability first** — every claim must be disprovable, not just plausible.  
2. **Human-in-the-loop rigor** — AI outputs are treated as hypotheses, not truths.  
3. **Immutable provenance** — all runs are signed, hashed, and traceable.  
4. **Transparent governance** — reproducibility replaces trust.

---

## Repository Structure

- `/docs/` → Whitepaper, Method Specification, and Handoff Records  
- `/templates/` → falsifiability manifests, audit checklists  
- `/logs/` → timestamped workflow and decision records  
- `/workflows/` → executable orchestration examples  
- `/decisions/` → Architecture Decision Records (ADRs 0001–0017)  
- `/schemas/` → validation and reproducibility schemas  
- `/runs/` → attested, immutable research runs  

> “If it can’t be audited, it doesn’t count.” — Waveframe Labs

---

## Successor Project

### CRI-CORE — Continuous Research Integration

The **CRI-CORE** repository builds directly on AWO v1.2, implementing:

- Runtime provenance verification  
- Schema validation and falsifiability gates  
- Continuous research integration (CRI) automation  
- Cryptographically sealed audit trails  

[→ View CRI-CORE Repository](https://github.com/Waveframe-Labs/CRI-CORE)

---

## Version Boundary

**AWO v1.2 (Final)** marks completion of the Aurora Workflow Orchestration framework.  
This repository remains the **methodological reference artifact** for reproducible AI–human research.  
All future enforcement and runtime development continues under **CRI-CORE**, which extends AWO’s logic into an executable system.

**Canonical DOI:** [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)  
(*Version-specific DOIs under merge review with Zenodo.*)

---

## Maintainer

**Shawn C. Wright** — independent researcher developing reproducible AI–human workflows  
- ORCID [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  
- Email s wright@waveframelabs.org  
- GitHub [Waveframe-Labs](https://github.com/Waveframe-Labs)

---

## License

- Code → [Apache 2.0](LICENSE)  
- Documentation → [CC BY 4.0](LICENSE-CC-BY-4.0.md)

---

## Maintenance and Continuity

This repository is maintained as a **finalized archival artifact** under **Waveframe Labs**.  
Its structure, governance model, and documentation pipeline have been deliberately preserved for verifiable citation and reuse.

While AWO’s methodological phase concludes here, its enforcement logic lives on in **CRI-CORE** — the runtime expression of the same epistemic framework.

In short:  
**AWO is the standard. CRI is the system.**

---

## Documentation Guard

README and CHANGELOG must reference the concept DOI (10.5281/zenodo.17013612).  
ADR citations must match files in `/decisions/`.  
The CI doc-guard warns by default; set `DOC_GUARD_STRICT=1` to enforce.

---

**Aurora Workflow Orchestration (AWO) v1.2 — Final Method Spec and CRI Handoff Edition**  
The concept DOI above will always resolve to the latest verifiable version.

# Aurora Workflow Orchestration (AWO)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17013612.svg)](https://doi.org/10.5281/zenodo.17013612)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0.md)  
[![Cite this repo](https://img.shields.io/badge/Cite-CITATION.cff-important.svg)](CITATION.cff)  
![Last Commit](https://img.shields.io/github/last-commit/Waveframe-Labs/Aurora-Workflow-Orchestration/main)

![AURORA WORKFLOW ORCHESTRATION](figures/awo_banner_cri.PNG)

> **Aurora Workflow Orchestration (AWO)**  
> A formal method for reproducible AI-assisted research  
> → Falsifiability • Provenance • Attestation • Auditability  
> → Works manually or via **CRI-CORE** automation  
> → Every artifact is signed, structured, and verifiable

AWO is a reproducibility framework for AI-assisted research — turning every run into a verifiable scientific artifact.

---

## Overview

**Aurora Workflow Orchestration (AWO)** defines how AI-assisted research can be made reproducible and auditable.  
It translates reasoning steps, decisions, and evidence into structured files that anyone can verify.

AWO is the **methodology layer** — it governs how reproducibility works.  
**CRI-CORE** is the **execution layer** — it automates that governance.  
Together they form a single, evidence-based research system.

---

## What You’ll Find Here

This repository contains the complete AWO governance layer:

- **Whitepaper** — conceptual rationale (“why”)  
- **Method Specification** — enforceable rules (“how”)  
- **Adoption Guide** — step-by-step usage (“apply”)  
- **Governance Records** — proof of adherence and integrity  
- **Automated Workflows** — reproducibility and checksum validation  

| Category | Description |
|-----------|-------------|
| **Whitepaper** | [AWO Whitepaper v1.2.1](docs/AWO_Whitepaper_v1.2.1.md) ([PDF](docs/AWO_Whitepaper_v1.2.1.pdf)) — Rationale and design philosophy |
| **Method Spec** | [AWO Method Spec v1.2.1](docs/AWO_Method_Spec_v1.2.1.md) ([PDF](docs/AWO_Method_Spec_v1.2.1.pdf)) — Normative definition of compliance |
| **Adoption Guide** | [AWO Adoption Guide](docs/AWO_Adoption_Guide.md) ([PDF](docs/AWO_Adoption_Guide.pdf)) — Practical onboarding |
| **Governance Records** | [`GOVERNANCE_SUMMARY.md`](docs/GOVERNANCE_SUMMARY.md), [`ROLE_ATTESTATION.md`](docs/ROLE_ATTESTATION.md), [`AWO_Compliance_Report.md`](docs/AWO_Compliance_Report.md) |
| **ADR Archive** | Sequential decision history (`decisions/ADR-0001 → ADR-0018`) |
| **Schemas / Templates** | Definitions for falsifiability manifests and attestations (`/schemas/`, `/templates/`) |
| **Runs** | Example reproducible runs with signed approvals (`/runs/`) |

All content is cryptographically verified through [`SHA256SUMS.txt`](./SHA256SUMS.txt)  
and governed by **ADR-0015 → ADR-0018** under the Aurora Research Initiative.

---

## Why AWO Exists

AI now produces ideas faster than science can verify them.  
AWO closes that gap by making reproducibility a **governance system**, not a guideline.

**Core Principles**

1. **Falsifiability First** – every claim must define how it can fail.  
2. **Human-in-the-Loop Rigor** – AI output remains a hypothesis until verified.  
3. **Immutable Provenance** – every artifact is signed, hashed, and auditable.  
4. **Transparent Governance** – reproducibility replaces reputation.

AWO turns the scientific method into a living protocol for evidence.

---

## Quick Start

You don’t need special tools or coding background to use AWO.

1. **Clone or fork the repository**  
   ```bash
   git clone https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration.git
   cd Aurora-Workflow-Orchestration
   ```

2. **Open the Adoption Guide**  
   → [`docs/AWO_Adoption_Guide.md`](docs/AWO_Adoption_Guide.md)  
   It walks you through creating a falsifiability manifest and running your first attested experiment.

3. **View a verified run**  
   Browse `/runs/` to see how manifests, approvals, and logs form a reproducible record.

---

## Documentation Map

| Purpose | Document | Description |
|----------|-----------|-------------|
| Vision & Rationale | [Whitepaper v1.2.1](docs/AWO_Whitepaper_v1.2.1.md) ([PDF](docs/AWO_Whitepaper_v1.2.1.pdf)) | Conceptual and historical background |
| Formal Rules | [Method Spec v1.2.1](docs/AWO_Method_Spec_v1.2.1.md) ([PDF](docs/AWO_Method_Spec_v1.2.1.pdf)) | Normative specification for AWO compliance |
| Adoption & Onboarding | [Adoption Guide](docs/AWO_Adoption_Guide.md) ([PDF](docs/AWO_Adoption_Guide.pdf)) | Practical steps for individuals and teams |
| Governance & Decisions | [ADRs 0001-0018](decisions/) | Formal design records and reasoning lineage |

---

## Adoption Tiers

| Tier | Audience | What It Includes |
|------|-----------|------------------|
| **Minimum** | Individuals | Manual logs + falsifiability manifests |
| **Standard** | Small teams | CI pipelines + attestation workflows |
| **Full** | Institutions / public research | Automated reproducibility via CRI-CORE |

For a ready-to-use template, see the  
[**AWO Template Repository**](https://github.com/Waveframe-Labs/AWO-Template).

---

## Example Projects Using AWO

| Project | Domain | Mode of Use |
|----------|---------|-------------|
| [Waveframe v4.0](https://github.com/Wright-Shawn/Waveframe-v4.0-XR) | Cosmology | Manual orchestration with falsifiability logs and ADRs |
| [Societal Simulator (Black Mirror Edition)](https://github.com/Wright-Shawn/Societal-Progress-Simulator) | Systems modeling | Manual orchestration; demonstrates reproducibility without CI |
| [CRI-CORE](https://github.com/Waveframe-Labs/CRI-CORE) | Research runtime | Automated orchestration, schema validation, and provenance automation |

These examples show AWO in both manual and automated modes.  
Full runtime automation is implemented in **CRI-CORE**.

---

## Common Questions

<details>
<summary><strong>Is AWO useful if I work alone?</strong></summary>
Yes. AWO scales down to a single researcher using manual manifests and logs, and scales up to teams or institutions.
</details>

<details>
<summary><strong>Do I need CRI-CORE to use AWO?</strong></summary>
No. CRI-CORE automates enforcement, but AWO is fully functional on its own.
</details>

<details>
<summary><strong>Does AWO replace peer review?</strong></summary>
No. It strengthens it — by ensuring every claim and artifact is traceable before publication.
</details>

<details>
<summary><strong>Can I publish AWO-based research?</strong></summary>
Yes. Include the AWO concept DOI (10.5281/zenodo.17013612) in your Methods or reproducibility statement.
</details>

---

## Version Boundary

**AWO v1.2.1 (Documentation and Accessibility Update)** marks the finalization of the AWO methodology under Waveframe Labs governance.  
Future updates will appear only as errata or citation additions.

**Canonical DOI:** [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)

---

## Maintainer

**Shawn C. Wright** — Independent Researcher, Waveframe Labs  
- ORCID [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  
- Email s wright@waveframelabs.org  
- GitHub [Waveframe-Labs](https://github.com/Waveframe-Labs)

---

## Citation

If you reference or build upon AWO, please cite using the **concept DOI**.

**APA**

> Wright, S. C. (2025). *Aurora Workflow Orchestration (AWO): A formal framework for reproducible AI-assisted research.*  
> Waveframe Labs / Aurora Research Initiative. https://doi.org/10.5281/zenodo.17013612

**BibTeX**

```bibtex
@software{wright_aurora_workflow_orchestration_2025,
  author       = {Wright, Shawn C.},
  title        = {Aurora Workflow Orchestration (AWO): A formal framework for reproducible AI-assisted research},
  year         = {2025},
  version      = {1.2.1},
  institution  = {Waveframe Labs / Aurora Research Initiative},
  license      = {Apache-2.0 (code), CC BY 4.0 (docs)},
  url          = {https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration},
  doi          = {10.5281/zenodo.17013612}
}
```

---

## Licensing

- **Code** → [Apache 2.0](LICENSE)  
- **Documentation** → [CC BY 4.0](LICENSE-CC-BY-4.0.md)

---

## Repository Status

This repository is an **archival reference artifact** — stable, verifiable, and citable.  
All new runtime development continues in **CRI-CORE**, which automates AWO’s governance logic.

---

## Integrity and Verification

This repository maintains a cryptographic integrity registry (`SHA256SUMS.txt`) at the root.  
It is automatically rebuilt and committed by the **Build root SHA256SUMS** workflow.

[![Integrity Registry](https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration/actions/workflows/root-sha256sums.yml/badge.svg)](https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration/actions/workflows/root-sha256sums.yml)

**Scope**  
- All core documents under `/docs/` (whitepaper, spec, guide)  
- All ADRs under `/decisions/`  
- Compliance and governance files at root  
- Current attested runs under `/runs/`

To verify locally:

```bash
sha256sum --check SHA256SUMS.txt
```

---

## Common Misinterpretations

AWO isn’t a belief system or manifesto.  
It’s a **formal structure** for making AI-assisted research provably reproducible.  
If it feels strict, that’s intentional — rigor is the point.

---

<p align="center">
  <sub>© 2025 Waveframe Labs · Independent Open-Science Research Entity</sub>
</p>

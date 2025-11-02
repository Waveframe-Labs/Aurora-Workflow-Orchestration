# Aurora Workflow Orchestration (AWO)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17013612.svg)](https://doi.org/10.5281/zenodo.17013612)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0.md)  
[![Cite this repo](https://img.shields.io/badge/Cite-CITATION.cff-important.svg)](CITATION.cff)  
![Last Commit](https://img.shields.io/github/last-commit/Waveframe-Labs/Aurora-Workflow-Orchestration/main)

![AURORA WORKFLOW ORCHESTRATION](figures/awo_banner_cri.PNG)

AWO is a reproducibility framework for AI-assisted research — turning every run into a verifiable scientific artifact.

---

## Overview

**Aurora Workflow Orchestration (AWO)** defines a reproducible-research methodology for AI–human collaboration.  
It converts reasoning, version control, and auditability into one governed workflow — making every research run **verifiable, citable, and falsifiable**.

AWO is the *methodology layer*; its successor, **CRI-CORE**, is the *execution layer*. Together they form a continuum:  

> **AWO defines the rules. CRI enforces them.**

---

## What You’ll Find Here

This repository serves as the **canonical reference implementation** of the *Aurora Workflow Orchestration (AWO)* method —  
a reproducibility and falsifiability framework for AI-assisted research.

| Category | Description |
|-----------|--------------|
| **Core Specification** | The normative definition of AWO methodology — [`docs/AWO_Method_Spec_v1.2.1.md`](docs/AWO_Method_Spec_v1.2.1.md) |
| **Governance Artifacts** | Compliance, attestation, and verification records (`GOVERNANCE_SUMMARY.md`, `ROLE_ATTESTATION.md`, `AWO_Compliance_Report.md`) |
| **ADR Archive** | All major design decisions (`/decisions/ADR-0001` → `/ADR-0017`) |
| **Schemas / Templates** | Machine-readable definitions of falsifiability manifests and attestations under `/schemas/` and `/templates/` |
| **Runs** | Example reproducible runs under `/runs/` with frozen workflows and signed approvals |
| **Automation** | GitHub Actions workflows for PDF generation, checksum integrity, and compliance validation |
| **Governance Logs** | Audit and continuity records under `/logs/governance/` |

All content is cryptographically verified through [`SHA256SUMS.txt`](./SHA256SUMS.txt) and governed by ADR-0015–ADR-0017.

---
 
### AWO Is / Isn't

AWO is not a software library. It is a procedural standard — a reproducibility protocol that defines how AI–human workflows can be made falsifiable, auditable, and citable.

```
+--------------------+
|  Aurora (AWO)      |  ← Defines structure
+--------------------+
|  CRI-CORE Runtime  |  ← Executes and validates
+--------------------+
```

---

## Why AWO Exists

AI accelerates discovery faster than verification can follow.  
AWO closes that gap by formalizing reproducibility as governance, not suggestion.

**Core Principles**

1. **Falsifiability First** – every claim must be disprovable.  
2. **Human-in-the-Loop Rigor** – AI output is a hypothesis until verified.  
3. **Immutable Provenance** – every run is signed, hashed, and auditable.  
4. **Transparent Governance** – reproducibility replaces reputation.

AWO treats the *scientific method* as executable code.

---

## Quick Start

1. **Clone this repository**  
   ```bash
   git clone https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration.git
   cd Aurora-Workflow-Orchestration
   ```

2. **Run a minimal test**  
   ```bash
   python cli.py --init --demo
   ```

   This creates a signed, reproducible run under `/runs/`, including frozen workflows, reports, and approval records.

3. **Inspect provenance**  
   Each output is cryptographically signed and archived for audit.

For a complete walkthrough, see the [Adoption Guide](docs/AWO_Adoption_Guide.md).

---

## Documentation Map

| Purpose | Document | Description |
|----------|-----------|-------------|
| Vision & rationale | [AWO Whitepaper v1.1](docs/AWO_Whitepaper_v1.1.md) | Philosophical and historical foundation for AWO. |
| Formal rules | [AWO Method Spec v1.2](docs/AWO_Method_Spec_v1.2.md) | Normative specification defining AWO compliance. |
| Adoption & onboarding | [AWO Adoption Guide](docs/AWO_Adoption_Guide.md) | Step-by-step handbook for individuals and teams. |
| Governance & decisions | [ADRs 0001-0017](decisions/) | Formal design records for all major changes. |

---

## Adoption Tiers

| Tier | Audience | What It Includes |
|------|-----------|------------------|
| **Minimum** | Individual researchers | Manual logs, falsifiability manifests, and local audit records. |
| **Standard** | Small teams | Integrated CI pipelines and attestation workflows. |
| **Full** | Institutions / public research | Automated reproducibility via CRI-CORE runtime. |

For a preconfigured starting point, see the [AWO Template Repository](https://github.com/Waveframe-Labs/AWO-Template).

---

## Example Projects Using AWO

| Project | Domain | AWO Usage | Notes |
|----------|---------|------------|--------|
| [Waveframe v4.0](https://github.com/Wright-Shawn/Waveframe-v4.0-XR) | Cosmology | Manual orchestration | Follows AWO v1.2 structure with falsifiability logs, ADRs, and reproducible documentation. |
| [Societal Simulator (Black Mirror Edition)](https://github.com/Wright-Shawn/Societal-Progress-Simulator) | Systems modeling | Manual orchestration | Demonstrates AWO principles without automated CI; all provenance, audit, and decision artifacts managed manually per AWO v1.2. |
| [CRI-CORE](https://github.com/Waveframe-Labs/CRI-CORE) | Research runtime | Automated orchestration | Demonstrates CI/CD enforcement, schema validation, and provenance automation. |

These are manual orchestration examples — built before CRI-CORE was available.  
They show how AWO principles work without automated CI.  
All provenance, audit, and decision artifacts were managed by hand and logged per AWO v1.2.

Full runtime automation is demonstrated in the **CRI-CORE** repository and upcoming template kits.

---

## Common Questions

**Is AWO useful if I work alone?**  
Yes. AWO supports solo workflows with manual logs and falsifiability manifests. It scales up to teams, but scales down just as well.

**Do I need CRI-CORE to use AWO?**  
No. AWO is fully usable without it. CRI-CORE simply automates enforcement.

**Does AWO replace peer review?**  
No. It strengthens it — by making each claim, revision, and artifact traceable before publication.

**Is AWO a software package?**  
Partially. The included code demonstrates the method, but AWO itself is a procedural governance system.

**Can I submit AWO-based research to journals?**  
Yes. AWO-compliant projects can accompany conventional papers, citing this repository’s DOI as the reproducibility reference.

**Where should I publish AWO-based results?**  
Include the concept DOI (10.5281/zenodo.17013612) in your reproducibility statement or Methods section.

---

## Repository Layout

```
/docs/       → Whitepaper, Method Spec, Adoption Guide, and handoff records  
/decisions/  → Architecture Decision Records (ADR-0001–0017)  
/logs/       → Workflow logs and provenance entries  
/figures/    → Diagrams and lifecycle visuals  
/runs/       → Attested, immutable research runs  
/core/       → Core runtime scripts (non-CRI implementation)  
```

"If it can’t be audited, it doesn’t count." — Waveframe Labs

---

## Successor Project

### CRI-CORE — Continuous Research Integration

Implements the AWO method as runtime governance:
- Provenance verification  
- Schema validation and falsifiability gates  
- Continuous research integration automation  
- Cryptographic audit trails  

[View CRI-CORE Repository](https://github.com/Waveframe-Labs/CRI-CORE)

---

## Common Misinterpretations

**“AWO is software.”**  
Not exactly. AWO is a **method specification** — a governance protocol for how AI-assisted research must be documented, attested, and verified.  
The included code only demonstrates the method; the method itself is procedural, not executable.

**“CRI-CORE and AWO are the same.”**  
No. AWO defines *the rules*; CRI-CORE executes and enforces them at runtime.  
AWO is the **constitution**, CRI is the **runtime judiciary**.

**“AWO requires institutional approval.”**  
False. AWO establishes legitimacy through **reproducibility, falsifiability, and cryptographic attestation**, not reputation.

**“AWO is too heavy for individuals.”**  
Incorrect. It scales down cleanly — a single researcher can run AWO manually with logs, manifests, and checksums,  
and scale up later to CRI-CORE automation without changing the underlying governance model.

---

## Version Boundary

**AWO v1.2.1 (Documentation and Accessibility Update)** marks the finalization of the AWO methodology under Waveframe Labs governance.  
Future changes occur only as errata or citation updates.

**Canonical DOI:** [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)

---

## Maintainer

**Shawn C. Wright** — Independent Researcher, Waveframe Labs  
- ORCID [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  
- Email s wright@waveframelabs.org  
- GitHub [Waveframe-Labs](https://github.com/Waveframe-Labs)

---

---

## Citation

If you reference, replicate, or build upon the AWO method, please cite using the **concept DOI**.

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

This repository is an archival reference artifact — stable, verifiable, and citable.  
All enforcement and runtime development continues in **CRI-CORE**, the operational extension of AWO.  

---  

## Integrity and Verification

This repository maintains a cryptographic integrity registry (`SHA256SUMS.txt`) at the root level.  
The registry is automatically rebuilt and committed by the **Build root SHA256SUMS** workflow.

[![Integrity Registry](https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration/actions/workflows/root-sha256sums.yml/badge.svg)](https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration/actions/workflows/root-sha256sums.yml)

**Scope:**  
- All primary specification, whitepaper, and adoption guide files under `/docs/`.  
- All Architecture Decision Records under `/decisions/`.  
- Core compliance, license, and governance files at repository root.  
- All current (non-legacy) run artifacts under `/runs/`.

**Exclusions:**  
- `/runs_legacy/` (archived data)  
- Workflow files and `.git` internals

To verify locally:

```bash
sha256sum --check SHA256SUMS.txt
```  

AWO is the standard. CRI is the system.   

---

<p align="center">
  <sub>© 2025 Waveframe Labs · Independent Open-Science Research Entity</sub>
</p>  


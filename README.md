# Aurora Workflow Orchestration (AWO)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17013612.svg)](https://doi.org/10.5281/zenodo.17013612)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0.md)  
[![Cite this repo](https://img.shields.io/badge/Cite-CITATION.cff-important.svg)](CITATION.cff)  
![Last Commit](https://img.shields.io/github/last-commit/Waveframe-Labs/Aurora-Workflow-Orchestration/main)

![AURORA WORKFLOW ORCHESTRATION](figures/awo_banner_cri.PNG)

---

## Overview

**Aurora Workflow Orchestration (AWO)** defines a reproducible-research methodology for AI–human collaboration.  
It converts reasoning, version control, and auditability into one governed workflow — so that every research run becomes **verifiable, citable, and falsifiable**.

AWO is the *methodology layer*; its successor, **CRI-CORE**, is the *execution layer*.  
Together they form a continuum:  

> **AWO defines the rules. CRI enforces them.**

---

## Why AWO Exists

AI accelerates discovery faster than verification can follow.  
AWO closes that gap by formalizing reproducibility as governance, not suggestion.

**Core Principles**

1. **Falsifiability First** – every claim must be disprovable.  
2. **Human-in-the-Loop Rigor** – AI output ≠ truth; it’s a hypothesis until verified.  
3. **Immutable Provenance** – every run is signed, hashed, and auditable.  
4. **Transparent Governance** – reproducibility replaces reputation.

AWO treats *scientific method* as executable code.

---

## Quick-Start (Minimal AWO Run)

1. **Clone this repository**  
   ```bash
   git clone https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration.git
   cd Aurora-Workflow-Orchestration
   ```
2. **Run a minimal test**  
   ```bash
   python cli.py --init --demo
   ```
   This generates a reproducible run record under `/runs/`, including  
   `workflow_frozen.json`, `report.md`, and `approval.json`.
3. **Inspect provenance**  
   Each output is cryptographically signed and archived for audit.

For a full tutorial, see the [**Adoption Guide →**](docs/AWO_Adoption_Guide.md)

---

## Visual Model

![AWO Lifecycle](figures/AOM-Workflow-Cycle.PNG)

*Lifecycle of an AWO-compliant research run — from hypothesis fan-out to attested report.*

---

## Documentation Map

| Purpose | Document | Description |
|----------|-----------|-------------|
| Vision & rationale | [**AWO Whitepaper v1.1**](docs/AWO_Whitepaper_v1.1.md) | Philosophical and historical foundation for AWO. |
| Formal rules | [**AWO Method Spec v1.2**](docs/AWO_Method_Spec_v1.2.md) | Normative specification defining AWO compliance. |
| Adoption & onboarding | [**AWO Adoption Guide**](docs/AWO_Adoption_Guide.md) | Step-by-step handbook for individuals and teams. |
| Governance & decisions | [**ADRs 0001-0017**](decisions/) | Formal design records for every major change. |

---

## Adoption Levels

| Tier | Audience | What It Includes |
|------|-----------|------------------|
| **Minimum** | Individuals testing AWO | Run local provenance logs manually. |
| **Standard** | Small teams | Integrate CI pipelines and attestation checks. |
| **Full** | Institutional / public use | Automated verification via CRI-CORE runtime. |

See [**Adoption Guide →**](docs/AWO_Adoption_Guide.md) for implementation steps.

---

## Example Use Cases

- **Waveframe v4.0 – Cosmology Research**  
  Demonstrates audit-based physics modeling with AI co-reasoning.  
- **Aurora Workflow Orchestration (self)**  
  The framework proving its own reproducibility via self-audit.  
- **Future: CRI-CORE**  
  Extends AWO into a live enforcement engine with plugin validation.

---

## FAQs

**Do I need CRI-CORE to use AWO?**  
No. AWO works as a standalone methodology — CRI-CORE simply automates enforcement.

**Is AWO a software package?**  
Partially. The code exists to demonstrate the method, but AWO is primarily *procedural law* for reproducible research.

**Can I modify it for my lab or team?**  
Yes, within the Apache 2.0 + CC BY 4.0 dual-license terms.  
If you extend AWO, cite this repository and the concept DOI.

**Where should I publish AWO-based results?**  
Include the concept DOI (`10.5281/zenodo.17013612`) in your reproducibility statement or Methods section.

---

## Repository Layout

```
/docs/       → Whitepaper, Method Spec, Adoption Guide, handoff records  
/decisions/  → Architecture Decision Records (ADR-0001–0017)  
/logs/       → Workflow logs and provenance entries  
/figures/    → Diagrams and lifecycle visuals  
/runs/       → Attested, immutable research runs  
/core/       → Core runtime scripts (non-CRI implementation)  
```

> “If it can’t be audited, it doesn’t count.” — Waveframe Labs

---

## Successor Project

### [CRI-CORE → Continuous Research Integration](https://github.com/Waveframe-Labs/CRI-CORE)

Implements the AWO method as runtime governance:
- Provenance verification  
- Schema validation and falsifiability gates  
- Continuous research integration automation  
- Cryptographic audit trails  

---

## Version Boundary

**AWO v1.2.1 (Documentation & Accessibility Update)** marks the finalization of the AWO methodology under **Waveframe Labs governance**.  
Future changes occur only as **errata or citation updates**.  

**Canonical DOI:** [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)

---

## Maintainer

**Shawn C. Wright** — Independent Researcher, Waveframe Labs  
- ORCID [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  
- Email s wright@waveframelabs.org  
- GitHub [Waveframe-Labs](https://github.com/Waveframe-Labs)

---

## Licensing

- **Code** → [Apache 2.0](LICENSE)  
- **Documentation** → [CC BY 4.0](LICENSE-CC-BY-4.0.md)

---

## Repository Status

This repository is an **archival reference artifact** — stable, verifiable, and citable.  
All enforcement and runtime development continues in **CRI-CORE**, the operational extension of AWO.

> **AWO is the standard. CRI is the system.**

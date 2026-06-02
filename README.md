---
title: "Aurora Workflow Orchestration (AWO) — Repository Overview"
filetype: "documentation"
type: "non-normative"
version: "2.0.0"
doi: "10.5281/zenodo.17013612"  
status: "Active"
created: "2025-12-25"
updated: "2026-01-09"   

author:
  name: "Shawn C. Wright"
  email: "swright@waveframelabs.org"
  orcid: "https://orcid.org/0009-0006-6043-9295"

maintainer:
  name: "Waveframe Labs"
  url: "https://waveframelabs.org"

license: "Apache-2.0"

copyright:
  holder: "Waveframe Labs"
  year: "2026"

ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting under full human oversight; aligned with AWO v2.0.0 method layer and ARI governance."

anchors:
  - "AWO-README-v2.0.0"
---

<p align="center">
  <img src="https://raw.githubusercontent.com/Waveframe-Labs/.github/main/assets/branding/canon_wf_logo_extended.png" width="700">
</p>

# Aurora Workflow Orchestration (AWO)

[![Waveframe Labs](https://img.shields.io/badge/WAVEFRAME%20LABS-Institutional%20Repository-FF6A00?style=flat)](https://waveframelabs.org)
[![Governed Repository](https://img.shields.io/badge/Governance-ARI%20Compliant-8A2BE2?style=flat)](https://github.com/Waveframe-Labs/Aurora-Research-Initiative)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17013612.svg)](https://doi.org/10.5281/zenodo.17013612)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--6043--9295-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0006-6043-9295)
[![Version](https://img.shields.io/badge/version-2.0.0-blue)](https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration/releases)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

> Method layer of the Waveframe Labs governance stack.  
> Defines **how research is conducted**, not what conclusions are reached.

AWO provides the **normative methodological framework** for running reproducible, auditable, AI‑assisted research workflows.

It formalizes:

- workflow phases  
- artifact classes  
- invariants  
- contracts  
- schema interfaces  

AWO does **not** enforce execution — enforcement belongs to **CRI‑CORE**.

This repository contains the complete **AWO v2.0.0 methodology layer**, replacing all v1.x material now archived under `/v1-archived/`.

---

## Purpose of AWO

AWO answers a single foundational question:

**How must research be structured so that results remain independently reconstructible, auditable, and epistemically valid?**

AWO governs:

- workflow phase ordering  
- artifact production requirements  
- role separation boundaries  
- reproducibility + falsifiability invariants  
- machine‑readable contract surface for CRI‑CORE  

AWO does **not** run workflows or judge correctness.

---

## Where to Start

Recommended reading path:

1. `AWO_OVERVIEW.md`  
2. `SCOPE.md`  
3. `WORKFLOW_SPEC.md`  
4. `ARTIFACT_CLASSES.md`  
5. `ARTIFACT_REQUIREMENTS.md`  
6. `INVARIANTS.md` and `ROLES.md`  
7. `GLOSSARY.md`, `PROVENANCE_MODEL.md`, `NEUROTRANSPARENCY.md`  
8. `/contracts/` — schemas & contract surfaces

---

## Method Execution Flow

```
Initiation → Scoping → Contribution → Review → Approval → Audit
```

Phase progression requires:

- required artifacts exist  
- metadata is complete  
- provenance is intact  
- role separation is enforced  

Self‑attestation and silent revision are prohibited.

---

## Relation to Waveframe Governance Stack

| Layer | System | Responsibility |
|------|--------|----------------|
| 0 | NTD / NTS | Epistemic disclosure & cognitive provenance |
| 1 | ARI | Governance, metadata law, authority boundaries |
| 2 | **AWO** | **Methodology specification (this repo)** |
| 3 | CRI‑CORE | Enforcement + attestation engine |
| 4 | Case Studies | Applications (e.g., Waveframe v4.0) |

---

## Repository Structure

```
/
├── contracts/
│   ├── CONTRACT_INDEX.md
│   ├── ARTIFACT_SCHEMA_MAP.md
│   └── schemas/
│       ├── awo.initiation.schema.json
│       ├── awo.execution.schema.json
│       ├── awo.review.schema.json
│       ├── awo.specification.schema.json
│       └── awo.release.schema.json
│
├── docs/
│   ├── ONBOARDING_GUIDE.md
│   ├── FAQ.md
│   └── CHANGE_LOG.md
│
├── examples/
│   └── awo.initiation.example.json
│
├── method/
│   ├── PHASE_TOPOLOGY.md
│   └── README.md
│
├── v1-archived/
│   (historical materials)
│
├── ADR/
│   ├── README.md
│   └── template.md
│
├── CITATION.cff
├── LICENSE
├── SECURITY.md
└── README.md
```

---

## Licensing & Attribution

- All material is licensed under **Apache‑2.0**
- AI assistance is disclosed per ARI + NTS requirements
- Derived artifacts must preserve metadata and provenance chains

---

## Citation

If you use AWO v2.0.0 in academic writing, tooling design, or reproducible-workflow research, please cite:

CFF (preferred)  
```
cff-version: "1.2.0"
message: "If you use this methodology, please cite it."
title: "Aurora Workflow Orchestration (AWO)"
version: "2.0.0"
doi: "10.5281/zenodo.17013612"
authors:
  - family-names: "Wright"
    given-names: "Shawn C."
    orcid: "https://orcid.org/0009-0006-6043-9295"
```

## Bibtex 

```
@software{AWO_v2_0_0,
  author       = {Wright, Shawn C.},
  title        = {Aurora Workflow Orchestration (AWO) v2.0.0},
  month        = jan,
  year         = 2026,
  publisher    = {Waveframe Labs},
  doi          = {10.5281/zenodo.17013612},
  url          = {https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration}
}
```

---  

<p align="center">
  <sub><strong>© 2026 Waveframe Labs</strong> · Independent Open-Science Research Entity · 
  <a href="https://orcid.org/0009-0006-6043-9295">ORCID: 0009-0006-6043-9295</a> · 
  <a href="https://doi.org/10.5281/zenodo.17013612">DOI: 10.5281/zenodo.17013612</a></sub>
</p>

<p align="center">
  <sub>Governed under the <a href="https://github.com/Waveframe-Labs/Aurora-Research-Initiative">Aurora Research Initiative (ARI)</a></sub>
</p>

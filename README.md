---
title: "Aurora Workflow Orchestration (AWO) — Repository Overview"
filetype: "documentation"
type: "readme"
version: "2.0.0"
status: "Active"
created: "2025-12-25"
updated: "2025-12-25"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting under full human oversight."
anchors:
  - "AWO-README-v2.0.0"
---

# Aurora Workflow Orchestration (AWO)

> Method layer of the Waveframe Labs governance stack.  
> Defines **how research is conducted**, not what conclusions are reached.

AWO provides the **normative methodological framework** for running reproducible, auditable, AI‑assisted research workflows. It formalizes workflow phases, artifact classes, invariants, contracts, and schema interfaces. AWO does **not** enforce execution — enforcement belongs to CRI‑CORE.

This repository contains the **complete AWO v2.0.0 methodology layer**, replacing all v1.x material now located in `/v1-archived/`.

---

## Purpose of AWO

AWO answers one question:

**How must research be structured so that results remain independently reconstructible, auditable, and epistemically valid?**

AWO governs:

- workflow phase ordering  
- artifact production requirements  
- role separation and authority boundaries  
- reproducibility, falsifiability, traceability  
- machine‑readable contract surface for CRI‑CORE  

AWO does **not** run workflows, validate artifacts, or adjudicate truth.

---

## Repository Structure

```
/
├─ /contracts/                 → schemas + machine‑readable contracts
│   ├─ CONTRACT_INDEX.md
│   ├─ ARTIFACT_SCHEMA_MAP.md
│   └─ /schemas/*.schema.json
│
├─ /v1-archived/               → legacy AWO layer (read‑only, not normative)
│
├─ SCOPE.md                    → What AWO governs & boundaries
├─ INVARIANTS.md               → Non‑negotiable methodological laws
├─ ROLES.md                    → Workflow role definitions
├─ WORKFLOW_SPEC.md            → Phase & transition structure
├─ ARTIFACT_CLASSES.md         → Required artifact classes
├─ ARTIFACT_REQUIREMENTS.md    → Mandatory semantic fields per artifact
├─ AWO_OVERVIEW.md             → High‑level conceptual orientation
├─ GLOSSARY.md                 → Normative definitions
├─ PROVENANCE_MODEL.md         → Traceability & reconstruction patterns
├─ DESIGN_LAWS.md              → Design‑time constraints
├─ AWO_NEUROTRANSPARENCY.md    → NTS interface & cognitive disclosure rules
└─ awo.manifest.json           → Machine manifest (metadata index root)
```

---

## Where to Start

New readers should follow documents in this order:

1. **AWO_OVERVIEW.md**
2. **SCOPE.md**
3. **WORKFLOW_SPEC.md**
4. **ARTIFACT_CLASSES.md**
5. **ARTIFACT_REQUIREMENTS.md**
6. **INVARIANTS.md** and **ROLES.md**
7. **GLOSSARY.md**, **PROVENANCE_MODEL.md**, **DESIGN_LAWS.md**
8. **contracts/** *(schemas & validation surface)*

After review, AWO should be deployable by CRI‑CORE or by human process.

---

## Method Execution Flow

```
Initiation → Scoping → Contribution → Review → Approval → Audit
```

Each phase produces **required artifacts**.  
Artifacts without metadata → **invalid**.  
Self‑attestation → **forbidden**.  
Opaque reasoning → **noncompliant**.

---

## Relation to Other Waveframe Layers

| Layer | System | Responsibility |
|---|---|---|
| 0 | NTD / NTS | Epistemic foundations & disclosure law |
| 1 | ARI | Governance, authority, metadata law |
| 2 | **AWO** | **Methodology specification (this repo)** |
| 3 | CRI‑CORE | Enforcement, attestation, validation (future) |
| 4 | Case Studies | Real‑world application of AWO workflows |

Governance sits above AWO.  
Tooling & enforcement sit below.  

---

## Current Status

AWO v2.0.0 is:

- **document‑complete**
- **methodologically stable**
- ready for **CRI‑CORE enforcement integration**
- pending **example workflow runs + test workflows**

Case study integration will begin with **Waveframe v4.0 cosmology**.

---

## Licensing & Attribution

- Documents licensed under **Apache‑2.0**
- AI assistance is transparently disclosed per **NTS & Metadata Policy**
- Derived artifacts (e.g., PDF builds via Forge) must preserve metadata equivalence

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open‑Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

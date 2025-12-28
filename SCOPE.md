---
title: "AWO Scope Definition"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-25"
updated: "2025-12-25"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight and alignment with AWO v2 architectural specification."
dependencies:
  - "AWO_OVERVIEW.md"
  - "INVARIANTS.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-SCOPE-v2.0.0"
---

# AWO Scope Definition

## 1. Purpose

This document defines the **formal scope and boundaries** of  
**Aurora Workflow Orchestration (AWO) v2.0.0**, establishing what the methodology governs,
what belongs upstream, and what must remain downstream.  
This document is **normative**.

---

## 2. In-Scope (Method Layer)

AWO governs:

1. Workflow structure and required phases  
2. Minimum artifact classes required for scientific reconstruction  
3. Methodological traceability and falsifiability conditions  
4. Role participation in each workflow phase  
5. Semantic requirements for artifacts  
6. Procedural validity conditions for scientific work

AWO defines **how work becomes reproducible**, not what work is correct.

---

## 3. Out-of-Scope (By Design)

AWO does **not**:

- Execute workflows or perform enforcement  
- Define runtime or CI/CD logic  
- Specify cryptographic or attestation engines  
- Govern policy, doctrine, or institutional authority  
- Replace ARI, NTD, or NTS  
- Judge correctness of research conclusions  

These responsibilities remain with **CRI‑CORE**, **ARI**, and case‑study repos.

---

## 4. Boundary Relationships

| Layer | Position | AWO Relationship |
|------|----------|------------------|
| ARI | Governance | AWO inherits policy + metadata law |
| NTD/NTS | Epistemic | AWO operationalizes transparency requirements |
| AWO | Method | Defines workflows + artifacts |
| CRI‑CORE | Enforcement | Implements AWO compliance |
| Case‑Studies | Downstream | Must follow AWO to claim reproducibility |

---

## 5. Compliance Statement

This document is valid only if its metadata complies with  
**ARI Metadata Policy v2.0.0**.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open‑Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

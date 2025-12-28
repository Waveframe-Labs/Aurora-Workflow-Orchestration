---
title: "AWO Scope Definition"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-27"
updated: "2025-12-27"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human governance; expanded from minimal version based on architectural alignment with ARI, NTD, NTS, and AWO methodology structure."
dependencies:
  - "AWO_OVERVIEW.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "INVARIANTS.md"
  - "AR I Metadata Policy v2.0.0"
anchors:
  - "AWO-SCOPE-v2.0.0"
---

# Aurora Workflow Orchestration — Scope Definition

## 1. Purpose

This document defines the **formal scope boundary** of
**Aurora Workflow Orchestration (AWO) v2.0.0**.

It establishes what AWO **governs**, what it **does not govern**, and
how it **interfaces** with upstream (doctrine/governance) and downstream
(enforcement/tooling) layers.

This document is **normative**.

---

## 2. Scope Summary

AWO governs:

- structure of research workflows,
- required workflow phases,
- required artifact classes,
- semantic requirements for artifacts,
- role separation within workflows,
- traceability and falsifiability logic.

AWO does **not** govern:

- organizational policy or institutional law (ARI),
- disclosure rules for AI cognition (NTS),
- execution, runtime behavior, or enforcement logic (CRI-CORE),
- publication/formatting outputs (Forge),
- case study scientific content (Waveframe, SHS, etc.).

AWO defines **how work is performed**, not **what results must be true**.

---

## 3. Positive Scope (Things AWO Controls)

### AWO governs methodology when a workflow is declared compliant.

Within an AWO-controlled workflow, the following are binding:

| Domain | AWO Authority |
|-------|---------------|
| Workflow Structure | Required phases + permitted transitions |
| Artifact Taxonomy | Classes, purpose, relation structure |
| Artifact Semantics | Minimum required content & metadata |
| Traceability Model | Inputs, outputs, lineage requirements |
| Falsifiability Conditions | Criteria must be pre-declared |
| Role Participation | Who is allowed to act in each phase |
| Independence | Separation of contribution/review/approval/audit |

If AWO says something **must exist**, then a workflow is invalid without it.

---

## 4. Explicit Out-of-Scope Domains

AWO MUST NOT:

- perform enforcement or verification,
- adjudicate scientific correctness,
- select tools, models, languages, or workflows,
- dictate storage layout or repo structures,
- alter or override ARI, NTD, or NTS requirements,
- govern post-publication activity or dissemination.

These are handled by **CRI-CORE, ARI, NTS, and infrastructure layers.**

AWO is **method only**, never execution.

---

## 5. Workflow Boundary Model

A workflow becomes AWO-governed when:

1. A research intention is declared, **and**
2. An **Initiation Record (A-1)** is created with compliant metadata.

A workflow exits AWO when:

- Approval (A-8) or Abandonment is recorded, **and**
- An **Audit Report (A-9)** verifies artifact completeness.

Anything outside this start-to-exit window is **not AWO’s domain**.

---

## 6. Lifecycle Scope Diagram
```  
[Outside Scope] → Initiation Record → SCOPE + CRITERIA → Contribution →
Review → Approval → Audit → [Outside Scope]
```  
AWO governs where the arrows are fixed, traceable, and role-separated.  

---

## 7. Upstream/Downstream Interaction

### Upstream (AWO must obey)

| Layer | What It Controls |
|---|---|
| **ARI Governance** | Institutional authority & metadata law |
| **NTS** | Cognitive provenance & AI disclosure requirements |
| **NTD Doctrine** | Epistemic rationale for transparency |
| **Role Separation Charter** | Who may do what under conflict rules |

### Downstream (AWO enables but does not control)

| Layer | AWO Provides Inputs To |
|---|---|
| **CRI-CORE** | Enforcement, attestation, runtime validation |
| **Waveframe PDF Forge** | Converts artifacts to publications |
| **Case Studies** | Research workflows executed using AWO |
| **External Tools** | Validators, metadata linters, etc. |

AWO is a **hinge layer** — upstream doctrine constrains it,
downstream tooling operationalizes it.

---

## 8. Misinterpretation Safeguards

AWO **does not imply**:

- research quality,
- scientific correctness,
- publication worthiness,
- validity of conclusions,
- credibility of researchers.

AWO ensures only that:

> **a result can be independently reconstructed, audited,
and falsified without trust in the author.**

---

## 9. Change Control

Any change that modifies:

- required artifacts,
- workflow phases,
- role permissions,
- invariants,

constitutes a **breaking methodological change** and requires a major
version increment + public log.

Clarifications that do not alter meaning may be patch-level updates.

---

## 10. Compliance Requirement

This document is valid only if its metadata complies
with **ARI Metadata Policy v2.0.0**.

Any violation invalidates AWO-scope authority.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

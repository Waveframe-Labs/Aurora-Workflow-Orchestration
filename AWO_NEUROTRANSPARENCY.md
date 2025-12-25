---
title: "AWO Neurotransparency Integration"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; bridges AWO workflow methodology with Neurotransparency Specification (NTS) cognitive provenance obligations."
dependencies:
  - "SCOPE.md"
  - "WORKFLOW_SPEC.md"
  - "INVARIANTS.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "ROLES.md"
  - "Neurotransparency Doctrine (NTD)"
  - "Neurotransparency Specification (NTS)"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-NEUROTRANSPARENCY-v2.0.0"
---

# AWO Neurotransparency Integration

## 1. Purpose

This document defines **how Neurotransparency requirements (NTD + NTS)** apply inside  
**Aurora Workflow Orchestration (AWO) v2.0.0** workflows.

It answers:

> “Where, when, and how must cognitive provenance be disclosed within AWO artifacts?”

This file is **binding for workflow integration**, but **not doctrinal** — authority derives from NTS.

---

## 2. Upstream Authority and Boundaries

- **NTD** provides justification for cognitive traceability.
- **NTS** defines *what disclosure is required*.
- **ARI Metadata Policy v2.0.0** defines field-level metadata requirements.

This file does **not**:
- redefine NTS rules,
- relax disclosure obligations,
- create new governance law.

This file **routes obligations into AWO phases**.

---

## 3. Disclosure Points Inside AWO Workflows

Neurotransparency applies whenever cognition (human or model) contributes to artifact content.

Required NT disclosure per phase:

| Phase | Artifact(s) | NT Requirement |
|---|---|---|
| **P-1 Initiation** | Initiation Record | NT disclosure **optional** unless AI influenced framing |
| **P-2 Scoping** | Scope + Evaluation Criteria | NT disclosure **required** if AI influenced boundaries or criteria |
| **P-3 Contribution** | Contribution + Reasoning Records | NT disclosure **mandatory** for AI-assisted decisions or reasoning |
| **P-4 Review** | Review Report + Issue Register | Must disclose if AI assisted review or critique |
| **P-5 Approval** | Approval Decision | Must disclose whether AI influenced decision justification |
| **P-6 Audit** | Audit Report | Must include NTS compliance assessment + provenance traceability check |

There is **no AWO-compliant workflow without provenance-aware reasoning**.

---

## 4. Provenance Recording Rules

When cognition contributes to an artifact, the artifact MUST disclose:

- origin of cognition (human, model, hybrid)
- whether AI suggestions were accepted, modified, or rejected
- responsibility for final decision (human ownership)
- reasoning or transformation path sufficient for reconstruction
- timestamp + workflow phase context

**Cognition may influence; cognition may not hide.**

---

## 5. Workflow Enforcement Boundary

This document mandates **where disclosure must occur**, not enforcement.

- AWO defines method.
- NTS defines disclosure semantics.
- CRI-CORE will enforce mechanically.

A workflow may claim compliance only if all required NT surfaces exist.

---

## 6. Change Control

Changes to **integration routing** may be minor.

Changes to:
- obligations,
- disclosure semantics,
- NT meaning or requirements,

are **not permitted** here and must occur upstream in NTS/NTD.

---

## 7. Compliance Requirement

This document is valid only while its metadata block is  
**fully compliant with ARI Metadata Policy v2.0.0**.

Metadata violations void institutional status.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

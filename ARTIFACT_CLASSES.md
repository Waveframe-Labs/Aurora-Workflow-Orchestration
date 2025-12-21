---
title: "AWO Artifact Classes"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2025-12-20"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight, aligned to AWO Scope, Invariants, Roles, Workflow Specification, and validated against ARI Metadata Policy v2.0.0."
dependencies:
  - "AWO Scope Definition v2.0.0"
  - "AWO Methodological Invariants v2.0.0"
  - "AWO Workflow Roles v2.0.0"
  - "AWO Workflow Specification v2.0.0"
  - "ARI Metadata Policy v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-ARTIFACT-CLASSES-v2.0.0"
---

# AWO Artifact Classes

## 1. Purpose

This document enumerates the **artifact classes** required by
**Aurora Workflow Orchestration (AWO) v2.0.0**.

Artifact classes are **conceptual categories of required outputs** produced by
workflow phases. This document defines **what artifacts are**, **why they exist**,
and **which phase produces them**, without defining formats, storage, tooling,
or enforcement.

This document is **normative**.

---

## 2. Artifact Class Principles

All AWO artifact classes MUST satisfy the following principles:

- **Explicitness:** the artifact is a discrete, identifiable object.
- **Persistence:** the artifact can be preserved and referenced.
- **Traceability:** the artifact can be linked to inputs and prior artifacts.
- **Role accountability:** responsibility for producing or issuing the artifact is role-bound.
- **Method over execution:** artifact classes describe methodology, not implementation.
- **Metadata compliance:** governed artifacts MUST include compliant YAML metadata (ARI Metadata Policy v2.0.0).

---

## 3. Phase-to-Artifact Mapping (Normative)

This section defines the required artifact classes per workflow phase.

### P-1 — Initiation

#### A-1 — Initiation Record
**Produced by:** Workflow Initiator  
**Purpose:** Establish the research objective, initial scope intent, and declared constraints.

---

### P-2 — Scoping

#### A-2 — Scope Definition Artifact
**Produced by:** Workflow Initiator and/or Contributor (within role constraints)  
**Purpose:** Formally define the bounded problem space and what is explicitly out of scope.

#### A-3 — Evaluation Criteria Artifact
**Produced by:** Workflow Initiator and/or Contributor (within role constraints)  
**Purpose:** Define the criteria by which outputs will be judged sufficient for review and approval.

---

### P-3 — Contribution

#### A-4 — Contribution Artifact
**Produced by:** Contributor  
**Purpose:** Capture substantive research work products (analysis, derivations, experiments, drafts).

#### A-5 — Reasoning Record
**Produced by:** Contributor  
**Purpose:** Preserve structured reasoning sufficient to explain transformations from inputs to outputs.

---

### P-4 — Review

#### A-6 — Review Report
**Produced by:** Reviewer  
**Purpose:** Evaluate contribution artifacts against evaluation criteria and methodological invariants.

#### A-7 — Issue Register
**Produced by:** Reviewer  
**Purpose:** Enumerate identified issues, gaps, ambiguities, or violations requiring resolution.

---

### P-5 — Approval

#### A-8 — Approval Decision Record
**Produced by:** Approver  
**Purpose:** Record approval or rejection of workflow outputs, including the basis of the decision.

---

### P-6 — Audit

#### A-9 — Audit Report
**Produced by:** Auditor  
**Purpose:** Assess invariant compliance, traceability completeness, and auditability sufficiency.

---

## 4. Cross-Phase Artifacts

The following artifact classes may appear across multiple phases, but remain conceptually defined.

#### A-10 — Change Log Entry
**Produced by:** Responsible role for the change context  
**Purpose:** Record material changes to scope, criteria, or workflow structure with traceable justification.

#### A-11 — Dependency Declaration
**Produced by:** Responsible role for the artifact  
**Purpose:** Declare upstream documents, artifacts, or policies that the artifact depends on.

---

## 5. Non-Normative Clarifications

- Artifact formats (Markdown, JSON, YAML) are out of scope.
- Storage layout (folders, naming conventions) is out of scope.
- Enforcement of artifact existence is delegated downstream.
- This document defines classes only; required fields are defined in subsequent semantic and schema specifications.

---

## 6. Stability and Change Control

Changes to artifact classes or phase mappings constitute **breaking methodological changes** and REQUIRE:
- a major version increment,
- explicit documentation of changes,
- preservation of backward traceability.

---

## 7. Compliance Requirement

This document is institutionally valid only if its metadata block complies
with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

---  

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

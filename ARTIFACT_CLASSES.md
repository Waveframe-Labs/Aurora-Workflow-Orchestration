---
title: "AWO Artifact Classes"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2026-01-04"

author:
  name: "Shawn C. Wright"
  email: "swright@waveframelabs.org"

maintainer:
  name: "Waveframe Labs"
  url: "https://waveframelabs.org"

license: "Apache-2.0"

copyright:
  holder: "Waveframe Labs"
  year: "2026"

ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight; revised to align with AWO v2 Design Envelope, Minimal Phase Topology, and revised Workflow Specification."

dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "PHASE_TOPOLOGY.md"

anchors:
  - "AWO-ARTIFACT-CLASSES-v2.0.0"
---

# AWO Artifact Classes

## 1. Purpose

This document defines the **conceptual artifact classes** required by
**Aurora Workflow Orchestration (AWO) v2.0.0**.

Artifact classes are **methodological categories of required outputs**
associated with workflow phases.

This document defines:
- what artifact classes exist,
- why they exist,
- which phase produces them.

It does **not** define formats, schemas, storage, tooling, or enforcement.

This document is **normative**.

---

## 2. Artifact Class Principles

All AWO artifact classes MUST satisfy the following principles:

- **Explicitness:** the artifact is a discrete, identifiable object.
- **Persistence:** the artifact can be preserved and referenced.
- **Traceability:** the artifact can be linked to inputs and prior artifacts.
- **Role accountability:** responsibility for the artifact is role-bound.
- **Method over execution:** artifact classes describe methodology, not implementation.

---

## 3. Phase-Aligned Artifact Classes (Normative)

Artifact classes are aligned to the **Minimal Phase Topology**.

---

### P-1 — Initiation

#### A-1 — Initiation Record
**Produced by:** Workflow Initiator  
**Purpose:**  
Declare research intent, initial assumptions, and the decision to operate under AWO methodology.

---

### P-2 — Specification

#### A-2 — Scope Definition Artifact
**Produced by:** Workflow Initiator and/or Contributor  
**Purpose:**  
Define the bounded problem space and explicitly state what is out of scope.

#### A-3 — Evaluation Criteria Artifact
**Produced by:** Workflow Initiator and/or Contributor  
**Purpose:**  
Declare the criteria by which outputs will later be reviewed for sufficiency.

---

### P-3 — Execution

#### A-4 — Contribution Artifact
**Produced by:** Contributor  
**Purpose:**  
Capture substantive research work products (analysis, derivations, experiments, drafts).

#### A-5 — Reasoning Record
**Produced by:** Contributor  
**Purpose:**  
Preserve structured reasoning sufficient to explain transformations from inputs to outputs.

---

### P-4 — Review

#### A-6 — Review Report
**Produced by:** Reviewer  
**Purpose:**  
Evaluate execution artifacts against declared criteria and methodological constraints.

#### A-7 — Issue Register
**Produced by:** Reviewer  
**Purpose:**  
Enumerate identified issues, gaps, ambiguities, or violations requiring resolution.

---

### P-5 — Release

#### A-8 — Release Record
**Produced by:** Authorized releasing role  
**Purpose:**  
Freeze a workflow iteration and declare the set of artifacts complete for that iteration.

---

## 4. Post-Workflow Artifacts (Outside AWO Phases)

The following artifact classes may reference AWO workflows but are **not workflow phases**.

#### A-9 — Audit Report
**Produced by:** Auditor  
**Purpose:**  
Assess invariant compliance, traceability completeness, and reconstructibility.

Audit occurs **outside AWO workflow execution**.

---

## 5. Cross-Cutting Artifact Classes

These artifact classes may appear at multiple points in a workflow.

#### A-10 — Change Log Entry
**Produced by:** Role responsible for the change context  
**Purpose:**  
Record material changes to scope, criteria, or workflow structure with justification.

#### A-11 — Dependency Declaration
**Produced by:** Artifact owner  
**Purpose:**  
Declare upstream documents, artifacts, or policies relied upon.

---

## 6. Stability and Change Control

Any change to:
- artifact classes,
- phase alignment,
- or artifact purpose,

constitutes a **breaking methodological change** and requires a major version increment.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

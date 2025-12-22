---
title: "AWO Workflow Specification"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2025-12-22"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight; revised to normalize completed AWO v2.0.0 contract schemas and aligned with ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "contracts/ARTIFACT_SCHEMA_MAP.md"
  - "contracts/CONTRACT_INDEX.md"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-WORKFLOW-SPEC-v2.0.0"
---

# AWO Workflow Specification

## 1. Purpose

This document defines the **abstract, normative workflow structure** for
**Aurora Workflow Orchestration (AWO) v2.0.0**.

It specifies required workflow phases, permissible transitions, and required
artifact classes, without defining execution, tooling, or enforcement behavior.

This document is **normative**.

---

## 2. Workflow Model Overview

An AWO workflow is a **finite, phase-structured process** composed of:

- Explicit phases
- Defined role participation
- Required artifact classes
- Deterministic transitions

Every compliant workflow MUST implement all required phases in an order
consistent with this specification.

---

## 3. Required Workflow Phases

### P-1 — Initiation

**Purpose:**
Establish research intent and scope.

**Required Inputs:**
- Research objective
- Initial assumptions
- Declared scope constraints

**Required Artifacts:**
- Initiation record (A-1)

**Permitted Roles:**
- Workflow Initiator

---

### P-2 — Scoping

**Purpose:**
Constrain the problem space and define evaluation criteria.

**Required Inputs:**
- Initiation record

**Required Artifacts:**
- Scope definition artifact (A-2)
- Evaluation criteria (A-3)

**Permitted Roles:**
- Workflow Initiator
- Contributor

---

### P-3 — Contribution

**Purpose:**
Produce substantive research artifacts.

**Required Inputs:**
- Scope definition

**Required Artifacts:**
- Contribution artifacts (A-4)
- Reasoning records (A-5)

**Permitted Roles:**
- Contributor

---

### P-4 — Review

**Purpose:**
Evaluate artifacts for methodological sufficiency.

**Required Inputs:**
- Contribution artifacts

**Required Artifacts:**
- Review report (A-6)
- Issue register when applicable (A-7)

**Permitted Roles:**
- Reviewer

---

### P-5 — Approval

**Purpose:**
Determine whether workflow outputs satisfy defined criteria.

**Required Inputs:**
- Review report

**Required Artifacts:**
- Approval decision record (A-8)

**Permitted Roles:**
- Approver

---

### P-6 — Audit

**Purpose:**
Assess compliance with AWO invariants, role constraints, and traceability requirements.

**Required Inputs:**
- All prior workflow artifacts

**Required Artifacts:**
- Audit report (A-9)

**Permitted Roles:**
- Auditor

---

## 4. Transition Constraints

- Phases MUST occur in the order defined.
- A phase MUST NOT begin unless all required inputs are present.
- Failed review or approval MAY require returning to an earlier phase.
- Audit MAY occur post-approval or at designated checkpoints.

Implicit or skipped phases are prohibited.

---

## 5. Artifact and Schema Normalization

All artifact classes referenced in this specification have corresponding
**machine-readable schemas** defined in `/contracts/schemas/` and indexed in
`contracts/CONTRACT_INDEX.md`.

- Required artifacts (A-1 through A-9) MUST conform to their schemas.
- Optional artifacts (A-10, A-11) MUST conform when present.
- Schema validation does not alter methodological meaning.

---

## 6. Role Compliance

Role participation in each phase MUST conform to:
- AWO Workflow Roles
- Role Separation Charter constraints
- No self-attestation invariants

Violations invalidate the workflow.

---

## 7. Enforcement Boundary

This specification defines **workflow methodology only**.

AWO:
- defines phases and transitions,
- does not execute workflows,
- does not enforce compliance,
- does not validate artifacts.

Enforcement and execution are delegated downstream.

---

## 8. Stability and Change Control

Changes to workflow phases, transitions, or required artifacts constitute
**breaking methodological changes** and REQUIRE:
- a major version increment,
- explicit documentation of changes,
- preservation of backward traceability.

---

## 9. Compliance Requirement

This document is institutionally valid only if its metadata block complies
with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

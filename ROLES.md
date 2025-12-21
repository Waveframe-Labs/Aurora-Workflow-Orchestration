---
title: "AWO Workflow Roles"
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
ai_assistance_details: "AI-assisted drafting with full human oversight, aligned to the Role Separation Charter v1.1.1 and ARI Metadata Policy v2.0.0."
dependencies:
  - "AWO Scope Definition v2.0.0"
  - "AWO Methodological Invariants v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-ROLES-v2.0.0"
---

# AWO Workflow Roles

## 1. Purpose

This document defines the **workflow-level roles** used within
**Aurora Workflow Orchestration (AWO) v2.0.0**.

These roles describe **functional responsibilities within a research workflow**.
They do **not** redefine governance authority, institutional power, or enforcement
capabilities, which are governed upstream by the Role Separation Charter.

This document is **normative**.

---

## 2. Role Model Principles

AWO workflow roles adhere to the following principles:

- Roles are **functional**, not organizational.
- Roles define **responsibilities**, not authority.
- Authority is exercised only where explicitly permitted by upstream governance.
- Role assumption MUST be explicit and declared.
- A single actor MAY occupy multiple workflow roles only if invariants are preserved.

---

## 3. Defined Workflow Roles

### R-1 — Workflow Initiator

**Responsibilities:**
- Defines the research objective and scope.
- Initiates the workflow.
- Declares initial assumptions and constraints.

**Constraints:**
- MUST NOT approve outcomes.
- MUST NOT attest to final validity.

---

### R-2 — Contributor

**Responsibilities:**
- Produces intermediate artifacts.
- Performs analysis, synthesis, or generation tasks.
- Documents reasoning and outputs.

**Constraints:**
- MUST NOT approve or attest to artifacts they produce.
- MUST operate within declared scope.

---

### R-3 — Reviewer

**Responsibilities:**
- Evaluates artifacts against methodological requirements.
- Verifies completeness and consistency.
- Flags violations or ambiguities.

**Constraints:**
- MUST be independent of artifact production.
- MUST declare reviewer role explicitly.

---

### R-4 — Approver

**Responsibilities:**
- Determines whether workflow outputs satisfy defined criteria.
- Issues approval or rejection decisions.

**Constraints:**
- MUST NOT be the same actor as Contributor for approved artifacts.
- Approval does not imply scientific truth, only methodological sufficiency.

---

### R-5 — Auditor

**Responsibilities:**
- Evaluates workflow adherence to AWO invariants.
- Assesses traceability and auditability.
- Documents audit findings.

**Constraints:**
- MUST remain independent of Initiation and Contribution roles.
- MUST NOT modify workflow artifacts.

---

## 4. Role Interaction Constraints

The following interactions are prohibited:

- Self-review or self-approval.
- Silent role switching.
- Undeclared role assumption.
- Reviewer or Auditor producing artifacts they evaluate.
- Approver validating artifacts they contributed to.

Violations invalidate the workflow.

---

## 5. Role Declaration Requirement

All workflow actions that exercise role-specific responsibility MUST explicitly
declare the role being exercised.

Implicit role inference is prohibited.

---

## 6. Relationship to Upstream Governance

This document:
- Defines workflow roles only.
- Defers authority boundaries to the Role Separation Charter.
- Introduces no governance power or enforcement capability.

In case of conflict, upstream governance documents prevail.

---

## 7. Stability and Change Control

Changes to workflow roles constitute **breaking methodological changes** and REQUIRE:
- a major version increment,
- explicit documentation of role impact,
- preservation of backward traceability.

---

## 8. Compliance Requirement

This document is institutionally valid only if its metadata block complies
with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

---  

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

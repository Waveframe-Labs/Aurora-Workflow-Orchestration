---
title: "AWO Artifact Requirements"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; requirements derived from AWO Scope, Invariants, Roles, Workflow Specification, and Artifact Classes; aligned with ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARI Metadata Policy v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-ARTIFACT-REQUIREMENTS-v2.0.0"
---

# AWO Artifact Requirements

## 1. Purpose

This document defines the **minimum semantic requirements** for each
artifact class specified in **ARTIFACT_CLASSES.md**.

It answers the question:
> “What information MUST each artifact contain to be institutionally valid?”

This document is **normative** and binding.

---

## 2. Global Requirements (All Artifacts)

Unless explicitly exempted, all AWO artifacts MUST satisfy the following:

### R-1 — Metadata Compliance
- Governed artifacts MUST include a top-of-file YAML metadata block.
- Metadata MUST comply with **ARI Metadata Policy v2.0.0**.

### R-2 — Role Declaration
- The producing role MUST be explicitly declared.
- The declared role MUST be permitted to produce the artifact class.

### R-3 — Traceability
- Artifacts MUST reference:
  - their immediate inputs, and
  - any upstream artifacts they depend upon.

### R-4 — Determinism Statement
- Artifacts MUST declare whether their contents are deterministic,
  partially deterministic, or nondeterministic.

### R-5 — Change Disclosure
- If an artifact revises or supersedes a prior artifact, that relationship MUST be declared.

---

## 3. Class-Specific Requirements

### A-1 — Initiation Record

MUST include:
- Declared research objective
- Initial scope intent
- Declared constraints or assumptions
- Producing role declaration

---

### A-2 — Scope Definition Artifact

MUST include:
- Explicit in-scope items
- Explicit out-of-scope items
- Boundary rationale
- Revision history (if applicable)

---

### A-3 — Evaluation Criteria Artifact

MUST include:
- Acceptance criteria
- Rejection criteria
- Quality thresholds
- Review applicability notes

---

### A-4 — Contribution Artifact

MUST include:
- Substantive work product
- Input references
- Declared limitations
- Reasoning linkage (direct or indirect)

---

### A-5 — Reasoning Record

MUST include:
- Structured reasoning steps
- Transformations applied to inputs
- Justifications for assumptions
- Known uncertainties or gaps

---

### A-6 — Review Report

MUST include:
- Artifacts reviewed
- Criteria applied
- Findings and concerns
- Reviewer role declaration

---

### A-7 — Issue Register

MUST include:
- Enumerated issues
- Severity or impact assessment
- Required remediation actions

---

### A-8 — Approval Decision Record

MUST include:
- Approval or rejection decision
- Basis for the decision
- Conditions or reservations (if any)
- Approver role declaration

---

### A-9 — Audit Report

MUST include:
- Invariant compliance assessment
- Traceability verification
- Deviations or violations identified
- Auditor role declaration

---

### A-10 — Change Log Entry

MUST include:
- Description of change
- Affected artifacts
- Justification
- Acknowledging role declaration

---

### A-11 — Dependency Declaration

MUST include:
- Enumerated dependencies
- Dependency version identifiers (when available)
- Dependency relevance description

---

## 4. Explicit Non-Requirements

This document DOES NOT define:
- File formats
- Directory structures
- Naming conventions
- Schema validation rules
- Automation behavior

Those concerns are addressed in downstream specifications.

---

## 5. Compliance and Enforcement

Artifacts that fail to meet the requirements in this document are:
- **Noncompliant**
- **Institutionally invalid**
- **Ineligible for approval, audit, or publication**

Enforcement mechanisms are delegated to CRI-CORE and related tooling.

---

## 6. Change Control

Any change to artifact requirements constitutes a **methodological change** and MUST:
- be explicitly documented,
- preserve backward traceability,
- follow semantic versioning rules.

---

## 7. Compliance Statement

This document is valid only if its metadata complies with
**ARI Metadata Policy v2.0.0**.

Any violation of metadata requirements invalidates this document.

---  

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>


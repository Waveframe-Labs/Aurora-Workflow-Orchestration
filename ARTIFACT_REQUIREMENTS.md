---
title: "AWO Artifact Requirements"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; revised to explicitly bind artifact requirements to implemented AWO v2.0.0 contract schemas; aligned with ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "contracts/ARTIFACT_SCHEMA_MAP.md"
  - "contracts/CONTRACT_INDEX.md"
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

### R-6 — Schema Conformance
- If a machine-readable schema exists for an artifact class, the artifact
  MUST conform to that schema.
- Required artifact classes (A-1 through A-9) MUST validate successfully.
- Optional artifact classes (A-10, A-11) MUST validate successfully when present.
- Schema identifiers and status are defined in `contracts/CONTRACT_INDEX.md`.

---

## 3. Class-Specific Requirements

### A-1 — Initiation Record
MUST include:
- Declared research objective
- Initial scope intent
- Declared constraints or assumptions
- Producing role declaration

Schema: `awo.initiation.schema.json`

---

### A-2 — Scope Definition Artifact
MUST include:
- Explicit in-scope items
- Explicit out-of-scope items
- Boundary rationale
- Revision history (if applicable)

Schema: `awo.scope.schema.json`

---

### A-3 — Evaluation Criteria Artifact
MUST include:
- Acceptance criteria
- Rejection criteria
- Quality thresholds
- Review applicability notes

Schema: `awo.evaluation.schema.json`

---

### A-4 — Contribution Artifact
MUST include:
- Substantive work product
- Input references
- Declared limitations
- Reasoning linkage (direct or indirect)

Schema: `awo.contribution.schema.json`

---

### A-5 — Reasoning Record
MUST include:
- Structured reasoning steps
- Transformations applied to inputs
- Justifications for assumptions
- Known uncertainties or gaps

Schema: `awo.reasoning.schema.json`

---

### A-6 — Review Report
MUST include:
- Artifacts reviewed
- Criteria applied
- Findings and concerns
- Reviewer role declaration

Schema: `awo.review.schema.json`

---

### A-7 — Issue Register
MUST include:
- Enumerated issues
- Severity or impact assessment
- Required remediation actions

Schema: `awo.issue_register.schema.json`

---

### A-8 — Approval Decision Record
MUST include:
- Approval or rejection decision
- Basis for the decision
- Conditions or reservations (if any)
- Approver role declaration

Schema: `awo.approval.schema.json`

---

### A-9 — Audit Report
MUST include:
- Invariant compliance assessment
- Traceability verification
- Deviations or violations identified
- Auditor role declaration

Schema: `awo.audit.schema.json`

---

### A-10 — Change Log Entry
MUST include:
- Description of change
- Affected artifacts
- Justification
- Authorizing role declaration

Schema: `awo.change_log.schema.json` (optional)

---

### A-11 — Dependency Declaration
MUST include:
- Enumerated dependencies
- Dependency version identifiers (when available)
- Dependency relevance description

Schema: `awo.dependency.schema.json` (optional)

---

## 4. Explicit Non-Requirements

This document DOES NOT define:
- File formats
- Directory structures
- Naming conventions
- Schema implementation details
- Automation or enforcement behavior

Those concerns are addressed downstream.

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

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

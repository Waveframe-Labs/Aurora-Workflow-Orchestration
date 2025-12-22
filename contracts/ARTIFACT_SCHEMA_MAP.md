---
title: "AWO Artifact Schema Map"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; schema mappings derived from ARTIFACT_CLASSES.md and ARTIFACT_REQUIREMENTS.md; updated to reflect implemented AWO v2.0.0 contract schemas."
dependencies:
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "WORKFLOW_SPEC.md"
  - "contracts/CONTRACT_INDEX.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-ARTIFACT-SCHEMA-MAP-v2.0.0"
---

# AWO Artifact Schema Map

## 1. Purpose

This document defines the **authoritative mapping** between AWO artifact classes
and their corresponding **machine-readable schema identifiers**.

It serves as the binding bridge between:
- human-governed methodological definitions, and
- machine-enforceable validation contracts.

This document is **normative with respect to schema association**.
It does not define schema semantics.

---

## 2. Mapping Principles

- Every artifact class defined by AWO has an associated schema.
- Required artifact classes MUST have active schemas.
- Optional artifact classes MAY have schemas; if present, they are enforceable.
- Schema identifiers are stable; schema versions are managed independently.

---

## 3. Artifact Class → Schema Mapping

| Artifact Class | Schema Identifier | Requirement Level |
|----------------|------------------|-------------------|
| A-1 Initiation Record | `awo.initiation.schema.json` | Required |
| A-2 Scope Definition | `awo.scope.schema.json` | Required |
| A-3 Evaluation Criteria | `awo.evaluation.schema.json` | Required |
| A-4 Contribution Artifact | `awo.contribution.schema.json` | Required |
| A-5 Reasoning Record | `awo.reasoning.schema.json` | Required |
| A-6 Review Report | `awo.review.schema.json` | Required |
| A-7 Issue Register | `awo.issue_register.schema.json` | Required |
| A-8 Approval Decision | `awo.approval.schema.json` | Required |
| A-9 Audit Report | `awo.audit.schema.json` | Required |
| A-10 Change Log Entry | `awo.change_log.schema.json` | Optional |
| A-11 Dependency Declaration | `awo.dependency.schema.json` | Optional |

---

## 4. Completeness Statement

As of **AWO v2.0.0**, all required artifact classes (A-1 through A-9)
have corresponding **active, implemented schemas**.

Optional artifact classes (A-10 and A-11) also have implemented schemas
and may be enforced when present.

---

## 5. Change Control

- Adding, removing, or reclassifying an artifact schema requires updating this map.
- Removing a schema for a required artifact is a breaking change.
- Schema version updates do NOT require changes to this document
  unless the identifier itself changes.

---

## 6. Compliance Statement

This document is institutionally valid only if its metadata complies
with **ARI Metadata Policy v2.0.0**.

Any violation of metadata requirements invalidates this document.

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

---
title: "AWO Artifact Schema Map"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; schema mappings derived from ARTIFACT_CLASSES.md and ARTIFACT_REQUIREMENTS.md and aligned with ARI Metadata Policy v2.0.0."
dependencies:
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "WORKFLOW_SPEC.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-ARTIFACT-SCHEMA-MAP-v2.0.0"
---

# AWO Artifact Schema Map

## 1. Purpose

This document defines the **authoritative mapping** between AWO artifact classes
and their corresponding **machine-readable schema identifiers**.

It acts as a bridge between:
- human-governed methodology (root-level specifications), and
- machine-enforceable contracts (schemas).

This document is **normative** with respect to schema association,
but does not define schema contents.

---

## 2. Mapping Principles

- Every artifact class MAY have a schema.
- If a schema exists, it MUST be listed here.
- Artifact classes without schemas MUST be explicitly noted.
- Schema identifiers are stable references; schema versions are handled separately.

---

## 3. Artifact Class → Schema Mapping

| Artifact Class | Schema Identifier | Required |
|----------------|------------------|----------|
| A-1 Initiation Record | `awo.initiation.schema.json` | YES |
| A-2 Scope Definition | `awo.scope.schema.json` | YES |
| A-3 Evaluation Criteria | `awo.evaluation.schema.json` | YES |
| A-4 Contribution Artifact | `awo.contribution.schema.json` | YES |
| A-5 Reasoning Record | `awo.reasoning.schema.json` | YES |
| A-6 Review Report | `awo.review.schema.json` | YES |
| A-7 Issue Register | `awo.issue_register.schema.json` | YES |
| A-8 Approval Decision | `awo.approval.schema.json` | YES |
| A-9 Audit Report | `awo.audit.schema.json` | YES |
| A-10 Change Log Entry | `awo.change_log.schema.json` | OPTIONAL |
| A-11 Dependency Declaration | `awo.dependency.schema.json` | OPTIONAL |

---

## 4. Schema Absence Rules

If an artifact class does not yet have a schema:
- The artifact remains methodologically valid.
- Tooling MUST NOT assume validation capability.
- The absence MUST be explicit and intentional.

---

## 5. Change Control

- Adding a new schema requires updating this map.
- Renaming or removing a schema is a breaking change.
- Schema version changes do NOT require updating this document
  unless the identifier changes.

---

## 6. Compliance Statement

This document is institutionally valid only if its metadata complies
with **ARI Metadata Policy v2.0.0**.

Any violation of metadata requirements invalidates this document.

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

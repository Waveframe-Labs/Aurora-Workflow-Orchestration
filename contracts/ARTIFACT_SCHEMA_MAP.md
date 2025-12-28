---
title: "AWO Artifact Schema Map"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2025-12-27"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting under human oversight; schema mappings derived from ARTIFACT_CLASSES.md & ARTIFACT_REQUIREMENTS.md; aligned to CONTRACT_INDEX.md and ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "CONTRACT_INDEX.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-ARTIFACT-SCHEMA-MAP-v2.0.0"
---

# AWO Artifact Schema Map

## 1. Purpose

This document defines the **authoritative mapping** between AWO artifact classes
and the **schema identifiers used for machine validation & enforcement**.

It formalizes *which artifact maps to which contract schema*, ensuring that:

- AWO remains methodology-first
- enforcement contracts are traceable to normative definitions
- downstream engines (CRI-CORE, validators, Forge workflows) have a single lookup source

This document is **normative with respect to schema association**, not schema structure.

---

## 2. Mapping Rules

1. Each required AWO artifact class MUST have a schema.
2. Optional artifacts MAY have schemas — if a schema exists, it is enforceable.
3. Schema identifiers are stable, versioned separately from this mapping.
4. Enforcement tools MUST reference this document as the **single source of truth**.

---

## 3. Artifact Class → Schema Identifier Map

| Artifact Class | Contract Key | Schema Filename | Requirement |
|---|---|---|---|
| A-1 Initiation Record | AWO-CONTRACT-A1 | `awo.initiation.schema.json` | Required |
| A-2 Scope Definition | AWO-CONTRACT-A2 | `awo.scope.schema.json` | Required |
| A-3 Evaluation Criteria | AWO-CONTRACT-A3 | `awo.evaluation.schema.json` | Required |
| A-4 Contribution Artifact | AWO-CONTRACT-A4 | `awo.contribution.schema.json` | Required |
| A-5 Reasoning Record | AWO-CONTRACT-A5 | `awo.reasoning.schema.json` | Required |
| A-6 Review Report | AWO-CONTRACT-A6 | `awo.review.schema.json` | Required |
| A-7 Issue Register | AWO-CONTRACT-A7 | `awo.issue_register.schema.json` | Required |
| A-8 Approval Decision | AWO-CONTRACT-A8 | `awo.approval.schema.json` | Required |
| A-9 Audit Report | AWO-CONTRACT-A9 | `awo.audit.schema.json` | Required |
| A-10 Change Log Entry | AWO-CONTRACT-A10 | `awo.change_log.schema.json` | Optional |
| A-11 Dependency Declaration | AWO-CONTRACT-A11 | `awo.dependency.schema.json` | Optional |

---

## 4. Enforcement Boundary

- AWO defines **what must exist**
- CONTRACT_INDEX defines **which contracts exist**
- Schema files define **validation structure**
- CRI-CORE enforces them

No contract may redefine methodology.
No enforcement engine may infer missing schemas.

---

## 5. Change Control

Changes require:

- update to this mapping document
- update to CONTRACT_INDEX.md
- major version bump if mappings change meaningfully

Schema version bumps alone **do not** require updates here.

---

## 6. Compliance Statement

This document is valid only if its metadata complies with
**ARI Metadata Policy v2.0.0**.

Non-compliant metadata voids enforcement authority.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

---
title: "AWO Artifact Schema Map"
short_title: "AWO Schema Map"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2026-01-02"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "CC-BY-4.0"
ai_assisted: "partial"
ai_assistance_details: "Map revised with AI assistance; schema set and scope determined and approved by maintainer."
policy_version: "ARI-Metadata-2.0.0"
dependencies:
  - "DESIGN_ENVELOPE.md"
  - "PHASE_TOPOLOGY.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-ARTIFACT-SCHEMA-MAP-v2.0.0"
---

# AWO Artifact Schema Map

## 1. Purpose

This document defines the **authoritative mapping** between AWO artifact classes and
their corresponding **JSON Schemas** for structural validation.

It exists to ensure that:

- AWO remains strictly **methodological (L1)**
- Artifact expectations are **explicit and finite**
- Downstream tooling (e.g., CRI-CORE, validators, Forge) has a **single source of truth**

This document is **normative with respect to artifact–schema association only**.  
It does **not** define schema structure, validation logic, or enforcement behavior.

---

## 2. Canonical Artifact Set (v2.0.0)

AWO v2.0.0 defines **exactly five** canonical artifact classes.

| Phase | Artifact Class | Schema Filename | Required |
|-----|---------------|-----------------|----------|
| Initiation | AWO Initiation Artifact | `awo.initiation.schema.json` | Yes |
| Specification | AWO Specification Artifact | `awo.specification.schema.json` | Yes |
| Execution | AWO Execution Artifact | `awo.execution.schema.json` | Yes |
| Review | AWO Review Artifact | `awo.review.schema.json` | Yes |
| Release | AWO Release Artifact | `awo.release.schema.json` | Yes |

---

## 3. Mapping Rules

1. Every AWO phase **must** have exactly one schema.
2. Schemas are **structural only** and must remain non-normative.
3. Artifact–schema mappings are **version-locked** to AWO releases.
4. Enforcement engines **must not infer** artifacts not listed here.
5. Tooling **must reference this file** as the canonical lookup source.

---

## 4. Removal of Legacy Artifacts

The following artifact classes and schemas **do not exist** in AWO v2.0.0 and are intentionally removed:

- Scope Definition
- Evaluation Criteria
- Reasoning Record
- Contribution Artifact
- Approval Decision
- Audit Report
- Issue Register
- Change Log Artifact
- Dependency Declaration

Any prior schemas associated with these classes are **non-canonical** and must not be used for validation or enforcement in v2.0.0.

---

## 5. Enforcement Boundary

- AWO defines **what artifacts must exist**
- Schemas define **how those artifacts are structured**
- CRI-CORE (L4) may validate presence, linkage, and completeness
- No enforcement logic is defined or implied here

AWO does not approve, reject, or legitimize artifacts.

---

## 6. Change Control

Changes to this document require:

- explicit revision
- version bump (MINOR or MAJOR)
- corresponding schema changes

Schema-only updates **do not** require changes here unless the artifact set itself changes.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

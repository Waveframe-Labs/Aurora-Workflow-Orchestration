---
title: "AWO Artifact Schema Map"
short_title: "AWO Schema Map"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2026-01-04"

author:
  name: "Shawn C. Wright"
  email: "swright@waveframelabs.org"
  orcid: "https://orcid.org/0009-0006-6043-9295"

maintainer:
  name: "Waveframe Labs"
  url: "https://waveframelabs.org"

license: "Apache-2.0"

copyright:
  holder: "Waveframe Labs"
  year: "2026"

ai_assisted: "partial"
ai_assistance_details: "Map revised with AI assistance; artifact set, scope, and collapse decisions determined and approved by the maintainer."

dependencies:
  - "DESIGN_ENVELOPE.md"
  - "PHASE_TOPOLOGY.md"
  - "ARTIFACT_CLASSES.md"

anchors:
  - "AWO-ARTIFACT-SCHEMA-MAP-v2.0.0"
---

# AWO Artifact Schema Map

## 1. Purpose

This document defines the **authoritative mapping** between
**AWO v2.0.0 artifact classes** and their corresponding **JSON Schemas**
used for structural validation.

It exists to ensure that:

- AWO remains strictly **methodological (L1)**
- Artifact expectations are **explicit, finite, and version-locked**
- Downstream tooling (e.g., CRI-CORE, validators, Forge) has a **single source of truth**

This document is **normative with respect to artifact–schema association only**.  
It does **not** define schema structure, validation logic, or enforcement behavior.

---

## 2. Canonical Artifact Set (AWO v2.0.0)

As a deliberate design decision, **AWO v2.0.0 defines exactly five canonical artifact classes**.
These correspond one-to-one with the minimal phase topology.

| Phase | Artifact Class | Schema Filename | Required |
|------|----------------|-----------------|----------|
| Initiation | AWO Initiation Artifact | `awo.initiation.schema.json` | Yes |
| Specification | AWO Specification Artifact | `awo.specification.schema.json` | Yes |
| Execution | AWO Execution Artifact | `awo.execution.schema.json` | Yes |
| Review | AWO Review Artifact | `awo.review.schema.json` | Yes |
| Release | AWO Release Artifact | `awo.release.schema.json` | Yes |

No other artifact classes are considered canonical in AWO v2.0.0.

---

## 3. Mapping Rules

1. Every AWO phase **MUST** have exactly one canonical artifact.
2. Every canonical artifact **MUST** have exactly one associated schema.
3. Schemas are **structural only** and must remain non-normative.
4. Artifact–schema mappings are **version-locked** to the AWO release.
5. Tooling **MUST NOT infer** artifacts not listed in this document.
6. Downstream systems **MUST reference this file** as the canonical lookup source.

---

## 4. Removal of Legacy Artifact Classes

The following artifact classes existed in earlier conceptual designs but
**do not exist in AWO v2.0.0** and are intentionally removed:

- Scope Definition
- Evaluation Criteria
- Contribution Artifact
- Reasoning Record
- Approval Decision
- Audit Report
- Issue Register
- Change Log Artifact
- Dependency Declaration

Any schemas associated with these classes are **non-canonical** and MUST NOT
be used for validation or enforcement under AWO v2.0.0.

---

## 5. Enforcement Boundary

- AWO defines **what artifacts must exist**
- Schemas define **how those artifacts are structured**
- CRI-CORE (L4) may validate presence, linkage, and completeness
- No approval, rejection, or legitimacy is defined or implied here

AWO does not enforce outcomes.

---

## 6. Change Control

Changes to this document require:
- explicit revision,
- version increment (MINOR or MAJOR),
- corresponding updates to the affected schemas.

Schema-internal changes **do not** require updates here unless the
canonical artifact set changes.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

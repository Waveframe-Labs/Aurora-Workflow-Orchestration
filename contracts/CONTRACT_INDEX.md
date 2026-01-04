---
title: "AWO Contract Index"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-27"
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
ai_assistance_details: "Contract index revised with AI assistance; contract set strictly derived from approved AWO v2 artifact classes and schema map."

dependencies:
  - "ARTIFACT_SCHEMA_MAP.md"
  - "ARTIFACT_CLASSES.md"
  - "PHASE_TOPOLOGY.md"
  - "DESIGN_ENVELOPE.md"

anchors:
  - "AWO-CONTRACT-INDEX-v2.0.0"
---

# AWO Contract Index

## 1. Purpose

This document defines the **authoritative list of machine-enforceable contracts**
that exist under **Aurora Workflow Orchestration (AWO) v2.0.0**.

It answers the question:

> **Which AWO artifacts may be validated or enforced by downstream systems?**

This document is **normative with respect to contract existence and identity only**.
It does **not** define schema structure, validation logic, or enforcement behavior.

---

## 2. Contract Authority Boundary

Contracts listed in this index:

- derive **exclusively** from AWO’s method layer (L1),
- correspond **only** to canonical AWO artifacts,
- MUST NOT introduce new methodological rules,
- MUST NOT encode governance, provenance, or disclosure policy.

Downstream systems (e.g., CRI-CORE) may enforce **only** the contracts listed here.

---

## 3. Canonical AWO v2.0.0 Contracts

AWO v2.0.0 defines **exactly five enforceable contracts**, corresponding
one-to-one with the canonical artifact set defined in `ARTIFACT_SCHEMA_MAP.md`.

| Contract ID | Artifact | Phase | Schema Filename | Status |
|------------|---------|-------|-----------------|--------|
| AWO-CONTRACT-A1 | Initiation Artifact | Initiation | `awo.initiation.schema.json` | Active |
| AWO-CONTRACT-A2 | Specification Artifact | Specification | `awo.specification.schema.json` | Active |
| AWO-CONTRACT-A3 | Execution Artifact | Execution | `awo.execution.schema.json` | Active |
| AWO-CONTRACT-A4 | Review Artifact | Review | `awo.review.schema.json` | Active |
| AWO-CONTRACT-A5 | Release Artifact | Release | `awo.release.schema.json` | Active |

No other contracts are valid under AWO v2.0.0.

---

## 4. Contract Semantics

For each **Active** contract:

- A corresponding JSON Schema **exists**
- The artifact **MUST** conform structurally to that schema
- Validation results are **descriptive**, not authoritative
- Enforcement actions are **out of scope** for AWO

Schemas define structure only.  
They do not approve, reject, or legitimize artifacts.

---

## 5. Explicit Non-Contracts

The following concepts are **not contracts** under AWO v2.0.0 and MUST NOT
be enforced as such:

- workflow graphs or transition engines
- provenance or lineage models
- cognitive or AI disclosure requirements
- metadata policies
- role charters or governance documents

These may be referenced by artifacts, but they are **not AWO contracts**.

---

## 6. Status Semantics

Contract status values are defined as:

- **Active** — Contract exists and may be enforced
- **Deprecated** — Contract maintained for backward compatibility only
- **Retired** — Contract no longer valid for new workflows

All AWO v2.0.0 contracts are **Active**.

---

## 7. Change Control

The identity and existence of AWO contracts are governed by this document.

- Adding or removing a contract:
  - Requires revision of this index
  - Requires a version increment
  - MAY require a major version bump if method scope changes

Schema-internal changes that do not alter contract identity
do **not** require updates here.

---

## 8. Enforcement Boundary

This index defines **what contracts exist** — nothing more.

Downstream systems MUST:

- enforce only contracts listed as **Active**
- fail safely if an unlisted contract is requested
- treat this document as the **single source of truth**

Tooling MUST NOT infer contracts from schema files alone.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

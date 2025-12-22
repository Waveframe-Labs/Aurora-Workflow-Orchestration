---
title: "AWO Contract Index"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-22"
updated: "2025-12-22"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight; contract inventory derived from AWO v2.0.0 normative specifications and ARTIFACT_SCHEMA_MAP.md; aligned with ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "contracts/ARTIFACT_SCHEMA_MAP.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-CONTRACT-INDEX-v2.0.0"
---

# AWO Contract Index

## 1. Purpose

This document is the **authoritative index of all machine-readable contracts**
defined under **Aurora Workflow Orchestration (AWO) v2.0.0**.

It answers the question:
> “What machine-enforceable contracts exist, and which normative artifacts authorize them?”

This document is **normative with respect to contract existence and identity**.
It does not define contract semantics or schema contents.

---

## 2. Contract Governance Model

- All contracts derive authority from **root-level AWO specifications**.
- Contracts MUST NOT introduce new methodological rules.
- Contracts MAY only formalize requirements already defined in normative documents.
- Enforcement tooling MUST rely on this index as the single source of contract truth.

---

## 3. Contract Inventory

### 3.1 Artifact Schemas (Required)

| Contract ID | Schema File | Authorized By | Status |
|-------------|------------|---------------|--------|
| AWO-CONTRACT-A1 | `schemas/awo.initiation.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A2 | `schemas/awo.scope.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A3 | `schemas/awo.evaluation.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A4 | `schemas/awo.contribution.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A5 | `schemas/awo.reasoning.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A6 | `schemas/awo.review.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A7 | `schemas/awo.issue_register.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A8 | `schemas/awo.approval.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A9 | `schemas/awo.audit.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Planned |
| AWO-CONTRACT-A10 | `schemas/awo.change_log.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Optional |
| AWO-CONTRACT-A11 | `schemas/awo.dependency.schema.json` | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md | Optional |

---

## 4. Contract Status Semantics

- **Planned:** Contract is defined but schema not yet implemented.
- **Active:** Schema implemented and approved for enforcement.
- **Deprecated:** Contract retained for compatibility only.
- **Retired:** Contract no longer valid; references prohibited.

Status changes MUST be documented and versioned.

---

## 5. Change Control

- Adding or removing a contract requires updating this index.
- Contract ID changes are breaking changes.
- Schema file updates do NOT require index updates unless identity or status changes.

---

## 6. Enforcement Boundary

- Enforcement engines (e.g., CRI-CORE) MUST NOT infer contracts not listed here.
- Tooling MUST fail safely if a referenced contract is missing or inactive.
- This index supersedes any implicit or ad hoc contract discovery.

---

## 7. Compliance Statement

This document is institutionally valid only if its metadata complies
with **ARI Metadata Policy v2.0.0**.

Any violation of metadata requirements invalidates this document.

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

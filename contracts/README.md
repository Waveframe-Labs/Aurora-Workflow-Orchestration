---
title: "AWO Contracts Directory README"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; describes the normative contract layer of AWO v2.0.0."
dependencies:
  - "CONTRACT_INDEX.md"
  - "ARTIFACT_SCHEMA_MAP.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-CONTRACTS-README-v2.0.0"
---

# AWO Contracts

This directory contains the **machine-readable contract layer** for  
**Aurora Workflow Orchestration (AWO) v2.0.0**.

Contracts formalize *already-defined* methodological requirements into
deterministic schemas that can be validated by downstream tooling.

This directory is **normative** with respect to contract existence and identity.

---

## 1. Purpose of the Contract Layer

The AWO contract layer exists to:

- Provide machine-verifiable representations of AWO artifact requirements
- Enable deterministic validation and enforcement by tooling (e.g., CRI-CORE)
- Support AI indexing, traversal, and dependency analysis
- Prevent implicit or ad hoc contract inference

Contracts do **not** introduce new methodological rules.
They encode requirements defined elsewhere.

---

## 2. Directory Structure

```
/contracts
├── README.md                 # This file
├── CONTRACT_INDEX.md         # Authoritative list of all AWO contracts
├── ARTIFACT_SCHEMA_MAP.md    # Mapping of artifact classes to schemas
└── schemas/                  # JSON Schemas implementing the contracts
```

---

## 3. Contract Authority Model

- All contracts derive authority from root-level AWO specifications:
  - `WORKFLOW_SPEC.md`
  - `ARTIFACT_CLASSES.md`
  - `ARTIFACT_REQUIREMENTS.md`
- Contract existence and status are governed by `CONTRACT_INDEX.md`
- Schema identifiers are stable; schema versions may evolve

Tooling MUST treat this directory as the **single source of truth**
for AWO contract definitions.

---

## 4. Schema Semantics

- Schemas define **structure and required fields only**
- Schemas MUST NOT encode workflow logic, governance decisions, or enforcement behavior
- Validation success or failure does not alter methodological meaning

Schemas are enforcement inputs, not adjudication mechanisms.

---

## 5. Change Control

- Adding or removing a contract requires updating `CONTRACT_INDEX.md`
- Modifying schema semantics requires:
  - alignment with upstream specifications
  - versioning discipline
  - backward traceability
- Breaking changes require a major version increment of AWO

---

## 6. Enforcement Boundary

This directory defines **contracts only**.

- Execution engines live downstream
- Governance authority lives upstream
- This layer MUST remain deterministic, inspectable, and minimal

---

## 7. Compliance Statement

This directory and its contents are institutionally valid only if all
documents and schemas comply with **ARI Metadata Policy v2.0.0**.

Any metadata violation invalidates the affected artifact.

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

---
title: "AWO Contract Schemas"
filetype: "documentation"
type: "specification"
version: "2.0.0"
doi: "10.5281/zenodo.18201829"  
status: "Active"
created: "2025-12-22"
updated: "2026-01-09"

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
ai_assistance_details: "AI-assisted drafting with full human oversight; documents schema scope and constraints without introducing methodological authority."

dependencies:
  - "../ARTIFACT_SCHEMA_MAP.md"
  - "../CONTRACT_INDEX.md"
  - "../../WORKFLOW_SPEC.md"

anchors:
  - "AWO-SCHEMAS-README-v2.0.0"
---

# AWO Contract Schemas

This directory contains the **JSON Schemas** that implement the
**contract layer** of **Aurora Workflow Orchestration (AWO) v2.0.0**.

Schemas are **structural only**.
They encode *how artifacts must be shaped*, not *what they mean*.

---

## 1. Purpose

The schemas in this directory exist to:

- Provide deterministic validation targets for AWO artifacts
- Enable downstream tooling to verify structural completeness
- Prevent implicit or inferred enforcement logic
- Preserve a clean boundary between method and automation

Schemas **do not define workflow rules**.
They **implement** rules defined elsewhere.

---

## 2. Authority Boundaries (Critical)

These schemas derive their authority **exclusively** from upstream documents.

- **Method authority lives in:**
  - `WORKFLOW_SPEC.md`
  - related AWO normative specifications

- **Contract identity and scope live in:**
  - `CONTRACT_INDEX.md`
  - `ARTIFACT_SCHEMA_MAP.md`

- **This directory:**
  - contains schema implementations only
  - must not introduce new rules, roles, or phases

If a requirement does not exist upstream, it **must not appear in a schema**.

---

## 3. Canonical Schema Set (AWO v2.0.0)

Exactly **five** schemas are canonical in AWO v2.0.0:

```
awo.initiation.schema.json
awo.specification.schema.json
awo.execution.schema.json
awo.review.schema.json
awo.release.schema.json
```

Each schema corresponds to **one and only one** AWO artifact class.

No additional schemas are valid unless explicitly added via:
- `ARTIFACT_SCHEMA_MAP.md`
- `CONTRACT_INDEX.md`

---

## 4. Schema Design Rules

All AWO schemas MUST adhere to the following constraints:

- **Structural only**  
  Schemas validate presence, shape, and typing — not correctness.

- **Non-normative**  
  Schemas MUST NOT encode:
  - approval logic
  - role authority decisions
  - workflow transitions
  - enforcement outcomes

- **Deterministic**  
  The same artifact must always validate the same way.

- **Explicit**  
  Required fields must be declared. No inference.

Schemas answer one question:

> “Is this artifact structurally complete according to its declared contract?”

Nothing more.

---

## 5. Validation Semantics

Schema validation results have **no intrinsic authority**.

- Passing validation means:
  - the artifact is structurally complete

- Failing validation means:
  - the artifact is incomplete or malformed

Validation **does not**:
- approve work
- reject conclusions
- assign legitimacy
- override method requirements

Those judgments occur elsewhere.

---

## 6. Change Control

Schema changes are governed as follows:

- **Structural clarifications**
  - Allowed if upstream meaning is unchanged
  - Must preserve backward traceability

- **Semantic changes**
  - Prohibited unless upstream method documents are revised first

- **New schemas**
  - Require updates to:
    - `ARTIFACT_SCHEMA_MAP.md`
    - `CONTRACT_INDEX.md`
  - May require an AWO version increment

Schemas must never lead method.

---

## 7. Enforcement Boundary

This directory does **not** perform enforcement.

- Execution engines are downstream
- Governance is upstream
- This layer remains:
  - inspectable
  - deterministic
  - minimal

Any tool enforcing AWO must treat these schemas as **inputs**, not authority.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity</sub>
</div>

---
title: "AWO Contracts Directory"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; describes the AWO v2.0.0 contract layer without introducing methodological authority."

dependencies:
  - "CONTRACT_INDEX.md"
  - "ARTIFACT_SCHEMA_MAP.md"
  - "../WORKFLOW_SPEC.md"

anchors:
  - "AWO-CONTRACTS-README-v2.0.0"
---

# AWO Contracts

This directory contains the **contract layer** for  
**Aurora Workflow Orchestration (AWO) v2.0.0**.

Contracts are **machine-readable representations** of requirements that are
**already defined elsewhere in the AWO method layer**.

This directory is **normative only with respect to contract existence, identity,
and structural scope**.

---

## 1. Purpose of the Contract Layer

The AWO contract layer exists to:

- Represent required AWO artifacts in machine-verifiable form
- Enable deterministic validation by downstream tooling
- Prevent implicit, inferred, or ad hoc enforcement logic
- Provide a stable interface between human methodology and automation

Contracts **do not create rules**.  
They encode rules that already exist.

---

## 2. Authority Boundaries

The contract layer sits **between** method and enforcement.

- **Upstream authority**  
  Methodological meaning is defined by:
  - `WORKFLOW_SPEC.md`
  - related root AWO specifications

- **This directory**  
  Defines:
  - which contracts exist
  - how they are identified
  - which schemas correspond to which artifacts

- **Downstream enforcement**  
  Execution, validation, and gating are handled by tooling (e.g. CRI-CORE),
  which must not infer rules beyond what is declared here.

At no point does this directory supersede the method layer.

---

## 3. Directory Structure

```
/contracts
├── README.md # This file
├── CONTRACT_INDEX.md # Authoritative list of all AWO contracts
├── ARTIFACT_SCHEMA_MAP.md # Canonical artifact ↔ schema mapping
└── schemas/ # JSON Schemas implementing the contracts
```

---

## 4. Schema Semantics

- Schemas define **structure only**
- Schemas MUST NOT encode:
  - workflow logic
  - governance decisions
  - approval semantics
  - enforcement outcomes

Schema validation answers one question only:

> “Is this artifact structurally complete according to its declared contract?”

Nothing more.

---

## 5. Change Control

- Adding or removing a contract requires:
  - an update to `CONTRACT_INDEX.md`
  - alignment with upstream method documents

- Schema changes MUST:
  - preserve backward traceability
  - remain consistent with the artifact–schema map

Changes to schemas **do not** alter AWO methodology unless upstream documents are revised.

---

## 6. Enforcement Boundary

This directory defines **contracts**, not enforcement.

- It does not execute workflows
- It does not block or approve artifacts
- It does not assign authority

Those responsibilities belong downstream.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity</sub>
</div>

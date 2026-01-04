---
title: "AWO Method Directory README"
filetype: "documentation"
type: "non-normative"
version: "2.0.0"
status: "Active"
created: "2025-12-29"
updated: "2025-12-29"

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
ai_assistance_details: "AI-assisted drafting with full human oversight; README intentionally minimal to prevent method drift and explicitly defer authority to PHASE_TOPOLOGY.md."

dependencies:
  - "PHASE_TOPOLOGY.md"
  - "WORKFLOW_SPEC.md"
  - "SCOPE.md"
  - "INVARIANTS.md"

anchors:
  - "AWO-METHOD-README-v2.0.0"
---

# AWO Method Directory

This directory exists to hold **method-level structural definitions** for  
**Aurora Workflow Orchestration (AWO) v2.0.0**.

It does **not** define workflow rules, artifact requirements, governance, or enforcement.

---

## Purpose of This Directory

The `method/` directory provides a **clear, isolated location** for documents that describe the *structural shape* of the AWO methodology without redefining or extending it.

Its purpose is to:

- Prevent accidental method drift
- Separate structure from explanation
- Provide a stable anchor for downstream tooling and interpretation
- Ensure that method authority is explicit and inspectable

---

## Authoritative Contents

### `PHASE_TOPOLOGY.md`

This file is the **sole authoritative artifact** in this directory.

It defines:

- the minimal phase structure of an AWO workflow
- allowed phase ordering
- topological constraints between phases

No other file in this directory may introduce, modify, or reinterpret method structure.

---

## What This Directory Does *Not* Do

This directory does **not**:

- define workflow entry or exit conditions  
- specify artifact classes or requirements  
- define roles or permissions  
- introduce invariants  
- encode contracts or schemas  
- describe enforcement or tooling behavior  

Those concerns are governed elsewhere in the repository.

---

## Authority Boundary

Method authority resolves in the following order:

1. `SCOPE.md`
2. `INVARIANTS.md`
3. `WORKFLOW_SPEC.md`
4. `method/PHASE_TOPOLOGY.md`

This README is **non-normative** and exists for orientation only.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity · Governed under the Aurora Research Initiative (ARI)</sub>
</div>

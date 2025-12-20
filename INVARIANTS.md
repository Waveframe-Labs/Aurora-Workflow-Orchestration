---
title: "AWO Methodological Invariants"
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
ai_assistance_details: "AI-assisted drafting with full human oversight, cross-checked against ARI Metadata Policy v2.0.0 and the Role Separation Charter v1.1.1, with final approval by the maintainer."
dependencies:
  - "AWO Scope Definition v2.0.0"
  - "ARI Metadata Policy v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-INVARIANTS-v2.0.0"
---

# AWO Methodological Invariants

## 1. Purpose

This document defines the **non-negotiable methodological invariants** of
**Aurora Workflow Orchestration (AWO) v2.0.0**.

Invariants are conditions that MUST hold for any research workflow to be
considered methodologically valid under AWO.

These invariants are **normative** and binding.

---

## 2. Invariant Classifications

AWO invariants fall into four categories:

1. **Structural invariants** — constraints on workflow structure
2. **Authority invariants** — constraints on roles and decision power
3. **Artifact invariants** — constraints on required outputs
4. **Process invariants** — constraints on how transitions occur

Violation of any invariant renders a workflow **non-compliant** with AWO,
regardless of outcome quality.

---

## 3. Structural Invariants

### I-1 — Method Over Execution

AWO defines methodology only.

No AWO-governed document or workflow MAY:
- implement execution logic,
- define runtime behavior,
- specify tooling, engines, or automation,
- or embed enforcement mechanisms.

All execution and enforcement are delegated downstream.

---

### I-2 — Deterministic Structure

AWO workflows MUST be structurally deterministic.

For any given workflow specification:
- phases MUST be explicitly defined,
- transitions MUST be explicit,
- required artifacts MUST be enumerated,
- and permissible orderings MUST be unambiguous.

Non-deterministic or implicit structure is prohibited.

---

## 4. Authority Invariants

### I-3 — Role Separation

Roles defined or referenced within AWO workflows MUST respect the
**Role Separation Charter**.

No workflow MAY:
- collapse governance, method, and enforcement authority,
- permit silent cross-role action,
- or allow implicit role assumption.

Role declaration is mandatory wherever authority is exercised.

---

### I-4 — No Self-Attestation

No actor MAY approve, attest to, or validate artifacts or decisions
originating from the same authority context.

Self-attestation is a categorical violation, regardless of scale or intent.

---

## 5. Artifact Invariants

### I-5 — Artifact Primacy

Research outputs are valid only if supported by required artifacts.

Narrative conclusions, summaries, or claims:
- MUST be derivable from artifacts,
- MUST NOT precede artifact existence,
- MUST NOT substitute for artifacts.

Artifacts are authoritative; prose is interpretive.

---

### I-6 — Metadata Compliance

All AWO-governed artifacts MUST include compliant YAML metadata as defined
by the **ARI Metadata Policy v2.0.0**.

Artifacts lacking required metadata are institutionally invalid and MUST
NOT be treated as compliant inputs or outputs.

---

## 6. Process Invariants

### I-7 — Audit-First Design

Workflows MUST be designed such that auditability is possible without
retrofitting.

This includes:
- explicit phase boundaries,
- preserved intermediate artifacts,
- and reconstructible decision paths.

Auditability is a design requirement, not an afterthought.

---

### I-8 — Methodological Traceability

Each workflow phase MUST be traceable to:
- a defined purpose,
- required inputs,
- and required outputs.

Opaque transitions or unexplained transformations are prohibited.

---

## 7. Invariant Enforcement Boundary

These invariants define **methodological law**.

AWO:
- defines invariants,
- does not enforce them.

Mechanical enforcement, validation, and attestation are delegated to
downstream systems (e.g., CRI-CORE).

---

## 8. Stability and Change Control

Changes to this document constitute **breaking methodological changes**
and REQUIRE:
- a major version increment,
- explicit documentation of invariant changes,
- and preservation of backward traceability.

Minor and patch versions MAY clarify wording but MUST NOT alter invariant meaning.

---

## 9. Compliance Requirement

This document is institutionally valid only if its metadata block complies
with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

---  

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

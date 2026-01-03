---
title: "AWO Methodological Invariants"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2026-01-02"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight, cross-checked against ARI Metadata Policy v2.0.0 and the Role Separation Charter v1.1.1, with final acceptance by the maintainer."
policy_version: "ARI-Metadata-2.0.0"
dependencies:
  - "AWO Scope Definition"
  - "Role Separation Charter v1.1.1 (upstream governance constraint)"
anchors:
  - "AWO-INVARIANTS-v2.0.0"
---

# AWO Methodological Invariants

## 1. Purpose

This document defines the **non-negotiable methodological invariants** of
**Aurora Workflow Orchestration (AWO) v2.0.0**.

Invariants are conditions that MUST hold for any workflow to be considered
**methodologically valid under AWO**.

These invariants are **normative within the method layer** and binding on all
AWO-governed workflows.

Methodological validity under AWO does **not** imply epistemic correctness,
governance approval, institutional legitimacy, or enforcement success.

---

## 2. Invariant Classifications

AWO invariants fall into four categories:

1. **Structural invariants** — constraints on workflow structure
2. **Authority invariants** — constraints on role relationships
3. **Artifact invariants** — constraints on required outputs
4. **Process invariants** — constraints on phase transitions

Violation of any invariant renders a workflow **methodologically non-compliant
with AWO**, regardless of outcome quality or intent.

---

## 3. Structural Invariants

### I-1 — Method Over Execution

AWO defines methodology only.

No AWO-governed document or workflow MAY:
- implement execution logic,
- define runtime behavior,
- specify tools, engines, or automation,
- or embed enforcement mechanisms.

All execution and enforcement concerns are delegated downstream.

---

### I-2 — Deterministic Structure

AWO workflows MUST be structurally deterministic.

For any declared workflow:
- phases MUST be explicit,
- transitions MUST be explicit,
- required artifacts MUST be enumerated,
- and permissible orderings MUST be unambiguous.

Implicit, inferred, or non-deterministic structure is prohibited.

---

## 4. Authority Invariants

### I-3 — Role Separation

Roles referenced within AWO workflows MUST respect the
**Role Separation Charter**.

No workflow MAY:
- collapse methodological, evaluative, and enforcement roles,
- permit silent cross-role action,
- or allow implicit role assumption.

Role declaration is mandatory wherever authority relationships are asserted.

---

### I-4 — No Self-Assertion of Authority

No actor MAY perform a role that asserts evaluative authority over artifacts
or decisions originating from the same authority context.

This includes, but is not limited to:
- reviewing one’s own contributions,
- curating releases derived from one’s own evaluative actions,
- or asserting independence where none exists.

The definition, execution, and enforcement of approval or attestation are
delegated to downstream systems.

---

## 5. Artifact Invariants

### I-5 — Artifact Primacy

Research outputs are **methodologically admissible under AWO** only if
supported by all required artifacts.

Narrative conclusions, summaries, or claims:
- MUST be derivable from artifacts,
- MUST NOT precede artifact existence,
- MUST NOT substitute for required artifacts.

Artifacts are authoritative within the method layer; prose is interpretive.

---

### I-6 — Metadata Compliance

All AWO-governed artifacts MUST include compliant YAML metadata as defined by
the **ARI Metadata Policy v2.0.0**.

Artifacts lacking required metadata are methodologically invalid under AWO and
MUST NOT be treated as compliant inputs or outputs.

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

These invariants define **methodological constraints within AWO**.

AWO:
- defines invariants,
- records compliance,
- does not enforce them.

Mechanical validation, enforcement, and attestation are delegated to
downstream systems (e.g., CRI-CORE).

---

## 8. Stability and Change Control

Changes that modify:
- required artifacts,
- workflow phases,
- role relationships,
- or invariant meaning,

constitute **breaking methodological changes** and REQUIRE:
- a major version increment,
- explicit documentation of invariant changes,
- preservation of backward traceability.

Clarifications MAY be released as patch-level updates provided meaning is
unchanged.

---

## 9. Compliance Requirement

This document is methodologically valid under AWO only if its metadata block
complies with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

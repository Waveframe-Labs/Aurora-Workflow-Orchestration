---
title: "AWO Glossary"
filetype: "documentation"
type: "specification"
version: "2.0.0"
doi: "TBD-2.0.0"  
status: "Active"
created: "2025-12-24"
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
ai_assistance_details: "AI-assisted drafting with human oversight; terminology consolidated from AWO v2 specifications, contracts, schemas, and upstream ARI / NTS doctrine. Definitions constrained to language stabilization only."

dependencies:
  - "OVERVIEW.md"
  - "INVARIANTS.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_SCHEMA_MAP.md"
  - "ROLES.md"
  - "PROVENANCE_MODEL.md"

anchors:
  - "AWO-GLOSSARY-v2.0.0"
---

# AWO Glossary

This document stabilizes terminology used throughout **Aurora Workflow Orchestration (AWO) v2.0.0**.

If language usage varies across documents, this glossary clarifies **intended meaning**,  
but **does not override normative method specifications**.

Method-defining authority remains with:
- `INVARIANTS.md`
- `WORKFLOW_SPEC.md`
- `ROLES.md`
- contract and schema definitions

---

## Core Concepts

**Aurora Workflow Orchestration (AWO)**  
A methodological framework governing reproducible, artifact-first research through explicit phases, role separation, and traceable provenance.

**Method vs. Enforcement**  
AWO defines *what must exist and when*.  
Enforcement (validation, blocking, attestation) is delegated to downstream systems (e.g., CRI-CORE).

**Governance Layer (ARI)**  
Upstream authority governing metadata structure, role legitimacy, and change control.  
AWO operates under ARI but does not redefine it.

**Neurotransparency (NTD / NTS)**  
Upstream epistemic doctrine requiring disclosure of cognitive influence.  
AWO integrates these requirements into workflow artifacts without redefining them.

**Reproducibility (AWO Definition)**  
The ability to reconstruct **decisions, reasoning, and transformations** using artifacts — not merely to re-execute code or experiments.

---

## Artifacts

**Artifact**  
A persistent, role-attributed record capturing epistemically relevant state.  
Actions without artifacts are methodologically invisible.

**Artifact Type**  
One of the canonical AWO artifact categories defined by schema:
- Initiation
- Specification
- Execution
- Review
- Release

**Schema Compliance**  
Conformance of an artifact to its structural JSON schema.  
Schema compliance is necessary but not sufficient for methodological validity.

**Supersession**  
Replacement of an artifact by a later version while preserving lineage.  
Artifacts are never silently modified.

**Invalid Artifact**  
An artifact that fails schema, provenance, or role constraints.  
Invalid artifacts MUST NOT participate in workflow progression.

---

## Workflow Structure

**Workflow Phase**  
One of the required AWO stages:
Initiation → Specification → Execution → Review → Release

**Entry Condition**  
The minimum required artifacts or declarations to enter a phase.

**Exit Condition**  
The artifacts or attestations required to progress forward.

**Transition**  
An explicit, traceable movement between phases.  
Implicit transitions are invalid.

---

## Roles

**Role**  
A formally defined locus of authority within a workflow.

**Originator**  
Declares intent and scope; may not approve or audit outcomes.

**Contributor / Executor**  
Produces substantive work artifacts under a governing specification.

**Reviewer**  
Evaluates artifacts against declared criteria without modifying them.

**Approver**  
Declares acceptance or rejection outcomes; must be independent of contribution.

**Auditor**  
Verifies invariant compliance, provenance completeness, and role separation.

---

## Provenance & Verification

**Provenance**  
The complete, linked lineage describing where an artifact came from, how it was formed, and who acted.

**Provenance Chain**  
A reconstructible graph of artifacts and references proving methodological history.

**Attestation**  
A formal declaration that a workflow state meets required conditions.  
Self-attestation is prohibited.

**Evidence**  
Artifacts or records that substantiate claims.  
Claims without evidence are methodologically void.

---

## Compliance Vocabulary

| Term | Meaning |
|---|---|
| MUST | Mandatory without exception |
| MUST NOT | Prohibited; violation invalidates workflow |
| SHOULD | Strong recommendation; deviations require justification |
| MAY | Optional |
| INVALID | Not eligible for workflow progression |
| COMPLIANT | Meets structural, role, and provenance requirements |

---

## Change Control

Changes that alter term meaning require a **major version increment**.  
Clarifications that preserve meaning may be minor revisions.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity</sub>
</div>

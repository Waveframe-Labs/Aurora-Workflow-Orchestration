---
title: "AWO Neurotransparency Integration"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-25"
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
ai_assistance_details: "AI-assisted drafting with full human governance; revised to align AWO v2 workflow methodology with Neurotransparency obligations without redefining doctrine."

dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_SCHEMA_MAP.md"
  - "Neurotransparency Doctrine (NTD)"
  - "Neurotransparency Specification (NTS)"

anchors:
  - "AWO-NEUROTRANSPARENCY-v2.0.0"
---

# AWO Neurotransparency Integration

## 1. Purpose

This document defines **how Neurotransparency obligations are surfaced and
routed within Aurora Workflow Orchestration (AWO) v2.0.0 workflows**.

It answers the question:

> *Where and when must cognitive influence be disclosed within an AWO workflow?*

This document is **normative for AWO integration only**.  
It does **not** define, modify, or supersede Neurotransparency doctrine or specification.

---

## 2. Authority Boundary (Normative)

Neurotransparency authority is strictly layered:

- **NTD** defines *why* cognitive provenance matters.
- **NTS** defines *what must be disclosed*.
- **AWO** defines *where disclosure appears in the workflow*.

This document:

- DOES route NTS obligations into AWO phases
- DOES NOT redefine disclosure semantics
- DOES NOT weaken or strengthen NTS requirements
- DOES NOT introduce new cognitive governance rules

If this document conflicts with NTS or NTD, **NTS/NTD prevails**.

---

## 3. Scope of Application

Neurotransparency applies whenever cognition influences an AWO artifact.

Cognition includes:
- human reasoning,
- AI-generated suggestions,
- hybrid human-AI synthesis,
- automated systems that affect artifact content.

Disclosure is required **only for governed AWO artifacts**:

- `awo.initiation`
- `awo.specification`
- `awo.execution`
- `awo.review`
- `awo.release`

---

## 4. Phase-Based Disclosure Routing

The following table defines **where Neurotransparency disclosures must occur**
within an AWO v2 workflow.

| Phase | Artifact | Disclosure Requirement |
|-----|--------|------------------------|
| **Initiation** | Initiation Artifact | Required **only if** AI influenced framing or intent |
| **Specification** | Specification Artifact | Required if AI influenced scope, assumptions, or planning |
| **Execution** | Execution Artifact | Required for AI-assisted decisions, generation, or automation |
| **Review** | Review Artifact | Required if AI assisted evaluation, critique, or triage |
| **Release** | Release Artifact | Required if AI influenced curation, selection, or packaging |

Absence of disclosure implies **no AI cognitive influence** and constitutes an explicit declaration.

---

## 5. Disclosure Content (Non-Semantic)

AWO does not define disclosure format or semantics.

However, each disclosure MUST be sufficient to support NTS requirements, including:

- cognitive origin (human / AI / hybrid),
- level of human engagement or oversight,
- responsibility for final decisions,
- traceability to affected artifacts or sections.

AWO requires **presence and placement**, not interpretation.

---

## 6. Provenance Relationship

Neurotransparency disclosures are **cognitive provenance**.  
AWO provenance (defined in `PROVENANCE_MODEL.md`) is **workflow provenance**.

Both are required for a workflow to be reconstructible.

Neither substitutes for the other.

---

## 7. Enforcement Boundary

AWO mandates **that disclosure surfaces exist**.

- AWO does not evaluate correctness of disclosures
- AWO does not validate NTS semantics
- AWO does not enforce compliance

Mechanical enforcement is delegated downstream (e.g., CRI-CORE).

---

## 8. Change Control

This document may change **only** to:

- adjust routing alignment with AWO workflow structure,
- clarify placement of disclosures.

Changes to Neurotransparency meaning, scope, or requirements
**must occur in NTS/NTD**, not here.

---

## 9. Compliance Statement

This document is valid only as an integration layer between
AWO v2 and Neurotransparency doctrine.

It carries no independent epistemic or governance authority.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

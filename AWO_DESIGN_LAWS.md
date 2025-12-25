---
title: "AWO Design Laws"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-25"
updated: "2025-12-25"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight; derived from AWO v2 normative methodology architecture."
dependencies:
  - "AWO_OVERVIEW.md"
  - "INVARIANTS.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "ARTIFACT_CLASSES.md"
  - "PROVENANCE_MODEL.md"
anchors:
  - "AWO-DESIGN-LAWS-v2.0.0"
---

# AWO Design Laws

## 1. Purpose
This document establishes the **meta‑level design laws** guiding AWO methodology development. 
Unlike invariants (non‑negotiable rules for validity), design laws define **how AWO itself must be designed, expanded, and reasoned about** going forward.

This document is normative for AWO *architecture*, not for workflow execution.

## 2. Design Law Principles

### D‑1 — Law of Upstream Supremacy
AWO may never contradict ARI, NTS, or NTD.  
If a conflict exists, **upstream prevails**.

### D‑2 — Law of Method Over Execution
AWO defines **method** only — never tooling, enforcement logic, runtime behavior, or CI workflows.

### D‑3 — Law of Explicitness
No workflow, artifact, or rule may rely on implicit interpretation.  
If it matters, it must be written.

### D‑4 — Law of Artifact‑First Cognition
No epistemic event is recognized unless it produces a governed artifact.

### D‑5 — Law of Falsifiable Procedure
AWO must enable others to *disprove claims*, not just reproduce them.

### D‑6 — Law of Role Independence
No design path may collapse authority roles or allow self‑attestation.

### D‑7 — Law of Forward Traceability
Every artifact, rule, and schema must be version‑traceable and auditable retroactively.

### D‑8 — Law of Schema‑Bound Semantics
Meaning must reside in **schemas + requirements**, not prose alone.

### D‑9 — Law of Mechanizable Enforcement
Rules should be written such that a machine *can* enforce them later via CRI‑CORE.

## 3. Change Control
Design laws are **high‑level architectural constraints**.
They may only change through a major version revision and must preserve historical traceability.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

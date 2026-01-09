---
title: "AWO Onboarding Guide"
filetype: "documentation"
type: "guide"
version: "2.0.0"
doi: "TBD-2.0.0"  
status: "Active"
created: "2025-12-28"
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
ai_assistance_details: "AI-assisted drafting under explicit human direction; content constrained to onboarding guidance and aligned with AWO v2 normative documents."

dependencies:
  - "OVERVIEW.md"
  - "SCOPE.md"
  - "WORKFLOW_SPEC.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "PROVENANCE_MODEL.md"
  - "ARTIFACT_SCHEMA_MAP.md"

anchors:
  - "AWO-ONBOARDING-GUIDE-v2.0.0"
---

# AWO Onboarding Guide  
*How to begin working inside the Aurora Workflow Orchestration method layer*

---

## 1. What This Guide Is

This document is a **practical orientation for working inside AWO-governed workflows**.

It does **not** define:
- method,
- rules,
- contracts,
- enforcement,
- or governance.

Those are defined elsewhere and are authoritative.

This guide exists to answer:

- Where do I start?
- What should I read first?
- How do artifacts and roles appear in practice?
- How do I participate without breaking invariants?

If this guide helps you enter a workflow without guessing, it has done its job.

---

## 2. How AWO Works (In Plain Terms)

AWO governs **how work is conducted**, not what conclusions must be reached.

At a high level:

> A workflow is valid only when its actions, decisions, and reasoning are
> captured as explicit, traceable artifacts produced under declared roles.

Three principles matter most:

| Principle | What it means |
|---------|---------------|
| **Explicit structure** | Phases and transitions are declared, not implied |
| **Artifact authority** | Claims follow artifacts, not explanations |
| **Role separation** | No silent authority blending or self-validation |

This is not bureaucracy — it is how uncertainty stays legible.

---

## 3. What to Read First (Order Matters)

If you are new, read these in sequence:

1. `OVERVIEW.md` — what AWO is and is not
2. `SCOPE.md` — what AWO governs
3. `WORKFLOW_SPEC.md` — phases and transitions
4. `INVARIANTS.md` — rules that may not be violated
5. `ROLES.md` — who may act, and when
6. `PROVENANCE_MODEL.md` — how traceability works

You do not need to memorize them.  
You need to know **which document answers which question**.

---

## 4. Declaring Your Role

Before acting in a workflow, identify **which role you are performing**.

Roles are defined normatively in `ROLES.md`.  
This guide does not redefine them.

A single person may occupy multiple roles across a workflow,  
but **never in a way that violates role separation invariants**.

If you are unsure, pause and check `ROLES.md` before proceeding.

---

## 5. Thinking in Artifacts

AWO requires a shift in how work is expressed.

| Instead of… | Do this… |
|------------|----------|
| “I’ll just explain what I did.” | Produce an artifact that records it |
| “This is obvious from context.” | Make the context explicit |
| “I fixed it quickly.” | Declare the change and its provenance |

If an action leaves no artifact, it is **methodologically invisible**.

This is intentional.

---

## 6. First Safe Exercise

To get comfortable without risk:

1. Create a mock **Initiation** artifact in `/examples/`
2. Declare a simple intent (one sentence is fine)
3. Explicitly state your role
4. Reference the governing documents you relied on

The goal is not correctness.

The goal is **traceability**.

---

## 7. Final Notes

AWO exists so research can be evaluated without trust in memory,
authority, or personal explanation.

Move slowly.
Write clearly.
Let artifacts do the talking.

If the process is visible, the science can be judged.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity · Governed under the Aurora Research Initiative (ARI)</sub>
</div>

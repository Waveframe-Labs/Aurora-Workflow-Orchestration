---
title: "AWO Onboarding Guide"
filetype: "documentation"
type: "guide"
version: "2.0.0"
status: "Active"
created: "2025-12-28"
updated: "2025-12-28"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting under explicit human direction, based on AWO normative documents. Verified against ARI Metadata Policy v2.0.0."
dependencies:
  - "AWO_OVERVIEW.md"
  - "SCOPE.md"
  - "WORKFLOW_SPEC.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "PROVENANCE_MODEL.md"
anchors:
  - "AWO-ONBOARDING-GUIDE-v2.0.0"
---

# AWO Onboarding Guide  
*How to begin working inside the Aurora Workflow Orchestration method layer*

---

## 1. What This Guide Is

This document is a **practical orientation for new contributors to AWO-governed research**.  
It does **not** define method, rules, enforcement, or governance — those live in the normative files.

This guide answers:

- Where do I start?
- What documents should I read first?
- How do artifacts and roles work in practice?
- How do I prepare to contribute using AWO?

If you understand this document, you should be able to **enter a workflow confidently without guessing**.

---

## 2. How AWO Operates at a High Level

AWO defines **how research is conducted**, not how results must turn out.

At its core:

> *A workflow is valid under AWO only if its artifacts, roles, and process are explicit, traceable, and auditable.*

There are three pillars to remember:

| Pillar | Meaning in practice |
|-------|---------------------|
| **Explicit Structure** | Workflow phases and transitions are not implied — they are declared. |
| **Artifact Authority** | Claims follow artifacts, never the reverse. |
| **Role Separation** | No self-review, no silent authority blending, no implicit decision-making. |

---

## 3. First Steps for a New Contributor

### Step 1 — Read the Core Documents  
*(order matters, because AWO builds upward)*

1. `AWO_OVERVIEW.md` — high-level purpose and position in Waveframe Labs.
2. `SCOPE.md` — what AWO governs and what it does not.
3. `WORKFLOW_SPEC.md` — workflow phases, transitions, required outputs.
4. `INVARIANTS.md` — the non-negotiable rules that must always hold.
5. `ROLES.md` — who can do what inside a workflow.
6. `PROVENANCE_MODEL.md` — how traceability and attribution are structured.

You do not need to memorize them — you only need to know **where truth lives**.

---

### Step 2 — Understand Your Role

Before participating, define *which role you are acting under*:

- **Initiator** — sets the problem
- **Contributor** — produces artifacts
- **Reviewer** — checks artifacts against requirements
- **Approver** — makes pass/fail decisions
- **Auditor** — validates traceability and compliance

The same person may occupy more than one — **but never in a way that breaks invariants**.

---

### Step 3 — Adopt the AWO Thinking Model

AWO requires contributors to think differently:

| Instead of… | You do… |
|-------------|---------|
| “I know the answer, let me write it.” | “I produce an artifact that supports the claim.” |
| “I’ll just fix this quickly.” | “I declare my role, scope, and artifact change.” |
| “Everyone knows what I meant.” | “Meaning is in the artifact — if it’s not written, it doesn’t exist.” |

This is not bureaucracy — it is **clarity under uncertainty**.

Workflows are **designed to be replayable and judged without context or memory of events**.

---

## 4. Minimum Bar to Contribute

A contribution is considered *ready for review* when:

- It is accompanied by the correct artifact type (e.g., `contribution`, `reasoning`, `review`).
- Role is declared explicitly.
- Scope is referenced or extended intentionally.
- The change can be audited without assumptions or chat history.
- No methodological invariant is violated.

If you can point to the artifact that justifies a claim — you are aligned.

---

## 5. Small First Assignment

To get comfortable:

1. Create a **mock workflow initiation artifact** inside `/examples/`
2. Write one sentence of reasoning for a hypothetical research question
3. Declare your role next to your change
4. Reference which documents governed your action

A good first goal:

> Produce something traceable, even if small.

Proof-of-method matters more than size.

---

## 6. Closing

Welcome to AWO.  
This system exists so research can **stand on evidence — not memory, authority, or trust**.  
You are encouraged to move slowly, write clearly, and let artifacts speak for themselves.

If you document the process, the science will follow.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity · Governed under the Aurora Research Initiative (ARI)</sub>
</div>

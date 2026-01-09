---
title: "Aurora Workflow Orchestration (AWO) — Overview"
filetype: "documentation"
type: "specification"
version: "2.0.0"
doi: "TBD-2.0.0"  
status: "Active"
created: "2025-12-22"
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
ai_assistance_details: "AI-assisted drafting with full human oversight; overview rewritten for clarity and boundary discipline following AWO v2 method lock."


dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "WORKFLOW_SPEC.md"
  - "ROLES.md"

anchors:
  - "AWO-OVERVIEW-v2.0.0"
---

# Aurora Workflow Orchestration (AWO) — Overview

## 1. Purpose

This document provides a **high-level orientation** to  
**Aurora Workflow Orchestration (AWO) v2.0.0**.

It exists to answer a simple question:

> *What is AWO, why does it exist, and how should it be understood within the Waveframe Labs ecosystem?*

This document is **descriptive**, not normative.  
All binding definitions, constraints, and requirements are specified in the
dedicated AWO specifications referenced throughout.

---

## 2. What AWO Is

AWO is a **methodological framework** for structuring reproducible,
AI-assisted research workflows.

It defines a shared method for:

- organizing research activity into explicit stages,
- requiring persistent artifacts for epistemically relevant actions,
- separating roles to preserve independence,
- enabling traceability across decisions, inputs, and transformations.

AWO governs **how work is recorded and structured**, not what conclusions are reached.

---

## 3. What AWO Is Not

AWO explicitly does **not**:

- execute workflows,
- evaluate scientific correctness,
- validate artifacts at runtime,
- define tooling, CI/CD, or infrastructure,
- enforce compliance.

Execution, validation, and enforcement are handled by downstream systems
(e.g., CRI-CORE and related tooling).

AWO is **method only**.

---

## 4. AWO’s Role in the Stack

Within the Waveframe Labs ecosystem, AWO occupies a **hinge position**.

- **Upstream**, it is constrained by governance, doctrine, and disclosure frameworks.
- **Downstream**, it provides structured inputs to enforcement engines,
  validators, publication tooling, and case-study research.

AWO does not replace governance or tooling.  
It connects them by making research workflows **legible and reconstructible**.

---

## 5. Reproducibility as a Structured Process

AWO treats reproducibility as a **procedural property**, not a reporting norm.

Rather than relying on post-hoc explanations, AWO requires that:

- epistemically relevant actions leave persistent artifacts,
- those artifacts are role-bound and traceable,
- downstream evaluation can occur without trust in the author.

Reproducibility emerges from **methodical structure**, not narrative authority.

---

## 6. Artifact-Centered Methodology

AWO is **artifact-first**.

Every meaningful action in a workflow is expected to result in
a persistent artifact that can be:

- referenced,
- inspected,
- reviewed,
- superseded without being silently altered.

If an action leaves no artifact, it is methodologically opaque.

---

## 7. Roles and Independence

AWO relies on **explicit role separation** to preserve epistemic independence.

Roles are:

- functional rather than institutional,
- declared per action rather than inferred,
- constrained to prevent self-review, self-approval, or self-attestation.

Role definitions and constraints are specified in the dedicated roles specification.
This document explains their purpose, not their rules.

---

## 8. Traceability and Falsifiability

AWO workflows are designed to support **challenge and reconstruction**.

A properly structured workflow should allow a third party to:

- identify inputs and assumptions,
- follow transformations and decisions,
- understand how outcomes were produced,
- determine how claims could be falsified or revised.

AWO does not judge correctness.  
It structures workflows so correctness *can be evaluated*.

---

## 9. Enforcement Boundary

AWO defines **methodological expectations**, not enforcement behavior.

Downstream systems may validate, block, attest, or automate,
but those mechanisms operate *on* AWO artifacts —
they are not defined *by* this document.

---

## 10. How to Use This Repository

This overview should be read as a **map**, not a rulebook.

To understand AWO in detail:
- consult scope and invariants for boundaries,
- review the workflow specification for structure,
- examine artifact classes and schemas for concrete expectations,
- refer to contract documentation for machine-readable projections.

This document exists to provide context and orientation,
not to restate normative specifications.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Aurora Workflow Orchestration (AWO)</sub>
</div>

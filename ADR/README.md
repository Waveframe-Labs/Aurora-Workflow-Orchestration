---
title: "AWO Architectural Decision Records — Overview"
filetype: "documentation"
type: "non-normative"
version: "2.0.0"  
doi: "TBD-2.0.0"  
status: "Active"
created: "2026-01-07"
updated: "2026-01-07"

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
ai_assistance_details: "AI-assisted drafting under human oversight; creates the ADR structure without making technical decisions."

dependencies:
  - "../SCOPE.md"
  - "../INVARIANTS.md"
  - "../WORKFLOW_SPEC.md"
  - "../ROLES.md"

anchors:
  - "AWO-ADR-README-v2.0.0"
---

# Architectural Decision Records (ADR) — Overview

This directory provides the **official location** for Architectural Decision Records (ADRs) used within  
**Aurora Workflow Orchestration (AWO) v2.0.0**.

ADRs capture **important decisions** that affect structure, direction, or constraints of this repository.  
They provide durable historical context that complements AWO’s artifact-first methodology.

This README is **non-normative**.  
It explains *how* ADRs are organized, not what decisions must be made.

---

## 1. What ADRs Are

ADRs document:

- A decision that affects architecture, structure, or methodology integration
- The context that led to the decision
- Options considered
- Why the final choice was made
- Consequences and follow-up requirements

An ADR **does not define AWO method**.  
It records decisions made when applying AWO to this repository.

---

## 2. When to Create an ADR

Create an ADR when:

- A structural choice affects multiple files or systems
- A rule from SCOPE / INVARIANTS / WORKFLOW_SPEC needs explicit application
- A change has long-term consequences
- A decision might need justification in future audits

Do **NOT** create ADRs for:

- Typographical edits  
- Metadata normalization  
- Simple refactoring  
- Content corrections aligned with existing specs  

Only decisions that **change direction** or **commit to one of several viable paths** belong here.

---

## 3. ADR Lifecycle

ADRs follow a simple lifecycle:

```
proposed → accepted → superseded → deprecated
```

- **Proposed** — Under discussion
- **Accepted** — Active decision
- **Superseded** — Replaced by a new ADR
- **Deprecated** — Historically relevant but no longer applies

---

## 4. Directory Structure

```
/ADR
├── README.md # This file
└── template.md # Boilerplate for new ADRs
```

ADRs will be named sequentially:

```
ADR-001-title.md
ADR-002-title.md
```

---

## 5. Relationship to AWO Method

ADRs are **subordinate** to the normative method layer:

- `SCOPE.md`  
- `INVARIANTS.md`  
- `ROLES.md`  
- `WORKFLOW_SPEC.md`  

If an ADR contradicts these documents, the ADR is invalid.

ADRs document **choices**, not **rules**.

---

<p align="center"><sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity</sub></p>

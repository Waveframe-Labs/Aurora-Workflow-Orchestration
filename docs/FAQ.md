---
title: "AWO — Frequently Asked Questions"
filetype: "documentation"
type: "non-normative"
version: "2.0.0"
doi: "TBD-2.0.0"  
status: "Active"
created: "2025-12-28"
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
ai_assistance_details: "AI-assisted drafting with human oversight; content constrained to explanatory guidance and aligned with AWO v2.0.0 normative documents."

dependencies:
  - "OVERVIEW.md"
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_SCHEMA_MAP.md"

anchors:
  - "AWO-FAQ-v2.0.0"
---

# AWO — Frequently Asked Questions

This FAQ answers common questions when first interacting with  
**Aurora Workflow Orchestration (AWO)**.

It is **non-normative and explanatory only**.  
All methodological authority resides in the AWO specification documents.

---

## 1. What is AWO in simple terms?

AWO is a **method for conducting research in a way that remains reconstructible and auditable**.

It defines:
- which workflow phases exist,
- which artifacts must be produced,
- how roles are separated,
- what makes a process traceable and falsifiable.

It does **not** run workflows, validate artifacts, or enforce compliance.

---

## 2. How is AWO different from CRI-CORE?

| AWO | CRI-CORE |
|----|---------|
| Defines methodology | Enforces methodology |
| Human-readable governance | Machine-addressable validation |
| Specifies required artifacts | Checks artifact presence and structure |
| Cannot block workflows | May block workflows (downstream) |

This repository defines **method only**.  
Enforcement tooling is intentionally out of scope.

---

## 3. Is AWO a software tool?

No.

AWO is **not an application, platform, or CI system**.  
It is a **methodological standard** that tools may implement.

---

## 4. Can one person participate in a workflow alone?

Only if **role separation invariants are preserved**.

A single person may act in multiple roles **across time**,  
but must not approve, audit, or validate their own work.

Role constraints are defined normatively in `ROLES.md`.

---

## 5. What happens if a required artifact is missing?

Under AWO, the workflow is **methodologically invalid**.

Results may still exist, but they do **not qualify as reproducible AWO outputs**  
because the process cannot be independently reconstructed.

---

## 6. Does AWO require traditional peer review?

No.

AWO replaces reliance on authority with **artifact-based auditability**.  
External peer review is optional and compatible, but not required.

Falsifiability replaces trust.

---

## 7. Do contributors need to understand the entire system?

No — but they must understand:

1. Which role they are acting under
2. Which artifact they are producing
3. How to reference governing documents
4. How to preserve traceability

Deep governance knowledge is not required to contribute responsibly.

---

## 8. Where should I start when joining a project?

A recommended order:

1. `OVERVIEW.md`
2. `ROLES.md`
3. `WORKFLOW_SPEC.md`
4. Review examples in `/examples/`
5. Make a small, well-scoped first contribution

Learning by producing traceable artifacts is encouraged.

---

## 9. Can AWO be used outside Waveframe Labs?

Yes.

AWO is designed to be **open, portable, and institution-agnostic**,  
subject to license and citation requirements.

---

## 10. Is AI participation allowed?

Yes — with disclosure.

AI assistance must be:
- explicitly declared,
- attributable,
- and paired with human decision ownership.

AI may influence content; it may not replace accountability.

---

## 11. What counts as a reproducible result under AWO?

A result is reproducible if:

- all required artifacts exist,
- the workflow can be reconstructed,
- inputs and reasoning are traceable,
- falsifiability conditions are declared.

Reproducibility is a property of **process**, not correctness.

---

## 12. What if documents disagree?

Authority resolves as follows:

1. `SCOPE.md`
2. `INVARIANTS.md`
3. `ROLES.md`
4. `WORKFLOW_SPEC.md`
5. Contract documents under `/contracts/`
6. Non-normative docs (FAQ, guides)

Non-normative documents never override specifications.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity</sub>
</div>

---
title: "AWO — Frequently Asked Questions"
filetype: "documentation"
type: "non-normative"
version: "2.0.0"
status: "Active"
created: "2025-12-28"
updated: "2025-12-28"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "Draft generated AI-assisted with human oversight, aligned to AWO v2.0.0 normative documents."
anchors:
  - "AWO-FAQ-v2.0.0"
dependencies:
  - "../AWO_OVERVIEW.md"
  - "../INVARIANTS.md"
  - "../ROLES.md"
  - "../WORKFLOW_SPEC.md"
  - "../ARTIFACT_CLASSES.md"
  - "../ARTIFACT_REQUIREMENTS.md"
---

# AWO — Frequently Asked Questions

This FAQ clarifies common questions when first interacting with  
**Aurora Workflow Orchestration (AWO)**.

It is **non-normative** and explanatory only.  
Normative authority is held exclusively by the AWO root specification files.

---

## **1. What *is* AWO in simple terms?**

AWO is a **method for doing research reproducibly.**
It defines:

- which artifacts must exist,
- how roles interact,
- how workflows progress,
- what makes work auditable and falsifiable.

It **does not run the workflow** or enforce rules — that is the job of later layers.

---

## **2. How is AWO different from CRI-CORE?**

| AWO | CRI-CORE |
|-----|----------|
| Defines *methodology* | Executes and *enforces* methodology |
| Human-readable governance | Machine-addressable enforcement |
| Requires artifacts | Validates artifacts |
| Cannot block workflows | Can block workflows |

AWO says **what must exist**, CRI-CORE will later verify **whether it does**.

---

## **3. Is AWO a software tool?**

**No.**

AWO is **not a product, engine, or CI system**.
It is a **methodological standard** that tools *implement*.

---

## **4. Can one person run a workflow alone?**

Only if **role separation invariants are preserved**.

A single human can occupy multiple roles **sequentially**, not simultaneously.
They may contribute, but **cannot approve or audit their own work.**

Approval or audit must come from an independent actor.

---

## **5. What happens if a required artifact is missing?**

The workflow is **methodologically invalid** under AWO.

It may still produce results, but **those results do not count as reproducible research outputs** in the AWO ecosystem.

---

## **6. Does AWO require formal peer review?**

No.  
AWO replaces peer review with **artifact-based audit pathways**.

External review is optional, not required — **falsifiability replaces authority.**

---

## **7. Do contributors need to understand the whole system?**

They must understand:

1. **How to declare roles**
2. **How to produce required artifacts**
3. **How to maintain traceability**

They do *not* need deep expertise in internal governance to participate.

---

## **8. Where should I start when joining a project?**

1. Read `AWO_OVERVIEW.md`  
2. Review `ROLES.md`  
3. Check examples under `/contracts/examples/`  
4. Submit first contribution as a **small, scoped change**

Learning by doing is preferred.

---

## **9. Can AWO be used outside Waveframe Labs?**

Yes.  
The design goal is broad reproducibility: **open, portable, institution-agnostic.**

Other groups may adopt or fork AWO as long as citations remain intact.

---

## **10. Is AI participation allowed?**

Yes — with conditions.

AI-assisted content **must be attributed in metadata**,  
and ownership of decisions must be clearly human-declared.

AI cannot replace human accountability.

---

## **11. What counts as a reproducible result?**

A workflow is reproducible if:

- all required artifacts exist,
- another actor can rerun the process,
- reasoning and inputs are traceable,
- falsifiability conditions are declared.

Reproducibility is a property of **process**, not outcome.

---

## **12. What happens if two documents disagree?**

Authority resolves as:

1. **SCOPE.md**
2. **INVARIANTS.md**
3. **ROLES.md**
4. **WORKFLOW_SPEC.md**
5. Supporting documentation (e.g., FAQ, Guides)

Normative docs always override non-normative ones.

---

## Compliance

This document is valid only while metadata remains compliant with  
**ARI Metadata Policy v2.0.0**.

---

<p align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity</sub>
</p>


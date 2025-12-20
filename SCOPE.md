---
title: "AWO Scope Definition"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2025-12-20"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight, validation against ARI Metadata Policy v2.0.0, and final approval by the maintainer."
dependencies:
  - "ARI Metadata Policy v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-SCOPE-v2.0.0"
---

# AWO Scope Definition

## 1. Purpose

This document defines the **authoritative scope** of **Aurora Workflow Orchestration (AWO) v2.0.0**.

It specifies:
- what AWO governs,
- what AWO explicitly does not govern, and
- the boundaries that prevent scope, governance, or enforcement creep.

This document is **normative**.

---

## 2. In-Scope (Governed by AWO)

AWO governs **methodology only**.

Specifically, AWO defines:

- The abstract structure of AI-assisted research workflows  
- The required logical phases of compliant research workflows  
- The separation of roles within research workflows, as constrained by the Role Separation Charter  
- The required classes of research artifacts and their conceptual relationships  
- Methodological constraints necessary for auditability and reproducibility  
- Conditions under which research outputs may be considered **methodologically valid**

AWO is concerned with **how research must be structured**, not how it is executed.

---

## 3. Out-of-Scope (Not Governed by AWO)

AWO explicitly does **not** govern:

- Execution engines or runtime systems  
- Automation tooling, CI/CD pipelines, or workflow runners  
- Enforcement mechanisms or compliance validation  
- Attestation generation, verification, or identity binding  
- Cryptographic operations, signing, or key management  
- File formats, storage layouts, or databases  
- AI model selection, orchestration strategies, or prompting logic  
- Organizational policy, institutional law, or epistemic doctrine  

Any document, code, or system performing these functions is **outside the scope of AWO**, regardless of historical association or naming.

---

## 4. Governance and Authority Boundaries

AWO operates under upstream governance and epistemic authority and introduces **no independent law**.

- **Metadata validity** is governed exclusively by the ARI Metadata Policy.
- **Role authority and separation** are governed exclusively by the Role Separation Charter.
- **Epistemic constraints** are governed by Neurotransparency doctrine and standards.
- **Enforcement and execution** are delegated to downstream systems (e.g., CRI-CORE).

AWO MUST NOT:
- enforce governance,
- implement enforcement logic,
- adjudicate scientific truth,
- or override upstream policy.

---

## 5. Normative Authority

Only documents explicitly listed as authoritative in `awo.manifest.json` and `DOCUMENT_REGISTRY.md` may define or extend AWO methodology.

Archived materials, historical implementations, and legacy documents are **non-normative** and MUST NOT be used to infer scope or authority.

---

## 6. Scope Stability

Changes to this document constitute a **breaking methodological change** and require:

- a major version increment,
- explicit documentation of scope impact,
- and preservation of backward traceability.

Minor and patch versions MUST NOT expand scope.

---

## 7. Compliance Requirement

This document is institutionally valid only if its metadata block complies with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this document as an authoritative AWO artifact.

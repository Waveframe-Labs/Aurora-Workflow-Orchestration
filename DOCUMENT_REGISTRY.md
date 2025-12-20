---
title: "AWO Document Registry"
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
ai_assistance_details: "AI-assisted drafting with full human oversight, aligned to AWO Scope, Invariants, Roles, and Workflow Specification, and validated against ARI Metadata Policy v2.0.0."
dependencies:
  - "AWO Scope Definition v2.0.0"
  - "AWO Methodological Invariants v2.0.0"
  - "AWO Workflow Roles v2.0.0"
  - "AWO Workflow Specification v2.0.0"
  - "ARI Metadata Policy v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-DOCUMENT-REGISTRY-v2.0.0"
---

# AWO Document Registry

## 1. Purpose

This document defines the **authoritative registry of normative documents** for
**Aurora Workflow Orchestration (AWO) v2.0.0**.

It enumerates which documents are authoritative, what each document governs,
and the boundaries of their authority.

This document is **normative**.

---

## 2. Normative Document Set

The following documents constitute the **complete normative specification**
of AWO v2.0.0.

No document outside this set may define, extend, or modify AWO methodology.

---

### D-1 — `SCOPE.md`

**Title:** AWO Scope Definition  
**Governs:** Methodological scope and authority boundaries  
**Status:** Normative  
**Version:** 2.0.0  

---

### D-2 — `INVARIANTS.md`

**Title:** AWO Methodological Invariants  
**Governs:** Non-negotiable methodological constraints  
**Status:** Normative  
**Version:** 2.0.0  

---

### D-3 — `ROLES.md`

**Title:** AWO Workflow Roles  
**Governs:** Workflow-level role semantics and responsibilities  
**Status:** Normative  
**Version:** 2.0.0  

---

### D-4 — `WORKFLOW_SPEC.md`

**Title:** AWO Workflow Specification  
**Governs:** Abstract workflow phases, transitions, and artifact classes  
**Status:** Normative  
**Version:** 2.0.0  

---

### D-5 — `DOCUMENT_REGISTRY.md`

**Title:** AWO Document Registry  
**Governs:** Enumeration and authority mapping of AWO normative documents  
**Status:** Normative  
**Version:** 2.0.0  

---

## 3. Non-Normative Materials

The following categories are **explicitly non-normative**:

- Historical documents and archived branches
- Implementation examples or reference workflows
- Tooling, automation, or enforcement code
- Diagrams, figures, and explanatory notes
- Website content and external summaries

Non-normative materials MUST NOT be used to infer or override AWO methodology.

---

## 4. Authority Resolution

In the event of conflict:

1. **ARI governance documents** prevail over AWO documents.
2. **AWO documents** prevail over downstream tooling or case studies.
3. Within AWO, authority is resolved in the following order:
   - `SCOPE.md`
   - `INVARIANTS.md`
   - `ROLES.md`
   - `WORKFLOW_SPEC.md`
   - `DOCUMENT_REGISTRY.md`

Later documents MUST be interpreted consistently with earlier ones.

---

## 5. Registry Stability

Changes to the normative document set REQUIRE:
- explicit modification of this registry,
- major version increment if scope or authority changes,
- preservation of backward traceability.

Adding, removing, or redefining a normative document is a governance action.

---

## 6. Compliance Requirement

This document is institutionally valid only if its metadata block complies
with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

---  

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

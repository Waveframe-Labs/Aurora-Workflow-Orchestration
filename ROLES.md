---
title: "AWO Workflow Roles"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2025-12-27"
author: "Waveframe Labs"
maintainer: "Shawn C. Wright"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight, aligned to the Role Separation Charter v1.1.1 and ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "WORKFLOW_SPEC.md"
  - "ARI Metadata Policy v2.0.0"
  - "Role Separation Charter v1.1.1"
anchors:
  - "AWO-ROLES-v2.0.0"
---

# AWO Workflow Roles

## 1. Purpose
This document defines **workflow-level functional roles** within
**Aurora Workflow Orchestration (AWO) v2.0.0** and establishes **constraints
governing who may perform which methodological actions**.

Roles define responsibility, **not authority** — authority remains upstream
in ARI governance.

This document is **normative**.

---

## 2. Role Model Principles

- Roles are functional, assigned on action — not identity or job title.
- Role assumption MUST be **declared**, not inferred.
- A single actor MAY hold multiple roles **only if invariants are preserved**.
- No role may implicitly inherit permissions of another role.
- Governance authority and enforcement authority are **out of scope here**.

---

## 3. Workflow Roles (Canonical)

### R-1 — Workflow Initiator
Responsibilities:
- Define problem, intent, and starting assumptions.
- Register workflow as AWO-compliant.
- Produce initiation record.

Constraints:
- MUST NOT review, approve, or audit workflow results.
- MUST NOT perform final decision actions.

---

### R-2 — Contributor
Responsibilities:
- Generate research artifacts and reasoning.
- Perform derivations, synthesis, modeling, or experimentation.
- Submit outputs for review.

Constraints:
- MUST NOT approve or audit artifacts they created.
- MAY revise artifacts only through documented change logs.
- MUST reference inputs and justify transformations.

---

### R-3 — Reviewer
Responsibilities:
- Evaluate artifacts against scope + evaluation criteria.
- Produce review reports and issue registers.

Constraints:
- MUST be independent of contribution context.
- MUST NOT approve artifacts they reviewed **if also contributor**.
- Review confirms sufficiency — **not scientific correctness**.

---

### R-4 — Approver
Responsibilities:
- Decide if the workflow satisfies required criteria.
- Issue approval or rejection decision records.

Constraints:
- MUST NOT be the contributor of approved artifacts.
- MUST base decisions on artifacts — not narrative claims.

---

### R-5 — Auditor
Responsibilities:
- Assess invariant compliance and traceability.
- Verify reconstructibility and metadata integrity.
- Produce audit report.

Constraints:
- MUST be role-independent from Initiator + Contributor.
- MUST NOT modify artifacts, only observe + report.

---

## 4. Role Interaction Constraints (Hard Law)

- ❌ Self-review is prohibited.
- ❌ Self-approval is prohibited.
- ❌ A single actor MAY NOT approve artifacts they contributed.
- ❌ Audit may not be performed by contributor or approver.
- ❌ Undeclared role assumption invalidates resulting artifacts.

Any violation renders workflow **methodologically invalid**.

---

## 5. Phase-Role Matrix (Normative Table)

| Phase | Allowed Roles | Forbidden Roles |
|---|---|---|
| Initiation | Initiator | Reviewer/Approver/Auditor |
| Scoping | Initiator, Contributor | Approver/Auditor |
| Contribution | Contributor | Approver/Auditor |
| Review | Reviewer | Contributor for same artifact |
| Approval | Approver | Contributor/Reviewer for same artifact |
| Audit | Auditor | Contributor/Approver |

---

## 6. Role Escalation & Multi-Role Rules

Escalation requires **explicit declaration** and MUST follow:
```  
Initiator → Contributor → Reviewer → Approver → Auditor
```  
(One direction only, no backward collapse)  

A single person **may occupy multiple roles sequentially**, **but never concurrently
within the same artifact lineage**.

If roles conflict, **inactive role must be explicitly set aside**.

---

## 7. Neurotransparency Alignment

All roles MUST include attribution sufficient for NTS compliance:

- who acted,
- under what role,
- based on what reasoning,
- using which cognitive agents (AI/Human/Both),
- traceable to commit or artifact.

---

## 8. Compliance & Invalidity

Non-compliance with this specification invalidates workflow status.
Remediation requires:

1. new artifact superseding invalid one,
2. updated provenance chain,
3. audit documenting correction.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

---
title: "AWO Workflow Roles"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2026-01-04"

author:
  name: "Shawn C. Wright"
  email: "swright@waveframelabs.org"

maintainer:
  name: "Waveframe Labs"
  url: "https://waveframelabs.org"

license: "Apache-2.0"

copyright:
  holder: "Waveframe Labs"
  year: "2026"

ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight; revised to align with AWO v2 Design Envelope, Minimal Phase Topology, and Role Separation Charter v1.1.1."  

dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "PHASE_TOPOLOGY.md"
  - "Role Separation Charter v1.1.1 (ARI concept DOI)"

anchors:
  - "AWO-ROLES-v2.0.0"
---


# AWO Workflow Roles

## 1. Purpose

This document defines **workflow-level functional roles** within  
**Aurora Workflow Orchestration (AWO) v2.0.0** and establishes **constraints
governing who may perform which methodological actions**.

Roles define **responsibility**, not authority.

All epistemic authority, approval, adjudication, and enforcement remain
**explicitly outside AWO scope** and are governed by upstream or downstream layers.

This document is **normative** with respect to AWO methodology.

---

## 2. Role Model Principles

- Roles are **functional**, assigned per action — not titles or identities.
- Role assumption MUST be **explicitly declared**, never inferred.
- A single actor MAY hold multiple roles **only if invariants are preserved**.
- No role implicitly inherits permissions from another role.
- Governance authority and enforcement authority are **out of scope** here.

---

## 3. Workflow Roles (Canonical, v2)

### R-1 — Workflow Initiator

**Responsibilities**
- Declare intent and scope of an intentional unit of work.
- Register workflow as AWO-governed.
- Produce the Initiation Artifact.

**Constraints**
- MUST NOT review or curate artifacts produced downstream.
- MUST NOT assert approval, legitimacy, or correctness.

---

### R-2 — Contributor

**Responsibilities**
- Produce Specification and Execution artifacts.
- Perform derivation, synthesis, modeling, or experimentation.
- Declare inputs, tools, and transformations.

**Constraints**
- MUST NOT review artifacts they contributed to.
- MUST NOT curate the final Release Artifact.
- MUST document revisions through new artifacts, not mutation.

---

### R-3 — Reviewer

**Responsibilities**
- Examine artifacts for structural completeness and declared criteria.
- Record observations, concerns, and findings in Review Artifacts.

**Constraints**
- MUST be independent of the contribution context for the reviewed artifact.
- MUST NOT assert approval, rejection, or legitimacy.
- Review confirms **methodological sufficiency**, not scientific truth.

---

### R-4 — Release Curator

**Responsibilities**
- Assemble the Release Artifact.
- Enumerate included artifacts.
- Declare release context and intended audience.

**Constraints**
- MUST NOT modify upstream artifacts.
- MUST NOT assert approval, legitimacy, or correctness.
- Acts solely as a **freezing and bundling function**.

---

## 4. Role Interaction Constraints (Methodological Law)

- ❌ Self-review is prohibited.
- ❌ Review of an artifact by its contributor is prohibited.
- ❌ Release curation by a contributor or reviewer of included artifacts is prohibited.
- ❌ Undeclared role assumption invalidates resulting artifacts.

Any violation renders the workflow **structurally non-compliant under AWO**
and may be acted upon by downstream governance or enforcement systems.

---

## 5. Phase–Role Matrix (Normative)

| Phase | Allowed Roles | Forbidden Roles |
|---|---|---|
| Initiation | Initiator | Reviewer, Curator |
| Specification | Initiator, Contributor | Reviewer |
| Execution | Contributor | Reviewer, Curator |
| Review | Reviewer | Contributor (same artifact) |
| Release | Curator | Contributor, Reviewer |

---

## 6. Multi-Role & Escalation Rules

A single actor MAY occupy multiple roles **sequentially**, but never
**concurrently within the same artifact lineage**.

Permitted escalation path:

```
Initiator → Contributor → Reviewer → Curator
```

Backward collapse or concurrent role execution is prohibited.

If a role transition occurs, the prior role MUST be explicitly relinquished.

---

## 7. Neurotransparency Alignment

All role actions MUST be attributable in compliance with NTS requirements,
including:

- who acted,
- under which role,
- using which cognitive agents (human / AI / hybrid),
- traceable to an artifact or commit.

AWO records **that reasoning occurred**, not whether it was correct.

---

## 8. Compliance & Invalidity

Non-compliance with this specification renders the workflow
**methodologically invalid under AWO**.

Remediation requires:
1. creation of superseding artifacts,
2. preserved provenance chains,
3. downstream evaluation if authority-bearing action is required.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

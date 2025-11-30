# Aurora Research Initiative (ARI)
## Role Separation Charter (v1.0.0)

**Author:** Shawn C. Wright  
**Affiliation:** Waveframe Labs — Independent Open-Science Research Entity  
**ORCID:** 0009-0006-6043-9295  
**Creation Date:** 2025-11-27  
**Concept DOI:** https://doi.org/10.5281/zenodo.17743096  

---
title: "Role Separation Charter"
version: "1.0.0"
status: "Final"
created: "2025-11-27"
type: "governance"  
doi: "10.5281/zenodo.17743096"  
author: "ARI Institutional Coordinator"
dependencies:
  - "ARI_BOUNDARIES_AND_RESPONSIBILITIES.md"
  - "METHOD_CONSTRAINTS.md"
  - "TOOLING_CONSTRAINTS.md"
  - "EPISTEMIC_DOCTRINE.md"
anchors:
  - "ARI-ROLE-SEPARATION-CHARTER-v1.0.0"
---  

This charter establishes the formal separation of roles, authorities, and responsibilities across the Aurora ecosystem. It defines the governance hierarchy and institutional boundaries that prevent role bleeding, ensure stability, and provide a long-term organizational structure.  
This document uses the **Hybrid Model (Option C)**: a minimal set of current active roles with defined *future governance bodies* reserved, enabling institutional growth without rewriting the charter.

---

# 1. Purpose

The purpose of this charter is to:

- define the distinct roles within ARI, AWO, CRI-CORE, Waveframe Labs, and Case Studies  
- ensure strict separation of powers  
- prevent authority overlap  
- establish long-term organizational stability  
- provide a structure for future councils and auditors  
- protect the ecosystem from governance drift  

This document is binding on all contributors and governance bodies.

---

# 2. Active Roles (Present-Day)

These roles exist **now**, and hold explicit authority today.

## 2.1 ARI Institutional Coordinator (IC)
**Scope:**  
- highest governance authority  
- approves governance changes  
- maintains epistemic doctrine  
- oversees all constitutional documents  
- ensures role separation compliance  
- enforces metadata and provenance policy  

**Prohibitions:**  
- may not act as AWO or CRI maintainer  
- may not approve changes without log entries  
- may not influence execution or method logic  

---

## 2.2 AWO Lead Maintainer
**Scope:**  
- maintains method logic  
- oversees workflow architecture  
- ensures compliance with Method Constraints  
- implements reproducible reasoning and metadata capture  

**Prohibitions:**  
- may not modify ARI doctrine  
- may not implement enforcement logic  
- may not perform epistemic validation  

---

## 2.3 CRI-CORE Lead Maintainer
**Scope:**  
- maintains deterministic execution engine  
- enforces identity, integrity, and reproducibility  
- implements attestation independence  

**Prohibitions:**  
- may not interpret workflow meaning  
- may not alter method logic  
- may not modify governance or doctrine  

---

## 2.4 Waveframe Labs Maintainer
**Scope:**  
- develops engineering projects under ARI rules  
- maintains AWO/CRI repositories and case studies  
- implements demos, tooling, and applied systems  

**Prohibitions:**  
- may not modify ARI doctrine  
- may not override governance constraints  

---

## 2.5 Case Study Maintainers
**Scope:**  
- run applied research using AWO + CRI  
- generate reproducible outputs  
- maintain domain-specific repositories  

**Prohibitions:**  
- may not alter method, tooling, or governance  
- may not modify AWO or CRI behavior  

---

# 3. Reserved Future Roles (Inactive but Defined)

These roles **do not exist yet**, but their definitions are locked into the charter to avoid structural rewrites.

## 3.1 ARI Governance Council (Future)
**Purpose:**  
Collective governance body responsible for doctrine updates, epistemic policy, and oversight.

---

## 3.2 AWO Method Council (Future)
**Purpose:**  
Reviews workflow architecture, proposes method revisions, ensures compliance with ARI doctrine.

---

## 3.3 CRI Integrity Council (Future)
**Purpose:**  
Oversees attestation rules, deterministic enforcement, and tooling compliance.

---

## 3.4 Audit & Compliance Officer (Future)
**Purpose:**  
Independent reviewer ensuring governance adherence across repos, workflows, and releases.

---

## 3.5 External Reviewers (Future, Read-Only)
**Purpose:**  
Academic or professional third parties with observational access to governance processes.

---

# 4. Separation of Powers

The following table defines strict boundaries:

| Role | Can Modify | Cannot Modify |
|------|------------|----------------|
| **ARI IC** | governance, doctrine | AWO logic, CRI enforcement |
| **AWO Lead** | workflow logic | ARI doctrine, CRI engine |
| **CRI Lead** | deterministic engine | ARI doctrine, AWO logic |
| **Labs Maintainer** | engineering tools, demos | ARI, AWO, CRI core rules |
| **Case Study Maintainer** | applied research | core system logic |

These boundaries are absolute.

---

# 5. Forbidden Role Interactions

The following interactions constitute governance violations:

- self-approval of governance changes  
- cross-role modification without authority  
- silent or undocumented updates  
- Labs modifying AWO or CRI core behavior  
- CRI interpreting method logic  
- AWO performing enforcement  
- Case Studies altering upstream systems  
- ARI engaging in execution or method design  

These clauses protect long-term institutional integrity.

---

# 6. Authority Hierarchy

Ordered from highest to lowest:

1. **ARI Institutional Coordinator**  
2. **(Future) ARI Governance Council**  
3. **AWO Lead Maintainer**  
4. **CRI Lead Maintainer**  
5. **Waveframe Labs Maintainer**  
6. **Case Study Maintainers**  

No lower role may override a higher one.

---

# 7. Revision Rules

All revisions require:

1. Approval by ARI IC  
2. Governance log entry  
3. Formal version increment  
4. Backward linkage  
5. Rationale included  

No silent changes permitted.

---  
<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>  


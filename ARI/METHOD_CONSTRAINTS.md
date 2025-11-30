# Aurora Research Initiative (ARI)
## Method Constraints (v1.0.0)

**Author:** Shawn C. Wright  
**Affiliation:** Waveframe Labs — Independent Open-Science Research Entity  
**ORCID:** 0009-0006-6043-9295  
**Creation Date:** 2025-11-27  
**Concept DOI:** https://doi.org/10.5281/zenodo.17743096  

---
title: "Method Constraints"
version: "1.0.0"
status: "Final"
created: "2025-11-27"
type: "governance"  
doi: "10.5281/zenodo.17743096"  
author: "ARI Institutional Coordinator"
dependencies:
  - "ARI_BOUNDARIES_AND_RESPONSIBILITIES.md"
  - "EPISTEMIC_DOCTRINE.md"
  - "METADATA_POLICY.md"
anchors:
  - "ARI-METHOD-CONSTRAINTS-v1.0.0"
---  

This document establishes the binding constraints and required capabilities governing the Aurora Workflow Orchestration (AWO) framework. It defines the responsibilities, prohibitions, and operational boundaries that AWO must adhere to under the authority of the Aurora Research Initiative (ARI). These constraints ensure long-term reproducibility, governance stability, and epistemic integrity.

---

# 1. Purpose

The purpose of this document is to:

- define the mandatory capabilities AWO must implement  
- prevent method-level overreach into governance or deterministic execution  
- ensure compliance with ARI doctrine  
- provide a clear contract for future contributors  
- guarantee reproducibility and interpretability  
- ensure method-level integrity under CRI-CORE enforcement  

This document is binding for all versions and implementations of AWO.

---

# 2. Required Capabilities of AWO

The following capabilities are required for AWO to remain ARI-compliant:

## 2.1 Metadata Capture
AWO must:
- extract metadata from all workflow steps  
- propagate metadata to outputs  
- ensure all artifacts produced include ARI-compliant metadata blocks  
- validate metadata presence before proceeding to subsequent steps  

## 2.2 Reasoning Traceability
AWO must:
- expose full reasoning chains  
- maintain step-level interpretability  
- avoid implicit or hidden reasoning transitions  
- record intermediate states in a reviewable format  

## 2.3 Reproducibility
AWO must:
- ensure workflows can be re-executed under equivalent conditions  
- document environment and runtime dependencies  
- maintain deterministic intent (even before CRI enforcement)  
- avoid reliance on transient or untracked external state  

## 2.4 Logging and Process Transparency
AWO must:
- record all workflow steps  
- log state transitions and inputs  
- produce human-readable audit trails  
- avoid silent branches or undocumented behavior  

## 2.5 CRI-CORE Compatibility
AWO must:
- operate correctly when executed under CRI-CORE  
- expose workflow structure in a form CRI can enforce deterministically  
- avoid embedding logic that conflicts with engine-level boundaries  

## 2.6 Epistemic Compliance
AWO must:
- comply with ARI Epistemic Doctrine  
- support falsifiability through clear reasoning chains  
- avoid introducing unfalsifiable processes  
- ensure all outputs are traceable to documented steps  

---

# 3. Explicit Prohibitions

The following actions and behaviors are strictly forbidden for AWO:

## 3.1 Epistemic Overreach
AWO may **not**:
- define or modify epistemic doctrine  
- interpret scientific truth or correctness  
- override epistemic rules defined by ARI  

AWO implements procedures; it does not define knowledge.

## 3.2 Governance Overreach
AWO may **not**:
- modify ARI governance documents  
- approve its own changes  
- bypass governance logs or metadata obligations  
- collapse governance and execution into one role  

## 3.3 Deterministic Enforcement
AWO may **not**:
- embed deterministic execution logic  
- perform attestation or identity-binding  
- override CRI-CORE enforcement behavior  

Determinism is the domain of CRI-CORE, not AWO.

## 3.4 Method Engine Collapse
AWO may **not**:
- perform engine-level validation  
- interpret or enforce workflow correctness  
- embed execution engine capabilities  
- self-modify during execution  

## 3.5 Provenance Violations
AWO may **not**:
- produce metadata-incomplete artifacts  
- bypass provenance requirements  
- silently modify workflow structures  

---

# 4. Cross-Layer Boundaries

## 4.1 AWO → ARI
AWO must follow ARI doctrine and governance rules.  
AWO may not modify, override, or conditionally reinterpret any ARI rule.

## 4.2 AWO → CRI-CORE
AWO must produce workflows compatible with CRI-CORE enforcement.  
AWO may not embed deterministic behavior or identity logic.

## 4.3 AWO → Waveframe Labs
AWO may be extended or adapted by Waveframe Labs only under ARI governance rules.  
Labs may not modify AWO in ways that violate constraints defined here.

## 4.4 AWO → Case Studies
Case Studies must use AWO without modifying its governance-scope responsibilities.  
Case Studies may not embed AWO logic within their own domain.

---

# 5. Revision Rules

All revisions to this document require:

1. Approval by the ARI Institutional Coordinator  
2. A governance log entry  
3. A version increment  
4. Backward linkage to previous versions  
5. A rationale included in the log  

No silent changes permitted.
---  
<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>  


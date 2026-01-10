---
title: "AWO v2.0.0 Changelog"
filetype: "documentation"
type: "non-normative"
version: "2.0.0"
doi: "10.5281/zenodo.18201829"
status: "Active"
created: "2026-01-07"
updated: "2026-01-09"

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
ai_assistance_details: "AI-assisted structuring and validation under human oversight; all change entries reviewed and approved by maintainer."

dependencies:
  - "./README.md"

anchors:
  - "AWO-CHANGELOG-v2.0.0"
---

# CHANGELOG — Aurora Workflow Orchestration (AWO) v2.0.0

## 2.0.0 — 2026-01-07
### Summary
Formalization and stabilization of the AWO methodology layer. All v1.x materials archived. Contract surface finalized. Schema suite completed and validated. Supporting documentation rewritten to align with the locked AWO v2.0.0 design envelope.

### Added
- Root-level CITATION.cff (initial version, pre-DOI freeze)
- Root-level LICENSE (Apache 2.0)
- SECURITY.md (minimal coordinated disclosure policy)
- ADR/README.md + ADR/template.md
- method/README.md
- contracts/schemas/README.md
- Revised onboarding guide (`docs/ONBOARDING_GUIDE.md`)
- Revised FAQ (`docs/FAQ.md`)
- New example initiation artifact aligned to schema

### Revised
- AWO_OVERVIEW.md (complete rewrite; non-normative summary)
- PROVENANCE_MODEL.md (aligned with schema + enforcement logic)
- NEUROTRANSPARENCY.md (integration-only routing, non-doctrinal)
- GLOSSARY.md (all terminology validated against locked method)
- contracts/README.md (clarified authority + boundaries)
- Root README.md (structure, badges, footer, canonical links)

### Removed / Deleted
- DESIGN_LAWS.md (obsolete under v2 invariants)
- DOCUMENT_REGISTRY.md (replaced by contract index)
- awo.scope.example.json (deprecated example no longer schema-valid)

### Archived
- Entire `v1-archived/` directory preserved unchanged

### Structural Changes
- Established canonical metadata block for AWO v2.0.0
- Standardized document classification: normative vs non-normative
- Locked workflow phase topology
- Locked contract authority model
- Locked schema map and artifact class definitions

### Pending Finalization
- DOI assignment (will be added to CITATION.cff post-release)
- Metadata normalization pass across entire repo (mechanical)
- CRI-CORE integration tests (external)

---

This changelog is authoritative for all AWO v2.0.0 repository state transitions.

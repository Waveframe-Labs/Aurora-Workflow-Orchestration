---
title: "AWO Change Log"
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
ai_assistance_details: "Initial structure drafted AI-assisted under human direction. Will be manually appended for all subsequent modifications."
anchors:
  - "AWO-CHANGE-LOG-v2.0.0"
dependencies:
  - "../AWO_OVERVIEW.md"
  - "../DOCUMENT_REGISTRY.md"
  - "../INVARIANTS.md"
  - "../WORKFLOW_SPEC.md"
  - "../ARTIFACT_SCHEMA_MAP.md"
---

# AWO — Change Log

This file documents **chronological changes** to the AWO methodology and supporting documentation.

It is **non-normative**, but changes recorded here must correspond to  
**approved modifications of normative artifacts** and/or project structure.

Versioning follows **semantic methodology conventions**:

- **Major** → breaking methodological change
- **Minor** → additional capabilities without breaking compatibility
- **Patch** → clarifications, formatting, non-method changes

---

## Version History

### **2.0.0 — Method Layer Formalization**  
**Date:** 2025-12-28  
Status: Active (current)  

Initial formal release milestone for **AWO v2.0.0** including:

- Root normative spec files established & structured:
  - `AWO_OVERVIEW.md`
  - `WORKFLOW_SPEC.md`
  - `INVARIANTS.md`
  - `ROLES.md`
  - `ARTIFACT_CLASSES.md`
  - `ARTIFACT_REQUIREMENTS.md`
  - `GLOSSARY.md`
  - `PROVENANCE_MODEL.md`
  - `DESIGN_LAWS.md`
  - `NEUROTRANSPARENCY.md`

- Contract layer added under `/contracts/`:
  - `CONTRACT_INDEX.md`
  - machine-readable schemas (A1–A11)
  - `/examples/` directory with initiation+scope examples

- `/docs/` documentation initiated:
  - `ONBOARDING_GUIDE.md`
  - `FAQ.md`
  - `CHANGE_LOG.md` (this file)

Notes:
- AWO now structurally ready for enforcement binding under CRI-CORE.
- Audit pass required before tagging v2.0.1 or v2.1.0.

---

## Usage

All modifications to AWO must:

1. Update relevant normative file(s)
2. Record change summary here
3. Increment version where required
4. Commit with reference to ADR/approval

Failure to update the change log is considered a **governance drift event**  
and must be remediated before release.

---

<p align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity</sub>
</p>

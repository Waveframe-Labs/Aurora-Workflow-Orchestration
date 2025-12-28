---
title: "AWO Document Registry"
filetype: "documentation"
type: "specification"
version: "2.1.0"
status: "Active"
created: "2025-12-20"
updated: "2025-12-27"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted restructuring and expansion under human methodological direction."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "PROVENANCE_MODEL.md"
  - "DESIGN_LAWS.md"
  - "CONTRACT_ENFORCEMENT_MODEL.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-DOCUMENT-REGISTRY-v2.1.0"
---

# AWO Document Registry

## 1. Purpose

This registry defines the **canonical list of authoritative AWO documents**,
their **governance scope**, and **dependencies**.  
It serves as the root of identity and authority for the **Method Layer**.

No document outside this registry has normative power over AWO.

---

## 2. Normative Document Set (Authoritative)

These documents collectively define **AWO v2 methodology in full**:

| Code | Document | Governs | Type |
|---|---|---|---|
| D-1 | **SCOPE.md** | Method boundaries & authority surface | Core |
| D-2 | **INVARIANTS.md** | Non-negotiable methodological rules | Core |
| D-3 | **ROLES.md** | Workflow roles & separation constraints | Core |
| D-4 | **WORKFLOW_SPEC.md** | Workflow phase model & transitions | Core |
| D-5 | **DOCUMENT_REGISTRY.md** | Registry & authority order | Core |
| D-6 | **ARTIFACT_CLASSES.md** | Classes of artifacts workflows produce | Structural |
| D-7 | **ARTIFACT_REQUIREMENTS.md** | Required fields & validation rules | Structural |
| D-8 | **PROVENANCE_MODEL.md** | Traceability & reconstruction logic | Structural |
| D-9 | **DESIGN_LAWS.md** | Design principles & constraints | Normative |
| D-10 | **CONTRACT_ENFORCEMENT_MODEL.md** | Contract validation & state transitions | Enforcement-binding |
| D-11 | **AWO_GLOSSARY.md** | Controlled terminology | Normative |
| D-12 | **AWO_NEUROTRANSPARENCY.md** | Cognitive provenance obligations under AWO | Normative |

📌 **These files *are* AWO v2. If it’s not listed above, it cannot define method.**

---

## 3. Schema & Contract Attachments

These are **not normative individually**, but are **normatively referenced**.  
Breaking or removing them affects compliance.

📁 `/contracts/schemas/`

- `awo.approval.schema.json`
- `awo.audit.schema.json`
- `awo.change_log.schema.json`
- `awo.contribution.schema.json`
- `awo.dependency.schema.json`
- `awo.evaluation.schema.json`
- `awo.initiation.schema.json`
- `awo.issue_register.schema.json`
- `awo.reasoning.schema.json`
- `awo.review.schema.json`
- `awo.scope.schema.json`

📁 `/contracts/`

- `CONTRACT_ENFORCEMENT_MODEL.md`
- `CONTRACT_INDEX.md`
- `ARTIFACT_SCHEMA_MAP.md`

These files form the **machine-readable enforcement surface for CRI-CORE**.

---

## 4. Authority Hierarchy (Resolution Order)

If conflict occurs:

1. **SCOPE.md**
2. **INVARIANTS.md**
3. **ROLES.md**
4. **WORKFLOW_SPEC.md**
5. **DOCUMENT_REGISTRY.md**
6. All other normative AWO docs
7. Artifact/Schema docs
8. Contracts & enforcement docs
9. Figures & explanatory materials

This ordering MUST be respected across all repos and tools.

---

## 5. Document Lifecycle & Change Rules

- Changes to Core docs require **major version bump**
- Additions/removals require **registry update**
- Deprecation must record rationale + successor document
- Historical versions must remain publicly accessible (`/v1-archived/`)

Registry updates without version control violate ARI governance law.

---

## 6. Non-Normative Materials

The following DO NOT define method:

- Diagrams, READMEs, website text
- Examples, tutorials, walkthroughs
- Archived v1 documentation
- Tooling implementations
- Generated PDFs

They exist *to enable* AWO, never *override* it.

---

<div align="center">
<sub>© 2025 Waveframe Labs — Method Layer Authority Registry</sub>
</div>

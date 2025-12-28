---
title: "AWO Contract Index"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-27"
updated: "2025-12-27"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with full human oversight; contract inventory derived from AWO v2.0.0 normative specifications and ARTIFACT_SCHEMA_MAP.md; aligned with ARI Metadata Policy v2.0.0."
dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "ARTIFACT_SCHEMA_MAP.md"
  - "ARI Metadata Policy v2.0.0"
anchors:
  - "AWO-CONTRACT-INDEX-v2.0.0"
---

# AWO Contract Index

## 1. Purpose

This document is the **authoritative index of all machine-readable contracts**
defined under **Aurora Workflow Orchestration (AWO) v2.0.0**.

It answers the question:

> "What machine-enforceable contracts exist, and which normative artifacts authorize them?"

This document is **normative with respect to contract existence and identity**.  
It does **not** define contract semantics, schema contents, or enforcement behavior.

All contracts listed here MUST be traceable to upstream AWO specifications
and MUST NOT introduce new methodological rules.

---

## 2. Relationship to the Method Layer

Contracts are a **projection** of AWO’s method layer into machine-readable form.

- **Source of authority:**  
  All contracts derive from:

  - `SCOPE.md` (what AWO governs)  
  - `INVARIANTS.md` (non‑negotiable constraints)  
  - `ROLES.md` (workflow role semantics)  
  - `WORKFLOW_SPEC.md` (phases and transitions)  
  - `ARTIFACT_CLASSES.md` and `ARTIFACT_REQUIREMENTS.md` (what must exist)

- **Projection boundary:**  
  Contracts MAY only formalize requirements that already exist
  in these documents.

- **Enforcement separation:**  
  Execution and enforcement (e.g., by CRI-CORE or other validators)
  are **downstream**.  
  Those systems MUST treat this index as the single source of contract truth.

---

## 3. Contract Types

Contracts are grouped into four logical families:

1. **Artifact Schema Contracts** — structure and required fields
2. **Phase / Workflow Contracts** — phase transitions and role constraints
3. **Provenance & Neurotransparency Contracts** — lineage and cognitive trace
4. **Metadata & Disclosure Contracts** — ARI metadata and NTS alignment

Actual JSON schema paths and filenames are governed by `ARTIFACT_SCHEMA_MAP.md`.  
This index defines **contract IDs, scopes, and authorizing documents**.

---

## 4. Artifact Schema Contracts

Artifact schema contracts formalize the structure of AWO artifacts defined
in `ARTIFACT_CLASSES.md` and `ARTIFACT_REQUIREMENTS.md`.

> **Note:** `schema_key` refers to the canonical key in `ARTIFACT_SCHEMA_MAP.md`,
> which in turn points to a concrete JSON schema file under `/schemas/`.

| Contract ID         | Logical Scope              | schema_key (see ARTIFACT_SCHEMA_MAP.md) | Authorized By                                      | Status |
|---------------------|----------------------------|------------------------------------------|----------------------------------------------------|--------|
| AWO-CONTRACT-A1     | Initiation artifacts       | `initiation_manifest`                    | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md      | Active |
| AWO-CONTRACT-A2     | Scope / objectives records | `scope_record`                           | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md      | Active |
| AWO-CONTRACT-A3     | Contribution artifacts     | `contribution_record`                    | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md      | Active |
| AWO-CONTRACT-A4     | Evaluation artifacts       | `evaluation_record`                      | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md      | Active |
| AWO-CONTRACT-A5     | Reasoning / cognition logs | `reasoning_log`                          | ARTIFACT_CLASSES.md, NEUROTRANSPARENCY.md          | Active |
| AWO-CONTRACT-A6     | Review artifacts           | `review_record`                          | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md      | Active |
| AWO-CONTRACT-A7     | Issue registers            | `issue_register`                         | ARTIFACT_CLASSES.md, ARTIFACT_REQUIREMENTS.md      | Active |
| AWO-CONTRACT-A8     | Approval / decision records| `approval_record`                        | ARTIFACT_CLASSES.md, INVARIANTS.md, ROLES.md       | Active |
| AWO-CONTRACT-A9     | Audit reports              | `audit_report`                           | ARTIFACT_CLASSES.md, INVARIANTS.md                 | Active |
| AWO-CONTRACT-A10    | Change logs                | `change_log`                             | ARTIFACT_CLASSES.md, PROVENANCE_MODEL.md           | Active (Optional) |
| AWO-CONTRACT-A11    | Dependency manifests       | `dependency_manifest`                    | ARTIFACT_CLASSES.md, PROVENANCE_MODEL.md           | Active (Optional) |

**Interpretation:**

- "Active" means a schema exists and may be enforced.
- "Optional" indicates the artifact is optional in the method layer
  but MUST comply with the schema when present.

---

## 5. Phase and Workflow Contracts

Phase / workflow contracts formalize structural requirements from `WORKFLOW_SPEC.md`
and `INVARIANTS.md`, such as allowed transitions and role eligibility.

| Contract ID         | Logical Scope                   | schema_key (see ARTIFACT_SCHEMA_MAP.md) | Authorized By                      | Status |
|---------------------|----------------------------------|------------------------------------------|------------------------------------|--------|
| AWO-CONTRACT-W1     | Workflow phase graph             | `workflow_phase_graph`                   | WORKFLOW_SPEC.md, INVARIANTS.md    | Active |
| AWO-CONTRACT-W2     | Phase transition constraints     | `phase_transition_rules`                 | WORKFLOW_SPEC.md, INVARIANTS.md    | Active |
| AWO-CONTRACT-W3     | Phase-to-artifact mapping        | `phase_artifact_map`                     | WORKFLOW_SPEC.md, ARTIFACT_CLASSES.md | Active |

These contracts do **not** redefine phases; they ensure that any machine-readable
workflow description remains consistent with the normative `WORKFLOW_SPEC.md`.

---

## 6. Provenance & Neurotransparency Contracts

Provenance and neurotransparency contracts encode lineage and cognitive trace
requirements from `PROVENANCE_MODEL.md` and `NEUROTRANSPARENCY.md`.

| Contract ID         | Logical Scope                       | schema_key (see ARTIFACT_SCHEMA_MAP.md) | Authorized By                       | Status |
|---------------------|--------------------------------------|------------------------------------------|-------------------------------------|--------|
| AWO-CONTRACT-P1     | Provenance record structure          | `provenance_record`                      | PROVENANCE_MODEL.md                 | Active |
| AWO-CONTRACT-P2     | Artifact linkage / chain-of-custody  | `provenance_link`                        | PROVENANCE_MODEL.md, INVARIANTS.md  | Active |
| AWO-CONTRACT-N1     | Neurotransparency pointer records    | `neurotrace_pointer`                     | NEUROTRANSPARENCY.md, INVARIANTS.md | Active |
| AWO-CONTRACT-N2     | Cognitive influence registry entries | `cognitive_influence_entry`              | NEUROTRANSPARENCY.md, ROLES.md      | Active |

These contracts ensure that:

- Every claim-affecting inference can be traced,
- Provenance chains are machine-verifiable,
- Cognitive influence (human or AI) is reconstructible.

---

## 7. Metadata & Disclosure Contracts

Metadata and disclosure contracts formalize ARI metadata and NTS-aligned
disclosure requirements.

| Contract ID         | Logical Scope                       | schema_key (see ARTIFACT_SCHEMA_MAP.md) | Authorized By                               | Status |
|---------------------|--------------------------------------|------------------------------------------|---------------------------------------------|--------|
| AWO-CONTRACT-M1     | YAML metadata blocks                 | `markdown_metadata_block`                | ARI Metadata Policy v2.0.0                  | Active |
| AWO-CONTRACT-M2     | AI assistance disclosure             | `ai_assistance_disclosure`               | ARI Metadata Policy v2.0.0, NTS             | Active |
| AWO-CONTRACT-M3     | NTS cognitive disclosure bindings    | `nts_disclosure_binding`                 | NEUROTRANSPARENCY.md, NTS, AWO_OVERVIEW.md  | Active (Optional) |

These contracts do **not** define NTS; they ensure that when NTS-required
fields are present, they follow a consistent schema.

---

## 8. Contract Status Semantics

Contract `Status` values have the following meanings:

- **Planned** — Contract is declared in this index, but its schema
  is not yet implemented or approved.
- **Active** — Contract schema exists, has been validated, and may be
  relied upon by enforcement tooling.
- **Deprecated** — Contract is maintained only for backward compatibility.
  New workflows SHOULD NOT depend on it.
- **Retired** — Contract is no longer valid; new references are prohibited.

Status transitions MUST be recorded via:

- an update to this document,
- a corresponding ADR entry,
- and a version increment where applicable.

---

## 9. Change Control

The **identity and existence** of contracts are governed by this index.

- Adding a new contract:
  - Requires adding a new entry here,
  - Requires an ADR documenting its rationale and authority,
  - Is typically a **minor** or **patch** version change, unless it alters
    methodological scope.

- Removing a contract:
  - Requires explicit deprecation followed by retirement,
  - MUST preserve backward traceability for historical workflows,
  - MAY require a **major** version change if core method behavior is affected.

- Renaming a contract ID:
  - Is a breaking change and requires a **major** version bump.
  - MUST document mapping from old ID to new ID.

Schema content changes that do **not** alter contract identity or status
do **not** require updates to this index, but SHOULD be cross-referenced
via ADRs and schema version fields.

---

## 10. Enforcement Boundary

This index defines what contracts **exist**. It does not execute or enforce them.

Downstream enforcement systems (e.g., CRI-CORE) MUST:

- Treat this index as the **single source of truth** for:
  - Contract IDs
  - Contract types
  - Status values
- Refuse to enforce contracts not listed as **Active**.
- Fail safely if:
  - A referenced contract is missing,
  - A contract is marked Deprecated or Retired for the requested use case.

Tooling MUST NOT:

- Infer new contracts from schema files alone,
- Treat unlisted schema files as authoritative AWO contracts,
- Redefine AWO methodology via schema changes.

---

## 11. Compliance Requirement

This document is institutionally valid only if its metadata block complies
with **ARI Metadata Policy v2.0.0**.

Any modification that renders the metadata non-compliant invalidates this
document as an authoritative AWO artifact.

---

<div align="center">
  <sub>© 2025 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>

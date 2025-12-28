---
title: "AWO Glossary"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-24"
updated: "2025-12-24"
author: "Waveframe Labs"
maintainer: "Waveframe Labs"
license: "Apache-2.0"
ai_assisted: "partial"
ai_assistance_details: "AI-assisted drafting with human oversight; terminology consolidated from AWO whitepaper v1.2.1, method spec lineage, NTS/NTD foundational docs, ARI governance structures, and artifact methodology."
dependencies:
  - "AWO_OVERVIEW.md"
  - "INVARIANTS.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "ARTIFACT_REQUIREMENTS.md"
  - "ROLES.md"
  - "PROVENANCE_MODEL.md"
anchors:
  - "AWO-GLOSSARY-v2.0.0"
---

# AWO Glossary

Authoritative term definitions for **Aurora Workflow Orchestration (AWO)**.  
If terminology conflicts with other AWO docs, **this glossary governs meaning**.

---

## Core Concepts

**Aurora Workflow Orchestration (AWO)** — methodology governing reproducible, artifact‑first research under role separation and verifiable traceability.

**Method vs. Enforcement** — AWO defines workflow rules; CRI‑CORE and tooling enforce them.

**Governance Layer (ARI)** — upstream authority defining metadata law, role boundaries, and change control.

**Neurotransparency (NTD/NTS)** — epistemic requirement for traceable cognition. AWO integrates it at workflow level.

**Reproducibility (AWO Definition)** — ability to reconstruct **reasoning + decisions** using artifacts. Not merely rerunning experiments.

---

## Artifacts

**Artifact** — a persistent, role‑attributed file capturing epistemic state. If no artifact exists, the action is methodologically invisible.

**Artifact Class** — category of artifact with defined purpose (A‑1 to A‑11).

**Artifact Requirements** — semantic minima an artifact must contain to be valid.

**Supersession** — replacement with version retention. Originals are never discarded.

**Invalid Artifact** — missing required metadata, provenance, or role legality. Must not enter provenance chains.

---

## Workflow Structure

**Workflow Phase** — one of six required stages: Initiation → Scoping → Contribution → Review → Approval → Audit.

**Entry Condition** — prerequisites required before entering a phase.

**Exit Condition** — required artifacts/decisions needed to transition forward.

**Transition** — movement between phases. Must be explicit and traceable.

---

## Roles

**Role** — procedural authority assignment. Defined in `ROLES.md`.

**Orchestrator** — initiates and scopes workflow; cannot approve or audit outputs.

**Contributor** — produces work artifacts and reasoning.

**Reviewer** — evaluates contributions using evaluation criteria.

**Approver** — grants acceptance or rejection; independent of contributor/reviewer.

**Auditor** — verifies invariants, provenance, and artifact lineage.

---

## Provenance & Verification

**Provenance Chain** — complete linked lineage of artifacts proving how knowledge was formed. Defined in `PROVENANCE_MODEL.md`.

**Attestation** — formal approval event. Self‑attestation prohibited.

**Checksum (SHA‑256)** — immutable identity fingerprint for artifact integrity.

**Evidence** — artifacts/logs that substantiate claims. No evidence → no claim.

---

## Compliance Vocabulary

| Term | Meaning |
|---|---|
| MUST | Mandatory without exception |
| MUST NOT | Prohibited; violation invalidates workflow |
| SHOULD | Strong recommendation; deviations must be justified |
| MAY | Optional, discretionary |
| INVALID | Not eligible for workflow progression |
| COMPLIANT | Meets structural, role, and provenance criteria |

---

## Change Control

Changes to term meaning require **major version increments**.  
Clarifications may be minor revisions if meaning is unchanged.

---

<div align="center"><sub>© 2025 Waveframe Labs — Governed by ARI</sub></div>

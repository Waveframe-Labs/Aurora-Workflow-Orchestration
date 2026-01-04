---
title: "AWO Artifact Requirements"
filetype: "documentation"
type: "specification"
version: "2.0.0"
status: "Active"
created: "2025-12-20"
updated: "2026-01-04"

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
ai_assistance_details: "AI-assisted drafting with full human oversight; revised to align with AWO v2 Design Envelope, Minimal Phase Topology, and approved Artifact Classes."

dependencies:
  - "SCOPE.md"
  - "INVARIANTS.md"
  - "ROLES.md"
  - "WORKFLOW_SPEC.md"
  - "ARTIFACT_CLASSES.md"
  - "PHASE_TOPOLOGY.md"

anchors:
  - "AWO-ARTIFACT-REQUIREMENTS-v2.0.0"
---

# AWO Artifact Requirements

## 1. Purpose

This document defines the **minimum informational requirements**
for each artifact class specified in **ARTIFACT_CLASSES.md**.

It answers the question:

> **What information MUST exist for an artifact to be methodologically valid under AWO?**

This document defines **requirements**, not formats, schemas, tooling, or enforcement.

This document is **normative**.

---

## 2. Global Requirements (All Artifacts)

Unless explicitly exempted, all AWO artifacts MUST satisfy the following:

### R-1 — Metadata Presence
- Artifacts MUST include a structured metadata block sufficient to:
  - identify the artifact,
  - identify responsible parties,
  - declare version and status,
  - enable traceability.

The specific metadata schema is defined externally.

---

### R-2 — Role Declaration
- The producing role MUST be explicitly declared.
- The role MUST be permitted to produce the artifact class under **ROLES.md**.

---

### R-3 — Traceability
- Artifacts MUST reference:
  - their immediate inputs, and
  - any upstream artifacts they depend upon.

Opaque artifacts are methodologically invalid.

---

### R-4 — Determinism Disclosure
- Artifacts MUST declare whether their contents are:
  - deterministic,
  - partially deterministic,
  - or nondeterministic.

This declaration is descriptive, not evaluative.

---

### R-5 — Change Disclosure
- If an artifact revises or supersedes a prior artifact, that relationship MUST be declared.
- The reason for change MUST be stated.

---

## 3. Class-Specific Requirements

### A-1 — Initiation Record
MUST include:
- Declared research objective
- Initial scope intent
- Declared constraints or assumptions
- Producing role declaration

---

### A-2 — Scope Definition Artifact
MUST include:
- Explicit in-scope items
- Explicit out-of-scope items
- Boundary rationale
- Revision history (if applicable)

---

### A-3 — Evaluation Criteria Artifact
MUST include:
- Acceptance criteria
- Rejection criteria
- Quality thresholds
- Notes on applicability and limitations

---

### A-4 — Contribution Artifact
MUST include:
- Substantive work product
- Input references
- Declared limitations
- Explicit linkage to reasoning records (if separate)

---

### A-5 — Reasoning Record
MUST include:
- Structured reasoning steps
- Transformations applied to inputs
- Justifications for assumptions
- Known uncertainties or gaps

---

### A-6 — Review Report
MUST include:
- Artifacts reviewed
- Criteria applied
- Findings and concerns
- Reviewer role declaration

---

### A-7 — Issue Register
MUST include:
- Enumerated issues
- Severity or impact assessment
- Required remediation actions

---

### A-8 — Release Record
MUST include:
- Declared release decision
- Artifacts included in the release
- Basis for freezing the workflow iteration
- Responsible role declaration

---

### A-9 — Audit Report
MUST include:
- Invariant compliance assessment
- Traceability verification
- Deviations or violations identified
- Auditor role declaration

Audit artifacts exist **outside workflow execution**.

---

### A-10 — Change Log Entry
MUST include:
- Description of change
- Affected artifacts
- Justification
- Authorizing role declaration

---

### A-11 — Dependency Declaration
MUST include:
- Enumerated dependencies
- Version identifiers when available
- Relevance description

---

## 4. Explicit Non-Requirements

This document DOES NOT define:
- file formats,
- directory structures,
- naming conventions,
- schema implementations,
- validation mechanisms,
- enforcement behavior.

Those concerns are addressed downstream.

---

## 5. Stability and Change Control

Any change to artifact requirements constitutes a **breaking methodological change**
and requires a major version increment with documented rationale.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

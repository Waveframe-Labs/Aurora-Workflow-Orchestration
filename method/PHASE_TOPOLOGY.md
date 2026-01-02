
---

## Phase 1 — Initiation

### Purpose
Capture the existence of an intentional unit of work.

### Entry Condition
- None (this is the starting phase).

### Required Artifacts
- **Initiation Artifact**
  - Declares intent
  - Declares scope boundary (high-level)
  - Declares initiating actor(s)
  - Declares AI assistance (if any)

### Allowed Roles
- Originator
- Synthesizer

### Structural Constraints
- Artifact must be complete and schema-conformant.
- No claims of correctness or legitimacy allowed.

### Forbidden in This Phase
- Validation
- Review
- Claims of approval or authority

---

## Phase 2 — Specification

### Purpose
Make intended reasoning explicit before execution.

### Entry Condition
- Initiation Artifact exists.

### Required Artifacts
- **Specification Artifact**
  - Defines goals or questions
  - Declares assumptions
  - References governing doctrine/specifications (by link only)
  - Declares intended methods or approach

### Allowed Roles
- Originator
- Synthesizer

### Structural Constraints
- All declared references must be linked.
- No results or conclusions permitted.

### Forbidden in This Phase
- Execution outputs
- Evaluative judgments
- Claims of success or failure

---

## Phase 3 — Execution

### Purpose
Record the act of doing work under the declared specification.

### Entry Condition
- Specification Artifact exists.

### Required Artifacts
- **Execution Artifact(s)**
  - Records actions taken
  - Records tools used
  - Records data or intermediate outputs
  - Records deviations from specification (if any)

### Allowed Roles
- Executor
- Originator

### Structural Constraints
- Every execution artifact must reference a specification.
- Deviations must be declared, not justified.

### Forbidden in This Phase
- Final conclusions
- Approval statements
- Validation claims

---

## Phase 4 — Review

### Purpose
Declare evaluation activity without asserting authority.

### Entry Condition
- At least one Execution Artifact exists.

### Required Artifacts
- **Review Artifact**
  - Declares reviewer role
  - Declares review scope
  - Declares evaluation criteria (descriptive)
  - Records observations or concerns

### Allowed Roles
- Validator
- Curator

### Structural Constraints
- Reviewer role must be declared.
- Review may reference but not alter prior artifacts.

### Forbidden in This Phase
- Enforcement actions
- Final legitimacy claims
- Release or publication actions

---

## Phase 5 — Release

### Purpose
Freeze artifacts for downstream consumption.

### Entry Condition
- Review Artifact exists.

### Required Artifacts
- **Release Artifact**
  - Enumerates included artifacts
  - Declares release context
  - Declares version identifier
  - Declares publication intent (if any)

### Allowed Roles
- Curator

### Structural Constraints
- Release is additive only (no mutation).
- All included artifacts must be linked.

### Forbidden in This Phase
- Post-release modification
- Retroactive justification
- Claims of approval or correctness

---

## Structural Enforcement Clarification

AWO enforces **structure only**, including:
- phase ordering
- artifact presence
- schema conformance
- declared role presence

AWO does **not** enforce:
- truth
- quality
- legitimacy
- compliance
- acceptance

Violations are **detectable** at the structural level and may be acted upon by downstream systems.

---

## Boundary Statement

This phase topology:
- does not redefine governance (L0),
- does not enforce validation (L4),
- does not encode ontology (L2),
- does not track lineage (L3).

It exists solely to **make epistemic responsibility legible through ordered structure**.

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Governed under the Aurora Research Initiative (ARI)</sub>
</div>

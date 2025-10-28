# Aurora Workflow Orchestration (AWO)
## Method Specification — v1.2.1 (Scaffold)
Maintainer: Waveframe Labs  
License: CC BY 4.0 (docs), Apache 2.0 (code)

---

### Preface
This document defines the **normative specification** for Aurora Workflow Orchestration (AWO).  
It replaces descriptive or philosophical language with enforceable procedural logic.  
All future automation layers (e.g., CRI-CORE) must validate conformance against these requirements.

**Interpretation of Compliance Language**  
- **MUST** — absolute requirement for AWO-compliant repositories.  
- **SHOULD** — strong recommendation; deviations must be justified in documentation.  
- **MAY** — optional behavior permitted for flexibility.  

---

## 1. Introduction

### 1.1 Purpose
Aurora Workflow Orchestration (AWO) establishes a formal, falsifiable framework for conducting reproducible AI-assisted research.  
It defines the structural and procedural rules by which reasoning processes—whether human, synthetic, or hybrid—are documented, attested, and version-controlled.

This specification is **methodological**, not philosophical.  
It governs the organization, validation, and archival of reasoning artifacts so that every claim produced under AWO can be independently verified.

---

### 1.2 Scope
This document applies to all research workflows that:

- Integrate AI or automated reasoning systems as active participants in the research process.  
- Produce verifiable artifacts such as manifests, runs, and audit logs.  
- Intend for those artifacts to be **reproducible, falsifiable, and citable**.  

It defines the **minimum structural and procedural requirements** for an AWO-compliant repository, including file hierarchy, provenance recording, versioning, and attestation rules.

AWO does **not** specify runtime behavior or enforcement mechanisms.  
Those are defined in successor frameworks such as **CRI-CORE**, which must implement this specification as their normative foundation.

---

### 1.3 Objectives
The objectives of the AWO standard are to:

1. Encode the **scientific method** as a verifiable workflow rather than a descriptive ideal.  
2. Replace subjective credibility with **objective auditability**.  
3. Ensure that every reasoning artifact—data, model, or decision—can be traced to its origin.  
4. Provide a foundation for automated reproducibility enforcement systems.  
5. Support both manual and fully automated orchestration without altering compliance semantics.

---

### 1.4 Relationship to Other Documents
- The **AWO Whitepaper** provides conceptual background and philosophical rationale.  
- The **AWO Adoption Guide** describes practical implementation and onboarding.  
- This **Method Specification** defines the normative requirements that all AWO artifacts must satisfy.  

Where discrepancies occur, **this specification takes precedence**.

---

### 1.5 Normative References
- **AWO Whitepaper v1.1** (Waveframe Labs)  
- **Aurora Workflow Orchestration Adoption Guide v1.2.1**  
- **Architecture Decision Records (ADR-0001 – ADR-0017)** — authoritative design decisions underlying AWO’s structural, governance, and lifecycle model.  
- **CRI-CORE Design Notes** (draft, forthcoming)  
- **ISO/IEC Directives Part 2** — interpretation of compliance terms (“shall,” “should,” “may”)

---

### 1.6 Status of This Version
Version 1.2.1 represents the **finalized methodological form** of AWO under Waveframe Labs governance.  
Future revisions may clarify or extend definitions for CRI-CORE compatibility but will not alter the normative logic without an explicit version increment.

---

## 2. Definitions

This section defines the key entities and concepts used throughout the Aurora Workflow Orchestration (AWO) standard.  
All terms are **normative** unless otherwise specified.

Wherever applicable, definitions align with terminology used in the AWO Whitepaper and will later be cross-referenced to CRI-CORE schema identifiers.

---

### 2.1 Core Entities

**Run**  
A discrete, traceable research execution instance.  
Each Run represents a bounded reasoning process that produces one or more verifiable artifacts and is identified by a unique timestamp or run ID.  
All Runs must be immutable once attested.

**Provenance**  
The complete, chronological lineage of data, logic, parameters, and decisions leading to a result.  
Provenance includes all intermediate steps, transformations, and validations necessary to reproduce a Run.  
In CRI-CORE, this concept maps to the `provenance-ledger` schema.

**Artifact**  
Any persistent output generated within an AWO process.  
Artifacts include reports, manifests, ADRs, checksums, datasets, logs, or schema validation results.  
Artifacts must be versioned, hashable, and linkable to a Run.

**Attestation**  
A confirmation—human, automated, or hybrid—that artifacts produced during a Run are complete, correct, and verified against defined falsifiability criteria.  
Attestations are recorded in `approval.json` and form the evidentiary basis for repository integrity.

**ADR (Architecture Decision Record)**  
A structured document that records a significant reasoning or design choice, the context in which it was made, and its consequences.  
ADRs form the canonical log of epistemic evolution and are numbered sequentially (`ADR-0001` to `ADR-NNNN`).  
Each Run must reference at least one ADR.

**Manifest (Falsifiability Manifest)**  
A declaration of the hypothesis, predicted outcomes, and explicit disproof conditions for a Run.  
The Manifest defines what constitutes falsification before execution.  
It serves as the precondition for attestation and must be stored under `/docs/`.

---

### 2.2 Secondary Concepts

**Repository**  
The complete version-controlled environment in which all AWO artifacts are stored.  
Every AWO-compliant Repository must maintain a standard directory structure defined in Section 4.

**Role**  
A functional agent—human or synthetic—responsible for a specific epistemic operation within the reasoning lifecycle (see Section 3).  
Roles are procedural, not hierarchical.

**Conformance**  
The degree to which an AWO repository satisfies all mandatory requirements defined in this specification.  
Conformance is binary (pass/fail) for each clause but may include graded compliance levels (“Minimum,” “Standard,” “Full”) as defined in the Adoption Guide.

**Attestation Record**  
The recorded output of a completed review or validation step, stored as a structured file (`approval.json`) under the corresponding Run directory.  
It includes participant identity, timestamp, and signature or digital hash.

---

### 2.3 Future Schema Alignment
All defined entities in this section will be mapped to corresponding CRI-CORE schema classes in later versions.  
Cross-references will be introduced once the enforcement layer is finalized.

**TODO:** Refine definitions list and cross-link to CRI-CORE schema references after CRI draft publication.

---

## 3. Roles and Responsibilities

### 3.1 Overview
AWO defines **roles** as functional agents within a reasoning workflow, not as human job titles.  
Each role represents a discrete epistemic operation necessary to ensure falsifiability, reproducibility, and integrity.  
Roles may be embodied by humans, AI systems, or hybrid arrangements, but the **responsibility and accountability structure** must remain explicit and verifiable.

Every AWO-compliant Run MUST declare the roles involved and the corresponding participants (human or synthetic).  
Multiple roles MAY be fulfilled by a single agent if traceability and attestation integrity are preserved.

---

### 3.2 Canonical Roles

| Role | Core Function | Description | Typical Implementation |
|------|----------------|-------------|-------------------------|
| **Orchestrator** | Governance and context management | Governs execution order, maintains reasoning context, and determines when to fork, merge, or conclude runs. Responsible for continuity, documentation, and decision routing. | Human-in-the-loop controller or primary model agent (e.g., lead researcher, workflow coordinator). |
| **Voter / Evaluator** | Comparative validation | Compares multiple reasoning paths or outputs, ranks them by internal consistency and falsifiability, and selects the candidate most aligned with predefined criteria. | Model ensemble, peer review, or statistical evaluator. |
| **Auditor** | Verification and compliance | Independently checks reasoning validity, schema adherence, falsifiability, and traceability to prior evidence. Approves or rejects attestation claims. | Dedicated verification model, CI validator, or human reviewer. |
| **Synthesizer / Consensus** | Result consolidation | Merges validated reasoning threads into a coherent, singular artifact. Produces the final report or output from attested inputs. | Aggregation model, summarizer, or post-processing layer. |
| **Critic / Red Team (optional)** | Adversarial robustness testing | Generates counterarguments or adversarial reasoning challenges to expose weaknesses in claims before attestation. | Adversarial model, external reviewer, or dedicated counterfactual analysis agent. |

---

### 3.3 Role Interactions

- **Sequential Integrity:** Roles SHOULD execute in a reproducible order—Orchestrator → Evaluator → Auditor → Synthesizer.  
  Optional Critic roles MAY interject between Evaluator and Synthesizer stages.
- **Non-Circular Validation:** The same agent MUST NOT serve as both Orchestrator and Auditor within the same Run unless explicitly justified and recorded in the attestation log.
- **Attestation Requirements:** Each Run MUST include a record of which roles were fulfilled, by whom, and under what authority.
- **Traceability Obligation:** Artifacts and logs MUST explicitly reference the roles responsible for their generation or validation.

---

### 3.4 Role Attribution and Record-Keeping
- Every `approval.json` file MUST list all participating roles and their associated agent identifiers (human name, model ID, or process hash).  
- When multiple roles are automated, their decision boundaries MUST be defined in the workflow manifest or configuration file.  
- Manual overrides or deviations from standard AWO behavior MUST be documented under /logs/overrides/ and cross-referenced to the applicable ADR  

---

### 3.5 Compliance and Auditing
- AWO-compliant repositories MUST demonstrate separation of governance (Orchestrator) and verification (Auditor).  
- Each role’s output MUST be traceable to an ADR or manifest entry.  
- Automated systems fulfilling these roles MUST log model versions, prompt contexts, and decision justifications to ensure reproducibility.  
- Failure to document role interactions constitutes a **non-conformance** condition under this specification.

---

### 3.6 Future Role Extensions
Future AWO or CRI-CORE revisions MAY extend the canonical role set (e.g., **Planner**, **Historian**, **Meta-Auditor**) as automated reasoning matures.  
Any such extensions MUST maintain backward compatibility with this role schema and preserve attestation semantics.

**TODO:** Cross-link these roles to CRI-CORE validation modules (e.g., `orchestrator-agent`, `auditor-module`, `consensus-engine`) once defined.

---

## 4. Repository Requirements

### 4.1 Purpose and Scope

This section defines the mandatory and recommended structural requirements for an AWO-compliant repository.  
These requirements ensure that every research artifact is **traceable**, **auditable**, and **reproducible** without external dependencies.  
All provisions in this section are **normative** unless explicitly labeled “informative.”

---

### 4.2 Core Directory Structure

An AWO-compliant repository **MUST** include the following top-level directories:

| Directory | Purpose | Requirement |
|------------|----------|-------------|
| `/docs/` | Contains all formal documents (Whitepaper, Method Spec, Adoption Guide, PDFs, and audit summaries). | MUST |
| `/decisions/` | Contains all Architecture Decision Records (ADRs). Each ADR MUST be timestamped and sequentially numbered. | MUST |
| `/logs/` | Houses all workflow, audit, and override logs (see ADR-0004). | MUST |
| `/schemas/` | Stores validation schemas and structure definitions for manifests, runs, and audits. | SHOULD |
| `/templates/` | Contains boilerplate forms for manifests, audit reports, and ADRs. | SHOULD |
| `/runs/` | Contains attested execution outputs, including manifests, reports, approvals, and checksums. | MUST |
| `/figures/` | Contains diagrams, charts, and other non-textual documentation. | SHOULD |
| `/workflows/` | Contains procedural examples or reproducible automation steps (optional, pre-CRI). | MAY |

The repository root **MUST** contain:
- `README.md` — entry point and index.
- `CHANGELOG.md` — lifecycle record of repository evolution.
- `SHA256SUMS.txt` — integrity registry for all signed artifacts.
- `LICENSE` and `LICENSE-CC-BY-4.0.md` — primary and documentation licenses.
- `.github/workflows/` — automated build and PDF pipelines.

---

### 4.3 Log Directory Specification

Each AWO-compliant repository **MUST** implement the following substructure within `/logs/`:

| Subfolder | Description | Reference |
|------------|--------------|------------|
| `/logs/workflow/` | Chronological records of human and agent activity, covering decisions, forks, merges, and context. | ADR-0004 |
| `/logs/audits/` | Independent audit results, rejection events, or revalidation findings. | ADR-0003 |
| `/logs/overrides/` | Manual interventions, rationale, and signatures for non-automated overrides. | ADR-0004, ADR-0012 |

Log entries **MUST** follow the schema outlined in ADR-0004, including timestamps, participant IDs, impacted artifacts, and outcome codes.  
Each log file **MUST NOT** be modified retroactively after attestation.

---

### 4.4 ADR Requirements

- ADRs **MUST** follow sequential numbering (`ADR-0001` through `ADR-NNNN`) and reside in `/decisions/`.  
- Each ADR **MUST** contain:  
  - Title, Status, Context, Decision, Consequences, and References.  
  - Date and author or originating role (Orchestrator, Auditor, etc.).  
- ADRs **MUST** reference corresponding workflow or audit logs when applicable.  
- Superseded ADRs **MUST** be marked `Deprecated` but retained for historical integrity.  
- ADRs **SHOULD** be linked from the Method Spec or README where directly relevant.

---

### 4.5 Manifest and Run Directory Requirements

Each repository **MUST** include a `/runs/` directory containing subfolders for every attested execution.  
Each Run folder **MUST** contain:

| File | Description | Requirement |
|-------|--------------|-------------|
| `manifest.json` or `.md` | Falsifiability declaration and preconditions for the run. | MUST |
| `report.md` | Primary human-readable research output. | MUST |
| `approval.json` | Attestation record confirming verification or rejection. | MUST |
| `hash.txt` or inclusion in `SHA256SUMS.txt` | Integrity signature of run artifacts. | MUST |
| `metadata.json` | Contextual parameters, participants, and timestamps. | SHOULD |

All files within a Run folder **MUST** be immutable once signed and referenced in `SHA256SUMS.txt`.

---

### 4.6 Integrity and Attestation

- The repository **MUST** maintain a single authoritative checksum file (`SHA256SUMS.txt`) in the root directory.  
- Every attested artifact (PDF, manifest, run report, ADR, etc.) **MUST** be listed with its SHA-256 digest.  
- Attestation signatures **MUST** follow the cryptographic signing policy defined in ADR-0015.  
- Human signoffs **MUST** reference ADR-0012 and be recorded in `/logs/overrides/` if manual validation was required.

---

### 4.7 Documentation & PDF Builds

- All core documents (`AWO_Method_Spec`, `AWO_Whitepaper`, `AWO_Adoption_Guide`) **MUST** be compiled via automated workflows.  
- The build system **MUST** ensure reproducibility and checksum verification per ADR-0016.  
- Generated PDFs **MUST** reside in `/docs/` and be referenced in the release assets.

---

### 4.8 Governance and Continuity

- The repository **MUST** include a governance note or `README` section referencing ADR-0017, confirming oversight under the Aurora Research Initiative (ARI).  
- Any repository transfer, rename, or fork **MUST** preserve ADR continuity and integrity hashes.  
- The repository’s `README.md` **MUST** declare the canonical DOI (see ADR-0010).  

---

### 4.9 Compliance Tiers (Informative)

AWO compliance operates in three tiers, as detailed in the Adoption Guide:
- **Minimum Compliance** — manual logging and attestation only.  
- **Standard Compliance** — includes structured manifests, checksums, and ADR linking.  
- **Full Compliance** — includes automated builds, schema validation, and cryptographic attestation.

---

### 4.10 Future Integration

When CRI-CORE enforcement becomes active:
- Validation schemas in `/schemas/` **WILL** become executable policies.
- Manual override logs in `/logs/overrides/` **WILL** trigger runtime verification events.
- Repository audits **WILL** be automatically generated from `SHA256SUMS.txt` diffs.

**TODO:** Link this section to CRI enforcement spec once published.


---

## 5. Lifecycle and Run Phases
Each research cycle proceeds through four canonical phases:

1. **Fan-out (Planning)** — Define hypotheses, manifests, ADRs.  
2. **Consensus (Execution)** — Perform runs and collect data.  
3. **Attestation (Verification)** — Approve or reject based on falsifiability criteria.  
4. **Archival (Publication)** — Freeze results, compute checksums, tag releases.

**TODO:** Create table describing inputs/outputs for each phase.

---

## 6. Artifacts and File Rules
Every run MUST produce a verifiable set of artifacts:

| File | Description | Required |
|------|--------------|-----------|
| `workflow_frozen.json` | Captures executed parameters and inputs. | Yes |
| `report.md` | Describes outcomes, metrics, and observations. | Yes |
| `approval.json` | Signed validation record by human reviewer. | Yes |
| `SHA256SUMS.txt` | Hash registry for all outputs. | Yes |
| `manifest.json` or `manifest.md` | Defines falsifiability boundaries. | Yes |

**TODO:** Add versioning, format validation (JSON schema references), and CRI-CORE integration hooks.

---

## 7. Compliance Language
This section defines the mandatory, recommended, and optional behaviors for implementers.

| Level | Definition | Enforcement |
|--------|-------------|-------------|
| **MUST** | Required for compliance. | Hard validation |
| **SHOULD** | Recommended unless documented exception. | Warning |
| **MAY** | Optional feature. | No enforcement |

**TODO:** Map existing AWO clauses to each compliance level.

---

## 8. Governance and Attestation
Each run requires human or automated attestation of validity and completeness.

**Core Requirements:**
- Runs MUST include `approval.json` with reviewer signature and timestamp.  
- Attestation MAY include checksum verification and peer confirmation.  
- Failed attestations MUST be logged under `/logs/attestation_failures/`.  

**TODO:** Specify acceptable digital signature methods and verification workflows.

---

## 9. Release and Versioning
AWO-compliant repositories MUST version all outputs and preserve immutability.

**Release Requirements:**
- Each release corresponds to a reproducible state of the repository.  
- Tags MUST follow semantic versioning (e.g., `v1.2.1`).  
- Releases MUST attach PDF artifacts, SHA256SUMS, and ADR references.  
- Released runs MUST NOT be altered post-publication.

**TODO:** Add instructions for checksum regeneration and Zenodo linkage.

---

## 10. Licensing and Attribution
AWO uses dual licensing to separate executable and textual components.

- **Code:** Licensed under Apache 2.0.  
- **Documentation:** Licensed under CC BY 4.0.  
- Attribution MUST include author, ORCID, and concept DOI in derivative works.

**TODO:** Add structured attribution metadata schema reference.

---

## 11. Falsifiability Manifests
Each experiment MUST include a falsifiability manifest before execution.

**Manifest Contents:**
- Hypothesis statement  
- Predicted outcomes  
- Disproof criteria  
- Experimental plan  
- Acceptance thresholds  
- Known risks

**TODO:** Formalize manifest schema for CRI-CORE parsing.

---

## 12. Conformance Checklist
Each repository MUST pass the following before claiming AWO compliance:

- [ ] Standard directory structure present.  
- [ ] At least one signed run in `/runs/`.  
- [ ] ADRs and falsifiability manifests linked.  
- [ ] SHA256SUMS.txt present at root.  
- [ ] PDF artifacts built successfully.  
- [ ] CHANGELOG includes version reference.  
- [ ] README links to Whitepaper, Method Spec, Adoption Guide.  

**TODO:** Add automated compliance script references (future CRI module).

---

## 13. Appendix C — Rationale Summary (Reserved)
**TODO:** When the Method Spec text is finalized, reintroduce Appendix C summarizing why each rule exists in concise bullet form.  
(Placeholder retained for structural continuity.)

---

**End of Specification — Aurora Workflow Orchestration (AWO) v1.2.1 Scaffold**

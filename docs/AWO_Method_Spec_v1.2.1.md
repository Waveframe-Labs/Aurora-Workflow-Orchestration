# Aurora Workflow Orchestration (AWO)
## Method Specification — v1.2.1 (Scaffold)
Maintainer: Waveframe Labs  
Version: 1.2.1 Final  
Release Date: 2025-10-28  
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
Each reasoning process is treated as a bounded, attestable experiment.  
The focus is on procedural traceability rather than interpretive meaning.

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

### 1.6 Principle of Neurotransparency (Normative)

Neurotransparency is the requirement that every inference influencing a claim is attributable to a declared role and recorded in a durable artifact such that the reasoning sequence can be deterministically reconstructed.

**MUST**

Record role-attribution and traceable evidence for all claim-affecting inferences in one of: `/logs/workflow/`, `/logs/audits/`, `/decisions/`, `/docs/manifests/`, or `approval.json`.

Ensure each attested artifact cites the originating role, linked files, and hashes (see §6, §9, §10).

Fail attestation if any claim-affecting inference lacks a recorded origin, evidence link, or hash reference.

**SHOULD**

Include concise “evidence pointers” (e.g., `prompt_id`, `run_id`, `diff_anchor`, file path + line range per §8.3) to minimize ambiguity.

**MAY**

Use automated capture (CRI-CORE) to serialize reasoning steps; manual projects can summarize via structured bullets.  

<!-- CRI-CORE:placeholder:neurotransparency.schema -->

---

### 1.7 Status of This Version
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
Provenance entries SHALL include Neurotransparency pointers when reasoning sequences are partially automated (§1.6).

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
It serves as the precondition for attestation and MUST be stored under `/runs/<RUN_ID>/` (see §12.4).  

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

**Neurotransparency Evidence Pointer**  
A durable reference to the reasoning context that influenced a claim (e.g., prompt/run IDs, diff snippets, log anchors).  
A pointer MUST cite a file path under `/logs/workflow/`, `/logs/audits/`, or an ADR in `/decisions/`, and SHOULD include a stable anchor (line range, heading, or block ID).

---

### 2.3 Future Schema Alignment
All defined entities in this section will be mapped to corresponding CRI-CORE schema classes in later versions.  
Cross-references will be introduced once the enforcement layer is finalized.

<!-- CRI-TODO: Add CRI-CORE schema identifiers once published. -->

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
Neurotransparency (§1.6) applies to any role that generates, evaluates, or verifies a claim-affecting artifact.  
Missing or unverifiable evidence pointers SHALL be treated as a non-conformance (§7.5).

---

### 3.4 Role Attribution and Record-Keeping
- Every `approval.json` file MUST list all participating roles and their associated agent identifiers (human name, model ID, or process hash).  
- When multiple roles are automated, their decision boundaries MUST be defined in the workflow manifest or configuration file.  
- Manual overrides or deviations from standard AWO behavior MUST be documented under /logs/overrides/ and cross-referenced to the applicable ADR.  

---

### 3.5 Compliance and Auditing
- AWO-compliant repositories MUST demonstrate separation of governance (Orchestrator) and verification (Auditor).  
- Each role’s output MUST be traceable to an ADR or manifest entry.  
- Automated systems fulfilling these roles MUST log model versions, prompt contexts, and decision justifications to ensure reproducibility.  
- Failure to document role interactions constitutes a **non-conformance** condition under this specification.

---

### 3.6 Red Team — Normative Role Definition

The **Red Team** is an *optional but recommended* adversarial role within the AWO governance model.  
Its function is to challenge the logical soundness, falsifiability, and reproducibility of results produced during a run.

**Status:** Advisory — automation and schema integration deferred until CRI-CORE implementation.

#### Requirements

| Level | Requirement |
|:------|:-------------|
| **MUST** | Operate independently from the Orchestrator and Auditor. |
|  | Attempt at least one explicit falsification or contradiction for each major claim subject to Attestation. |
|  | Record each challenge as a narrative entry in the run’s `report.md` under the heading `## Red Team Review`. |
|  | If a challenge successfully falsifies a claim, mark the corresponding verdict in `approval.json` as `FAILED_VERIFICATION`. |
| **SHOULD** | Maintain adversarial separation (no prior access to finalized consensus artifacts). |
|  | Include entropy or compression observations, where available, to support future Neurotransparency metrics. |
| **MAY** | Be executed manually (human reviewer) or through automated agents once CRI-CORE introduces adversarial challenge modules. |

#### Rationale
This clause defines the Red Team role without introducing new folders or schema dependencies.  
It allows human reviewers to perform adversarial verification immediately using existing artifact locations (`report.md`, `approval.json`), ensuring the falsifiability principle is maintained until automated CRI-CORE modules become available.

---

### 3.7 Future Role Extensions
Future AWO or CRI-CORE revisions MAY extend the canonical role set (e.g., **Planner**, **Historian**, **Meta-Auditor**) as automated reasoning matures.  
Any such extensions MUST maintain backward compatibility with this role schema and preserve attestation semantics.

<!-- CRI-TODO: Link role modules once CRI-CORE publishes validator interfaces. -->

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
| `/logs/governance/` | Governance records of approvals, rejections, and release decisions. | ADR-0017 |
| `/logs/attestation_failures/` | Permanent records of failed or rejected attestations with reasons and run IDs. | ADR-0003 |  

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
|------|--------------|-------------|
| `run_manifest.json` | Canonical description of the run configuration and declared claims. | MUST |
| `workflow_frozen.json` | Snapshot of parameters, environment, and configuration state immediately before execution. Serves as the immutable record of run conditions. | MUST |
| `environment.json` | Expanded environment record generated automatically at runtime; may include dependency and version info. | SHOULD |
| `approval.json` | Signed attestation record confirming validation per ADR-0012. | MUST |
| `provenance.json` | Lineage map tracing input → output artifacts. | MUST |
| `gate_decision.yml` | Structured record of pass/fail decisions and rationale. | MUST |
| `report.md` | Human-readable summary of outputs and evaluation notes. | SHOULD |
| `SHA256SUMS.txt` | Integrity registry for all run artifacts. | MUST |
| `ATTSTATION.txt(.sig/.cert)` | Signature artifacts generated by the Attestation Gate. | SHOULD |  

All files above **MUST** exist in each run folder (`/runs/<RUN_ID>/`), except where noted. Each `workflow_frozen.json` serves as the canonical pre-execution record for that run.  
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

<!-- CRI-TODO: Link to CRI-CORE enforcement spec once available. -->

**TODO:** Link this section to CRI enforcement spec once published.

---

## 5. Lifecycle and Run Phases

### 5.1 Overview
Every AWO-compliant project advances through a reproducible four-phase lifecycle.  
These phases define the canonical order of epistemic operations, ensuring that each claim moves from **hypothesis** to **verified artifact** under transparent governance.

The canonical lifecycle phases are:

1. **Fan-out (Planning)** — Definition of hypotheses, falsifiability conditions, and manifests.  
2. **Consensus (Execution)** — Generation of reasoning paths or experimental runs.  
3. **Attestation (Verification)** — Evaluation of results against falsifiability and audit criteria.  
4. **Archival (Publication)** — Finalization, signing, and release of immutable artifacts.

Each phase yields its own artifacts, logs, and ADRs, forming a complete reasoning lineage.

---

### 5.2 Phase 1 — Fan-Out (Planning)

#### Purpose
To define *what will be tested, how it could fail,* and *who will oversee verification.*  
Fan-out begins the epistemic process by expanding a single research goal into a set of structured, falsifiable hypotheses.

#### Activities
- Create or update the **Run Manifest** (`manifest.md` or `.json`) describing:
  - Objective, assumptions, and falsifiability criteria.
  - Expected inputs, data sources, and transformation paths.
  - Defined roles (Orchestrator, Evaluator, Auditor, Synthesizer).
- Register a new **ADR** if the planned run changes methodology or assumptions.
- Log planning steps under `/logs/workflow/`.

#### Inputs
- Prior ADRs and manifests.  
- Source data, context from previous runs, or external citations.

#### Outputs
- Updated or new manifest.  
- Associated ADR (e.g., “ADR-NNNN — Run Plan vX”).  
- Planning log entries.
- Initial neurotransparency pointer(s) recorded under `/logs/workflow/` referencing planned claims or falsifiability clauses.  
 
#### Trigger for Next Phase
Orchestrator approval of the manifest and human sign-off per **ADR-0012 (Human-in-Loop Validation)**.

---

### 5.3 Phase 2 — Consensus (Execution)

#### Purpose
To perform reasoning, model inference, or experimental execution under the conditions defined in the manifest.

#### Activities
- Execute all reasoning agents or models specified.  
- Collect generated outputs, intermediate data, and system logs.  
- Optionally employ multiple agents or parameter sweeps to create a **fan-out of reasoning paths.**  
- Evaluate preliminary consistency via internal scoring or evaluator votes.  
- Record all contextual parameters (versions, seeds, env vars) into `/runs/<RUN_ID>/workflow_frozen.json` immediately before execution.
- During/after execution, write run-level metadata (participants, timing, outputs index) to `/runs/<RUN_ID>/metadata.json`.
- Capture reasoning context identifiers (e.g., prompt IDs, model/version, seeds, diff anchors) and store durable pointers under `/logs/workflow/`.  
 
#### Inputs
- Manifest and ADR definitions.  
- Roles configuration file (implicit or explicit).  
- Versioned environment and model parameters.

#### Outputs
- Raw results and intermediate artifacts.  
- Execution logs (`/logs/workflow/`).  
- Temporary evaluation summaries.

#### Trigger for Next Phase
Evaluator consensus or Orchestrator decision to proceed to formal verification.

---

### 5.4 Phase 3 — Attestation (Verification)

#### Purpose
To formally verify that results meet falsifiability and audit criteria defined in the manifest.  
This phase converts raw outputs into **attested knowledge.**

#### Activities
- Auditors perform validation checks:
  - Schema compliance (structure, completeness).  
  - Logical falsifiability (did any counterexample occur?).  
  - Provenance linkage (data lineage intact).
  - Neurotransparency linkage (evidence pointers present and resolvable to `/logs/workflow/`, `/logs/audits/`, or `/decisions/`).  
- Record results in `/logs/audits/`.  
- If human validation is required, document it in `/logs/overrides/` referencing **ADR-0012.**  
- Generate `approval.json` containing:
  - Verdict (`approved`, `rejected`, or `needs-revision`).  
  - Auditor signatures or cryptographic attestations (per **ADR-0015**).  
  - References to manifest, run hash, and ADR numbers.

#### Inputs
- Run artifacts from Phase 2.  
- Manifest and corresponding ADRs.  

#### Outputs
- `approval.json` (attestation record).  
- Audit log entries with validation outcomes.  
- Updated `SHA256SUMS.txt`.

#### Trigger for Next Phase
All required approvals recorded and checksums generated.

---

### 5.5 Phase 4 — Archival (Publication)

#### Purpose
To freeze, sign, and publish verified artifacts for long-term reproducibility and citation.  
This is the point at which a Run becomes an immutable element of the research record.

#### Activities
- Move verified run artifacts into `/runs/` and compute final checksums.  
- Update `SHA256SUMS.txt` and verify integrity.  
- Generate or update PDFs via automated workflows (per **ADR-0016**).  
- Create changelog entry summarizing the Run and resulting ADR references.  
- Tag repository version (e.g., `v1.2.1`) and attach signed artifacts.  
- Register DOI once repositories are synced to Zenodo or equivalent archival service (per **ADR-0010**).  

#### Inputs
- Verified artifacts from Attestation.  
- Final audit results and approval files.

#### Outputs
- Immutable run directory with all signatures.  
- Release tag and checksum record.  
- DOI-linked archival snapshot.

#### Trigger for Completion
Publication of DOI and confirmation of checksum match against `SHA256SUMS.txt`.

---

### 5.6 Lifecycle Transition Matrix

| Phase | Primary Inputs | Primary Outputs | Responsible Roles | Key Artifacts | Governing ADRs |
|--------|----------------|-----------------|------------------|----------------|----------------|
| **Fan-Out** | Prior ADRs, data, goals | Manifest, planning log | Orchestrator, Critic | `manifest.json`, ADR-NNNN | 0002, 0009, 0012 |
| **Consensus** | Manifest | Raw results, metadata | Evaluator, Synthesizer | `metadata.json`, temp logs | 0002, 0013 |
| **Attestation** | Run outputs | `approval.json`, audit logs | Auditor, Orchestrator | `/logs/audits/`, `/logs/overrides/` | 0003, 0012, 0015 |
| **Archival** | Verified artifacts | Signed release, DOI, checksums | Orchestrator, Auditor | `SHA256SUMS.txt`, release tag | 0010, 0014, 0016, 0017 |

---

### 5.7 Compliance Expectations
- Every AWO Run **MUST** pass through all four phases in order.  
- No phase **MAY** be skipped or merged unless justified in an ADR and recorded in `/logs/overrides/`.  
- Each transition **MUST** be timestamped and logged.  
- Failing a phase (e.g., rejection in Attestation) **MUST** result in either iteration or termination — never silent acceptance.  
- Archival freezes all prior phases; no edits are permitted post-checksum.

---

### 5.8 Future Automation Notes
Once CRI-CORE is operational:
- Each phase will map to a discrete enforcement module.  
- State transitions will be validated via CRI schema events.  
- Overrides will trigger automated diff-based verification alerts.

<!-- CRI-TODO: Define JSON schema alignment between lifecycle phases and CRI runtime. -->

**TODO:** Define JSON schema alignment between lifecycle phases and CRI runtime once available.

---

## 6. Artifacts and Provenance Rules

### 6.1 Purpose
This section defines the mandatory artifacts, metadata files, and validation mechanisms that constitute the **evidence chain** in every AWO-compliant repository.  
All artifacts must be uniquely identifiable, cryptographically verifiable, and cross-linked to the corresponding log and ADR entries.

---

### 6.2 Required Artifacts per Run

Every Run **MUST** produce a verifiable and complete set of artifacts:

| File | Description | Required | Notes |
|------|--------------|-----------|-------|
| **workflow_frozen.json** | Snapshot of executed parameters, configuration state, and environment context. | Yes | Must be generated immediately before execution. |
| **report.md** | Narrative or analytical summary describing the run outcome, metrics, and interpretations. | Yes | May be human- or model-authored but must include run ID and timestamp. |
| **approval.json** | Signed attestation record confirming human or automated validation per ADR-0012. | Yes | Must reference corresponding manifest and checksum hashes. |
| **SHA256SUMS.txt** | Integrity registry listing artifact hashes. Each run MAY include its own `SHA256SUMS.txt`, but the root-level file remains authoritative for full-repo verification. | Yes | Updated after each attested run. |
| **manifest.json** or **manifest.md** | Defines falsifiability boundaries, inputs, and expected failure conditions. | Yes | Root file required; per-run files optional but recommended. |  

All files above **MUST** exist in each run folder (`/runs/<RUN_ID>/`), except that the root-level `SHA256SUMS.txt` serves as the canonical registry for repository-wide verification (§4.6).  
All entries **MUST** be immutable once signed and referenced in `SHA256SUMS.txt`.

---

### 6.3 File Naming and Structure Conventions

- Each run directory **MUST** be timestamped or uniquely identified (e.g., `RUN_2025-10-28_001`).  
- Filenames **MUST** use lowercase alphanumeric characters and underscores only.  
- Each file **MUST** contain a metadata header (JSON or YAML front-matter) including:  
  - Run ID  
  - Timestamp (ISO 8601)  
  - Origin role (Orchestrator, Auditor, etc.)  
  - Linked ADR IDs  
  - Provenance lineage references (see below)

---

### 6.4 Provenance Chain and Lineage Requirements

The **Provenance Chain** represents the traceable path connecting:
1. Manifest → Workflow execution → Report → Approval → Archive.  
2. ADR decisions and logs that define or verify each step.

#### Minimum Provenance Links

| Relationship | Requirement |
|---------------|--------------|
| Manifest ↔ Report | The report **MUST** reference the manifest version and falsifiability clause. |
| Report ↔ Approval | The approval record **MUST** include hash references of the report and manifest. |
| Approval ↔ SHA256SUMS | Each approval **MUST** verify against current checksum state. |
| SHA256SUMS ↔ Release | The release process **MUST** include and verify the checksum file. |
| ADR ↔ All | Relevant ADR numbers **MUST** be cited in manifest, report, and approval metadata. |

All provenance references **MUST** be machine-readable and auditable via JSON key paths or Markdown tables.

---

### 6.5 Validation and Versioning Rules

- Artifacts **MUST** conform to JSON or Markdown schemas defined under `/schemas/`.  
- Schema validation **SHOULD** be performed manually for Minimum Compliance, and automatically for Full Compliance (see Adoption Guide).  
- Each artifact revision **MUST** be versioned using semantic tags (`vX.Y.Z`).  
- Any change that affects results **MUST** trigger a new Run folder.  
- Historical artifacts **MUST NOT** be altered; corrections require a superseding Run ID and cross-reference.

---

### 6.6 Cryptographic and Attestation Linkage

- Every artifact **MUST** be signed or hashed according to ADR-0015.  
- The signing authority (human or model) **MUST** be recorded in `approval.json` and linked to `/logs/overrides/` if any manual intervention occurred.  
- Attestation hashes **MUST** match those in `SHA256SUMS.txt`; discrepancies trigger audit flags.

---

### 6.7 Integration with Evidence Registry (ADR-0002)

- Each artifact **MUST** register its existence in the Evidence Registry table (maintained under `/docs/Evidence_Registry.md` or equivalent).  
- The registry **MUST** include:
  - Artifact path  
  - Type (manifest, report, etc.)  
  - Linked ADRs  
  - Hash value  
  - Attestation reference  
- Each registry update **MUST** be recorded in `/logs/workflow/` with a unique entry ID.

---

### 6.8 Future CRI-CORE Hooks

Once CRI-CORE enforcement is active:
- Each artifact type will correspond to a schema module (e.g., `manifest.schema.json`, `approval.schema.json`).  
- Provenance chains will be validated automatically using CRI runtime modules.  
- Manual overrides will trigger provenance-diff checks to confirm trace continuity.

<!-- CRI-TODO: Define schema references and CRI module mappings once CRI-CORE v0.1 is published. -->

**TODO:** Define schema references and CRI module mappings once CRI-CORE Specification v0.1 is published.

---

## 7. Compliance Language

### 7.1 Purpose
This section defines the normative language used throughout the Aurora Workflow Orchestration (AWO) specification.  
The following terms establish the required, recommended, and optional behaviors that determine conformance.

---

### 7.2 Normative Terms

| Keyword | Meaning | Enforcement Implication |
|----------|----------|-------------------------|
| **MUST** | A requirement that is absolutely mandatory for AWO compliance. Implementations lacking this behavior are non-conformant. | Hard validation — failure blocks attestation or release. |
| **SHOULD** | A strong recommendation. Equivalent alternatives are permitted **only** if explicitly documented and justified in logs or ADRs. | Soft validation — warning status logged; manual review required. |
| **MAY** | An optional or discretionary behavior that does not affect compliance. | Informational — no enforcement. |

---

### 7.3 Interpretive Rules

- The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in **RFC 2119 / ISO IEC TR 29110**.  
- All **MUST** clauses are binding for compliance certification under the Aurora Research Initiative (ARI).  
- A **SHOULD** clause may be overridden **only** through a logged exception referencing its justification (see `/logs/overrides/`).  
- A **MAY** clause introduces permitted flexibility and cannot be used to claim non-compliance of another implementation.  
- Deviations from any **MUST** clause **MUST** be documented as a non-conformance record.

---

### 7.4 Mapping of Compliance Levels

| Section | Description | Compliance Level |
|----------|--------------|------------------|
| §3 Roles and Responsibilities | Role declaration and separation of duties | **MUST** |
| §4 Repository Requirements | Directory structure, ADR layout, log subfolders | **MUST** |
| §5 Lifecycle and Run Phases | Sequential execution order and audit flow | **MUST** |
| §6 Artifacts and Provenance Rules | Artifact creation, immutability, hash verification | **MUST** |
| §8 Accountability Matrix | Role–artifact responsibility mapping | **SHOULD** |
| §9 Governance and Attestation | Tagging, checksum maintenance, archival | **MUST** |
| §11 Licensing and Attribution | License files and acknowledgments | **MUST** |
| §12 Future Integration | CRI-CORE hooks and schema mappings | **MAY** |

---

### 7.5 Non-Conformance Handling

- Any violation of a **MUST** clause **MUST** be treated as a **non-compliance event** and logged in `/logs/audits/`.  
- Deviations from a **SHOULD** clause **MUST** be recorded in `/logs/overrides/` with justification.  
- Repeated or uncorrected non-conformances **MUST** trigger re-attestation or run invalidation.  
- Compliance auditors **MAY** issue a variance report summarizing exceptions and resolutions.

---

### 7.6 Certification and Conformance Evidence

- A repository claiming AWO compliance **MUST** include a `COMPLIANCE.md` file or equivalent table summarizing clause-level adherence.  
- The file **SHOULD** include references to specific ADRs, manifests, and run IDs verifying each claim.  
- Attestation signatures in `approval.json` serve as binding statements of compliance at the time of release.

---

## 8. Roles–Artifact Accountability Matrix

### 8.1 Purpose
This section defines the accountability relationships between AWO roles (as specified in §3) and the artifacts produced during the lifecycle (as specified in §6).  
The objective is to ensure that every file, log, and decision is traceable to a responsible role and attested according to the AWO governance standard.

Each artifact **MUST** have:
- A clearly declared **origin role** (who created it).  
- A **reviewing or attesting role** (who verified it).  
- A **governing ADR reference** defining the applicable rules.

---

### 8.2 Role–Artifact Responsibility Matrix

| Artifact | Origin Role(s) | Reviewing Role(s) | Governing ADRs | Compliance Level |
|-----------|----------------|-------------------|----------------|------------------|
| **manifest.json / manifest.md** | Orchestrator | Auditor | 0002, 0012 | **MUST** |
| **workflow_frozen.json** | Orchestrator, Evaluator | Auditor | 0002, 0004 | **MUST** |
| **report.md** | Synthesizer | Critic (optional), Auditor | 0002, 0012 | **MUST** |
| **approval.json** | Auditor | Orchestrator (acknowledgment) | 0012, 0015 | **MUST** |
| **SHA256SUMS.txt** | Orchestrator | Auditor | 0015, 0016 | **MUST** |
| **ADR files** | Orchestrator, Auditor | Orchestrator | 0001–0017 | **MUST** |
| **/logs/workflow/** | Orchestrator | Auditor | 0004 | **MUST** |
| **/logs/audits/** | Auditor | Orchestrator (review only) | 0003, 0013 | **MUST** |
| **/logs/overrides/** | Orchestrator (manual intervention) | Auditor | 0004, 0012 | **SHOULD** |
| **/schemas/** | Orchestrator, Auditor | CRI validator (future) | 0002, 0015 | **MAY** |
| **/templates/** | Orchestrator | N/A | 0011 | **MAY** |
| **/figures/** | Orchestrator | N/A | 0009 | **MAY** |

---

### 8.3 Chain of Custody

All artifacts **MUST** maintain a documented chain of custody that records:
- **Creation timestamp**  
- **Responsible role**  
- **Verification signature or attestation hash**  
- **Referenced ADR(s)**  
- **Linked run ID**

This metadata **MUST** be stored in either:
- File front matter (for Markdown-based artifacts), or  
- Embedded JSON keys (for structured data).

Example metadata block:
```yaml
run_id: RUN_2025-10-28_001
origin_role: Orchestrator
verified_by: Auditor
adr_refs: [0002, 0012]
sha256: "2f7b3e8e..."
timestamp: 2025-10-28T18:21:00Z
```
Example with evidence pointers:
```yaml
run_id: RUN_2025-10-28_001
origin_role: Orchestrator
verified_by: Auditor
adr_refs: [0002, 0012]
sha256: "2f7b3e8e..."
evidence_pointers:
  - path: logs/workflow/2025-10-28_plan.md#L22-L48
  - path: decisions/ADR-0012-human-in-loop-signoff.md
timestamp: 2025-10-28T18:21:00Z
```

### 8.4 Attestation Logic

1) **Primary Attestation**  
- Each artifact requiring human or automated approval (e.g., `approval.json`, `report.md`) **MUST** be signed off by the Auditor role.  
- Signatures may be human-readable (signed-by) or cryptographic (per ADR-0015).

2) **Secondary Acknowledgment**  
- The Orchestrator **SHOULD** acknowledge attested artifacts via changelog or run note entry.  
- This creates a closed validation loop and allows two-party accountability.

3) **Override Case**  
- If the Orchestrator bypasses or modifies an attested artifact, an entry **MUST** be logged in `/logs/overrides/` citing justification and relevant ADR(s).

### 8.5 Accountability Validation (Automated and Manual)

- Automated systems **SHOULD** validate that every artifact in `/runs/` and `/docs/` has both an origin and attesting role recorded.  
- Manual audits **MUST** confirm that metadata matches recorded logs and ADRs.  
- Missing or ambiguous role assignments **MUST** trigger a non-conformance flag under §7.5.  

### 8.6 Role Coverage Summary

| Role | Primary Responsibilities | Secondary Responsibilities | Key Compliance Points |
|------|--------------------------|----------------------------|-----------------------|
| **Orchestrator** | Manage run lifecycle; produce manifests and workflow logs; coordinate attestation. | Review audits; ensure completeness. | §3.2, §4.2, §5, §6 |
| **Evaluator** | Generate and compare outputs from reasoning models. | Assist in `workflow_frozen.json` capture. | §3.2, §5.3 |
| **Auditor** | Perform formal verification; approve or reject artifacts; maintain audit logs. | Validate checksum and signature integrity. | §3.2, §5.4, §6.6 |
| **Synthesizer** | Produce consolidated reports from approved reasoning paths. | Support narrative generation for publication. | §3.2, §5.3 |
| **Critic / Red Team** | Challenge claims to test falsifiability (optional). | N/A | §3.2, §5.2 |

### 8.7 Conformance Evidence

To demonstrate role–artifact compliance:  
- Repositories **MUST** maintain a `ROLE_ATTESTATION.md` or equivalent manifest summarizing each role’s contributions.  
- The file **SHOULD** be updated per release tag and reference ADRs, Run IDs, and hash values.  
- Future CRI-CORE integrations **MAY** automate this process using agent-based signature validation.  

### 8.8 Future Integration Notes

Once CRI-CORE is active:  
- Each role’s attestation will correspond to a schema validator module (e.g., `auditor.schema.json`).  
- The Accountability Matrix will be machine-enforced through the CRI runtime layer.  
- Non-human agents (models) will sign their outputs using embedded identity tokens or deterministic cryptographic fingerprints.  

<!-- CRI-TODO: Define CRI-CORE accountability schema references when CRI Spec v0.1 is released. -->

**TODO**: Define CRI-CORE accountability schema references upon release of CRI Specification v0.1.

---

## 9. Governance and Attestation

### 9.1 Purpose
This section defines how AWO-governed research runs are validated, attested, and archived.  
Attestation provides the binding guarantee that all artifacts within a run are **complete, verified, and reproducible** under human or automated oversight.

All attestations constitute part of the formal governance record of a project and **MUST** be preserved in perpetuity for audit and citation.

---

### 9.2 Core Attestation Requirements

| Requirement | Description | Governing ADRs | Compliance Level |
|--------------|--------------|----------------|------------------|
| **approval.json** | Each run **MUST** include a signed attestation file recording reviewer identity, timestamp, and verdict. | 0012, 0015 | **MUST** |
| **Checksum verification** | The attesting role **MUST** confirm that all artifacts listed in `SHA256SUMS.txt` are valid. | 0015 | **MUST** |
| **Peer confirmation** | Optional secondary review by another role (e.g., Critic or Red Team) **MAY** supplement the attestation. | 0013 | **MAY** |
| **Failure logging** | Any rejected or failed attestation **MUST** be recorded under `/logs/attestation_failures/` with justification and linked run ID. | 0003, 0004 | **MUST** |
| **Immutable record** | Once committed, attestations **MUST NOT** be modified or deleted; amendments require a superseding entry. | 0010 | **MUST** |

---

### 9.3 Attestation Metadata Schema

All `approval.json` files **MUST** conform to a minimal metadata schema for traceability and verification.

```json
{
  "run_id": "RUN_2025-10-28_001",
  "reviewer_role": "Auditor",
  "reviewer_identity": "s.wright@waveframelabs.org",
  "attestation_timestamp": "2025-10-28T21:45:00Z",
  "verdict": "approved",
  "checksum_verified": true,
  "adr_refs": ["0012", "0015"],
  "signature": "base64-encoded digital signature",
  "comments": "Verification completed successfully; no anomalies detected."
}
```

The `signature` field may represent:
- A manual human signature (`signed-by` line in text-based files), or  
- A cryptographic signature generated via OIDC or PGP keypair (ADR-0015).

---

### 9.4 Signature and Verification Workflows

1. **Human Attestation**
   - The **Auditor** reviews all artifacts for integrity, compliance, and falsifiability.
   - Signs `approval.json` manually or via embedded digital identity token.
   - Marks run as `approved` or `rejected`.

2. **Automated Attestation (Future CRI Integration)**
   - A validator module checks artifact hashes, manifest completeness, and schema compliance.
   - Generates deterministic signature via SHA256 + identity token.
   - Writes automated attestation record to `/runs/<id>/approval.json`.

3. **Dual-Signature Option**
   - The **Orchestrator** may co-sign attested runs for dual accountability.
   - Dual signatures are encouraged for formal publication releases.

---

### 9.5 Attestation Failure Handling

- A failed attestation **MUST** generate a markdown entry in `/logs/attestation_failures/` using the following format:

```markdown
# Attestation Failure — RUN_2025-10-28_001
**Date:** 2025-10-28  
**Reviewer:** Auditor  
**Reason:** Checksum mismatch in `report.md`  
**Status:** Rejected  
**Next Action:** Correct artifact and resubmit for attestation  
**ADR References:** 0003, 0012
```

- Failed attestations **MUST NOT** be deleted; they serve as part of the permanent audit trail.
- Corrected runs **MUST** reference the failed run ID in their manifest (`supersedes: RUN_2025-10-28_001`).

---

### 9.6 Governance Records

Each repository **MUST** maintain a persistent log of all attestations, approvals, and failures under `/logs/governance/`.  
These logs **MUST** contain:
- Run ID  
- Reviewer identity  
- Timestamp  
- Attestation verdict  
- Linked ADRs  
- Immutable reference to the attestation artifact

This forms the canonical audit trail for human and automated verification.

---

### 9.7 Governance Roles and Oversight

| Governance Function | Responsible Role | Description |
|----------------------|------------------|-------------|
| **Primary Review** | Auditor | Performs verification and signs `approval.json`. |
| **Secondary Review (Optional)** | Critic / Red Team | Provides peer-level falsifiability challenge. |
| **Governance Record Maintenance** | Orchestrator | Maintains `/logs/governance/` and ensures traceability. |
| **Policy Enforcement** | Aurora Research Initiative (Waveframe Labs) | Oversees alignment of attestation procedures with AWO standard. |

---

### 9.8 Integrity Assurance

- All attestation-related files **MUST** be included in the repository’s root `SHA256SUMS.txt`.  
- Verification of checksums **MUST** occur before tagging a release (§10).  
- Attestation results **MUST** propagate to any derived DOI, Zenodo, or archival metadata.

---

### 9.9 Future Integration Notes

- CRI-CORE will implement attestation as an automated module (`attestation_validator.py`) using deterministic signatures.  
- Each role’s digital identity **WILL** be represented by a unique agent keypair, recorded in the CRI identity ledger.  
- Automated attestation results will trigger governance alerts or webhooks for audit notifications.

<!-- CRI-TODO: Add CRI-CORE schema mapping once `attestation.schema.json` is defined. -->

**TODO:** Add CRI-CORE schema mapping once `attestation.schema.json` is defined.

---

**Governing ADRs:** 0003, 0004, 0010, 0012, 0013, 0015  
**Compliance Level:** MUST

---

## 10. Release and Versioning

### 10.1 Purpose
This section defines the release, versioning, and archival policies that ensure AWO-governed repositories remain immutable, traceable, and verifiable over time.  
Every AWO-compliant release represents a **frozen, reproducible state** of the repository — complete with its documentation, checksums, and attestations.

---

### 10.2 Core Release Requirements

| Requirement | Description | Governing ADRs | Compliance Level |
|--------------|--------------|----------------|------------------|
| **Semantic Versioning** | All releases **MUST** follow the semantic versioning convention `vMAJOR.MINOR.PATCH` (e.g., `v1.2.1`). | 0010 | **MUST** |
| **Artifact Immutability** | Once tagged, all artifacts within the release (PDFs, manifests, reports, checksums) **MUST NOT** be altered. | 0010, 0014 | **MUST** |
| **Checksum Registry** | Each release **MUST** include `SHA256SUMS.txt` with verified hashes for all distributed files. | 0015 | **MUST** |
| **DOI Linkage** | Every public release **SHOULD** include a DOI via Zenodo or an equivalent archival service. | 0010, 0017 | **SHOULD** |
| **Release Attachments** | The release **MUST** attach final PDF artifacts, integrity file, and citation metadata. | 0010, 0016 | **MUST** |
| **Change Documentation** | The `CHANGELOG.md` **MUST** include an entry describing new or modified artifacts. | 0010 | **MUST** |

---

### 10.3 Tagging Policy

1. **Tag Naming Convention**
   - Format: `v<major>.<minor>.<patch>`  
     Examples: `v1.2.1`, `v2.0.0`  
   - Tags **MUST** be unique and immutable.  
   - Pre-release or test tags (e.g., `v1.2.1-beta`) **MAY** be used internally but **MUST NOT** be cited as archival releases.

2. **Tag Commit Association**
   - The tag **MUST** correspond to the exact commit that generated the release artifacts and `SHA256SUMS.txt` file.
   - Git commit message **SHOULD** match the release title in CHANGELOG.

3. **Amended Releases**
   - If a critical fix is required post-publication, a **new patch version** (e.g., `v1.2.2`) **MUST** be issued.
   - Reusing or overwriting tags constitutes a non-compliance event (§7.5).

---

### 10.4 Artifact Attachment Policy

Each release **MUST** attach the following verified files to its GitHub or archival entry:

| File | Description |
|------|--------------|
| `AWO_Method_Spec_<ver>.pdf` | Finalized Method Specification document. |
| `AWO_Whitepaper_<ver>.pdf` | Finalized Whitepaper. |
| `SHA256SUMS.txt` | Integrity file listing all hashes. |
| `CITATION.cff` | Machine-readable citation metadata. |
| `CHANGELOG.md` | Historical record of updates. |
| `approval.json` (optional) | Attestation record, if release represents an approved run. |

All attachments **MUST** match the recorded checksums in `SHA256SUMS.txt`.

---

### 10.5 Checksum Regeneration Workflow

Before final tagging, the following checksum verification process **MUST** occur:

1. Generate fresh checksums for all distributable files:
   ```bash
   sha256sum docs/*.pdf > SHA256SUMS.txt
   sha256sum CITATION.cff >> SHA256SUMS.txt
   sha256sum CHANGELOG.md >> SHA256SUMS.txt
   ```
2. Verify against any previous version to confirm consistency.  
3. Commit updated `SHA256SUMS.txt` prior to tagging.  
4. Attest checksum integrity via `approval.json` (§9).

The checksum process ensures content-addressable integrity across all archived artifacts.

---

### 10.6 DOI Registration and Archival

- Public releases **SHOULD** be archived with a persistent DOI through Zenodo or equivalent repository.  
- Each DOI record **MUST** reference:
  - Repository URL and commit hash  
  - Release tag (e.g., `v1.2.1`)  
  - Author and ORCID metadata  
  - Associated artifacts (PDFs, `SHA256SUMS.txt`, `CITATION.cff`)

**Zenodo Integration Notes:**
- Zenodo automatically version-links new uploads under the same “concept DOI.”  
- AWO releases **MUST** maintain continuity with the concept DOI established at project initiation.  
- If account merges or DOI conflicts occur, the concept DOI **MUST** be treated as authoritative (§README).

---

### 10.7 Archival Protocol

1. **Release Creation**
   - Verify all governance and attestation steps complete (§9).  
   - Ensure all artifacts have valid checksums.  
   - Commit all documentation updates.  

2. **Tag and Publish**
   - Tag repository with final version.  
   - Attach all required artifacts.  
   - Publish release through GitHub and/or Zenodo.  

3. **Post-Publication Lock**
   - No further changes permitted to tagged commit.  
   - Only errata or new minor/patch versions may follow.  

---

### 10.8 Example Release Entry

```markdown
# AWO v1.2.1 — Documentation & Accessibility Finalization
Release Date: 2025-10-28  
Maintainer: Waveframe Labs  
Contact: s.wright@waveframelabs.org  

Overview:
Finalized documentation for Aurora Workflow Orchestration (AWO) under Waveframe Labs governance, introducing governance logs, checksum verification, and final archival compliance.  

Included Artifacts:
- AWO_Method_Spec_v1.2.1.pdf  
- AWO_Whitepaper_v1.1.1.pdf  
- SHA256SUMS.txt  
- CITATION.cff  
- CHANGELOG.md  

DOI: 10.5281/zenodo.17013612
```

---

### 10.9 Compliance Verification

Each release **MUST** demonstrate the following before publication:

- [x] Attestation approved and logged (§9)  
- [x] `SHA256SUMS.txt` regenerated and verified  
- [x] `CHANGELOG.md` updated with release details  
- [x] Artifacts attached to GitHub and/or Zenodo  
- [x] DOI record cross-linked to release tag  
- [x] Governance logs reflect approval event
- [x] Evidence pointers resolvable for claim-affecting artifacts (§1.6, §4.3).

---

**Governing ADRs:** 0010, 0014, 0016, 0017  
**Compliance Level:** MUST  

---

## 11. Licensing and Attribution

### 11.1 Purpose
This section defines the licensing and attribution standards that govern the use, distribution, and citation of Aurora Workflow Orchestration (AWO) materials.  
AWO uses a **dual-license model** to separate executable and textual components, ensuring that both source code and documentation remain openly accessible while maintaining clear intellectual property boundaries.

---

### 11.2 Dual Licensing Structure

| Component Type | License | Description | Governing ADR | Compliance Level |
|----------------|----------|--------------|----------------|------------------|
| **Source Code** | Apache 2.0 | Grants open use, modification, and distribution rights for all executable and workflow logic. | 0006 | **MUST** |
| **Documentation & Text** | CC BY 4.0 | Allows reuse, adaptation, and redistribution with required attribution. | 0006, 0017 | **MUST** |

This separation ensures that code implementations can be integrated into open infrastructure projects, while research documentation remains attributable to its original author and institution.

---

### 11.3 Attribution Requirements

All derivative works, redistributions, or publications referencing AWO materials **MUST** include the following attribution fields:

| Field | Description | Example |
|--------|-------------|----------|
| **Author** | Full name of primary maintainer. | *Shawn C. Wright* |
| **Affiliation** | Organization or project under which the work is governed. | *Waveframe Labs / Aurora Research Initiative* |
| **ORCID** | Persistent researcher identifier. | 0009-0006-6043-9295 |
| **Concept DOI** | Persistent identifier for the overall project lineage. | 10.5281/zenodo.17013612 |
| **License Notice** | Statement of applicable licenses. | “Code licensed under Apache 2.0; Documentation under CC BY 4.0.” |

Attribution **MUST** appear in at least one of the following locations:
- The repository `README.md`
- Any redistributed documentation or derivative works
- Metadata entries in DOI or preprint systems
- Published works referencing AWO as a reproducibility method

---

### 11.4 Required License Files

Each AWO-compliant repository **MUST** include the following license files at its root:

| File | Description |
|------|--------------|
| `LICENSE` | The Apache 2.0 license text governing executable content. |
| `LICENSE-CC-BY-4.0.md` | The Creative Commons Attribution 4.0 license text governing documentation. |
| `NOTICE` *(optional)* | May include additional acknowledgments or third-party dependencies. |

These license files **MUST NOT** be modified except to update copyright years or maintainers.

---

### 11.5 Attribution Metadata Schema

To support automated validation and citation generation, AWO-compliant repositories **SHOULD** maintain structured attribution metadata in JSON or YAML format.

Example (`attribution.json`):

```json
{
  "project": "Aurora Workflow Orchestration (AWO)",
  "author": "Shawn C. Wright",
  "affiliation": "Waveframe Labs / Aurora Research Initiative",
  "orcid": "0009-0006-6043-9295",
  "concept_doi": "10.5281/zenodo.17013612",
  "licenses": {
    "code": "Apache-2.0",
    "documentation": "CC-BY-4.0"
  },
  "repository_url": "https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration",
  "release_tag": "v1.2.1",
  "attestation_status": "approved"
}
```

This metadata **MAY** be used by CRI-CORE to auto-generate citation badges, compliance checks, and DOI payloads.

---

### 11.6 Redistribution and Derivative Works

- Redistribution of modified AWO code **MUST** preserve the Apache 2.0 notice.  
- Redistribution of modified documentation **MUST** include visible attribution to the original author and DOI.  
- Any derivative research or software **SHOULD** clearly indicate whether it remains AWO-compliant or diverges from the standard.  
- Repositories using AWO as a framework **MAY** include their own attribution schema extending the above fields.

---

### 11.7 License Enforcement and Governance

Waveframe Labs retains governance authority over the AWO standard under the **Aurora Research Initiative (ARI)**, as established in ADR-0017.  
Compliance with licensing terms ensures long-term reproducibility, traceability, and authorship integrity across derivative projects.

Violations or ambiguities regarding licensing **MUST** be documented in `/logs/governance/` and resolved through governance review (§9).

---

**Governing ADRs:** 0006, 0014, 0017  
**Compliance Level:** MUST

---

## 12. Falsifiability Manifests

### 12.1 Purpose
Falsifiability is the foundation of AWO’s reproducibility standard.  
Every research run **MUST** define its disproof criteria before execution to prevent post hoc reasoning or unverifiable outcomes.  
The falsifiability manifest ensures each run begins with explicit hypotheses, boundaries, and measurable success conditions.

---

### 12.2 Core Manifest Requirements

| Requirement | Description | Governing ADRs | Compliance Level |
|--------------|--------------|----------------|------------------|
| **Manifest Presence** | Each run **MUST** include a `manifest.json` or `manifest.md` file in its directory. | 0002 | **MUST** |
| **Disproof Criteria** | Each manifest **MUST** define falsification conditions for all primary claims. | 0002 | **MUST** |
| **Hypothesis Statement** | Each manifest **MUST** declare the specific hypothesis being tested. | 0002 | **MUST** |
| **Acceptance Thresholds** | The manifest **MUST** define quantitative or qualitative acceptance boundaries. | 0002 | **MUST** |
| **Known Risks** | Each manifest **SHOULD** include a list of known limitations, uncertainties, or external dependencies. | 0002 | **SHOULD** |
| **Experimental Plan** | Each manifest **MUST** describe the intended sequence of actions or analyses. | 0002 | **MUST** |

---

### 12.3 Example Falsifiability Manifest (`manifest.json`)

```json
{
  "run_id": "RUN_2025-10-28_001",
  "title": "Entropy-Driven Expansion Model Validation",
  "hypothesis": "Cosmological expansion rate correlates with entropy gradient across horizon boundaries.",
  "predicted_outcomes": [
    "Measured entropy growth rate exceeds geometric expansion rate.",
    "Entropy variance remains bounded within ±3σ of model prediction."
  ],
  "disproof_criteria": [
    "Entropy gradient fails to correlate with Hubble parameter over observed intervals.",
    "Simulated entropy trajectory diverges beyond tolerance threshold for three consecutive iterations."
  ],
  "acceptance_thresholds": {
    "correlation_coefficient_min": 0.8,
    "entropy_growth_tolerance": 0.05
  },
  "experimental_plan": "Simulate entropic horizon model under varying initial conditions; compare observed entropy evolution against predicted rates.",
  "known_risks": [
    "Limited data resolution at high redshift values.",
    "Numerical instability in early-run entropy estimations."
  ],
  "created_by": "Orchestrator",
  "verified_by": "Auditor",
  "adr_refs": ["0002", "0012"],
  "timestamp": "2025-10-28T22:45:00Z"
}
```

---

### 12.4 Manifest Structure and Placement

Each run **MUST** store its falsifiability manifest in the root of its `/runs/<run_id>/` directory.  
Example structure:

```
/runs/
 ├── RUN_2025-10-28_001/
 │    ├── manifest.json
 │    ├── workflow_frozen.json
 │    ├── report.md
 │    ├── approval.json
 │    └── SHA256SUMS.txt
```

Each manifest file **MUST** be included in checksum verification (§10.5) and referenced in its corresponding attestation (§9).

---

### 12.5 Manifest Schema Definition

The following schema defines the minimum required fields for JSON-based manifests:

```json
{
  "$schema": "https://schema.waveframe.org/awo/manifest.schema.json",
  "title": "AWO Falsifiability Manifest",
  "type": "object",
  "properties": {
    "run_id": {"type": "string"},
    "hypothesis": {"type": "string"},
    "predicted_outcomes": {"type": "array", "items": {"type": "string"}},
    "disproof_criteria": {"type": "array", "items": {"type": "string"}},
    "acceptance_thresholds": {"type": "object"},
    "experimental_plan": {"type": "string"},
    "known_risks": {"type": "array", "items": {"type": "string"}},
    "created_by": {"type": "string"},
    "verified_by": {"type": "string"},
    "adr_refs": {"type": "array", "items": {"type": "string"}},
    "timestamp": {"type": "string", "format": "date-time"}
  },
  "required": ["run_id", "hypothesis", "disproof_criteria", "acceptance_thresholds", "experimental_plan"]
}
```

---

### 12.6 Manual vs. Automated Compliance

| Workflow Type | Manifest Creation | Verification Method | Example Implementation |
|----------------|------------------|---------------------|-------------------------|
| **Manual AWO Runs** | Authored by Orchestrator before execution. | Verified by Auditor post-run. | `manifest.md` signed manually (instantiated from `templates/falsifiability-manifest.md`). |
| **CRI-CORE Integrated Runs** | Auto-generated from hypothesis input. | Validated by schema engine (`manifest_validator.py`). | `manifest.json` validated automatically. |

---

### 12.7 Governance and Traceability

- Each falsifiability manifest **MUST** reference its governing ADRs (typically 0002 and 0012).  
- The manifest’s hash value **MUST** be included in the `SHA256SUMS.txt`.  
- Any revisions to the manifest **MUST** be versioned with a unique timestamp and included in governance logs (§9).  
- Superseded manifests **MUST** reference the previous run ID (`supersedes` field).

---

### 12.8 Future Integration Notes

- CRI-CORE will implement automated manifest validation using deterministic schemas.  
- Falsifiability data may be visualized in the CRI dashboard for longitudinal tracking of epistemic robustness.  
- Future schema versions will include extended metadata such as probabilistic priors and entropy-weighted predictions.

<!-- CRI-TODO: Hook to CRI manifest validator once available. -->

**TODO:** Hook to CRI manifest validator once available.

---

**Governing ADRs:** 0002, 0012  
**Compliance Level:** MUST

---

## 13. Conformance Checklist

### 13.1 Purpose
This section defines the mandatory verification steps a repository **MUST** complete before claiming compliance with the Aurora Workflow Orchestration (AWO) standard.  
The checklist ensures each implementation maintains complete traceability, reproducibility, and documentation integrity across all lifecycle phases.

This checklist also serves as the **baseline schema** for future automated compliance validation under CRI-CORE.

---

### 13.2 Repository Conformance Requirements

Each repository claiming AWO compliance **MUST** satisfy the following conditions:

| # | Requirement | Verification Method | Governing ADRs | Compliance Level |
|---|--------------|--------------------|----------------|------------------|
| 1 | **Standard directory structure present** | Verify `/docs/`, `/logs/`, `/runs/`, `/schemas/`, `/decisions/`, and `/templates/` directories exist. | 0011 | **MUST** |
| 2 | **At least one signed run in `/runs/`** | Confirm presence of `approval.json` with valid attestation (§9). | 0012, 0015 | **MUST** |
| 3 | **ADRs linked and numbered (0001–0017)** | Verify all referenced ADRs exist and correspond to governing sections. | 0001–0017 | **MUST** |
| 4 | **Falsifiability manifest present** | Ensure each run contains `/runs/<run_id>/falsifiability-manifest.md` (instantiated from `templates/falsifiability-manifest.md`) **or** `manifest.json`. | 0002, 0012 | **MUST** |
| 5 | **SHA256SUMS.txt present and verified** | Regenerate and compare to recorded hash file (§10.5). | 0015 | **MUST** |
| 6 | **CHANGELOG includes version reference** | Confirm most recent version is logged (§10.9). | 0010 | **MUST** |
| 7 | **README cross-links all core documents** | README must reference the Whitepaper, Method Spec, and Adoption Guide. | 0017 | **MUST** |
| 8 | **Governance and attestation logs maintained** | Verify `/logs/governance/` and `/logs/attestation_failures/` directories exist with entries. | 0003, 0012 | **MUST** |
| 9 | **Licensing files present and unmodified** | Confirm `LICENSE` and `LICENSE-CC-BY-4.0.md` exist and match canonical text (§11.4). | 0006, 0017 | **MUST** |
| 10 | **PDF build workflows operational** | Confirm automated GitHub Actions produce valid PDFs. | 0016 | **MUST** |
| 11 | **ADR citations consistent across documents** | Cross-check citations in Method Spec, Whitepaper, and ADR index. | 0017 | **SHOULD** |
| 12 | **Repository integrity registry updated** | Ensure `SHA256SUMS.txt` includes all critical files (PDFs, manifests, governance logs). | 0015 | **MUST** |
| 13 | **Compliance declaration committed** | Add `/docs/AWO_Compliance_Report.md` or equivalent summary signed by Orchestrator. | 0012, 0017 | **MUST** |  
| 14 | Evidence pointers present and resolvable | Confirm at least one pointer exists for each claim-affecting artifact and resolves to /logs/workflow/, /logs/audits/, or an ADR. | 0003, 0004 | MUST |  

---

### 13.3 Optional Extended Compliance

For repositories implementing advanced reproducibility or CRI integrations, the following **optional** checks apply:

| # | Requirement | Verification Method | Compliance Level |
|---|--------------|--------------------|------------------|
| 1 | **Automated validation via CRI-CORE** | Validator confirms compliance schema. | **MAY** |
| 2 | **Dual attestation present** | Both Orchestrator and Auditor signatures recorded in approval file. | **SHOULD** |
| 3 | **DOI registration complete** | DOI record publicly accessible and linked to release. | **SHOULD** |
| 4 | **Role-attestation matrix documented** | `/docs/ROLE_ATTESTATION.md` includes all artifacts and responsible roles (§8.7). | **SHOULD** |
| 5 | **Governance report exported** | Governance logs compiled into `GOVERNANCE_SUMMARY.md`. | **MAY** |

---

### 13.4 Automated Compliance Schema (Future Integration)

The following JSON schema will define minimum conformance structure for automated validation in CRI-CORE v0.1:

```json
{
  "$schema": "https://schema.waveframe.org/awo/compliance.schema.json",
  "type": "object",
  "properties": {
    "repository_structure": {"type": "boolean"},
    "signed_run_present": {"type": "boolean"},
    "falsifiability_manifest_present": {"type": "boolean"},
    "checksum_verified": {"type": "boolean"},
    "governance_logs_present": {"type": "boolean"},
    "licenses_valid": {"type": "boolean"},
    "changelog_updated": {"type": "boolean"},
    "pdf_build_verified": {"type": "boolean"},
    "compliance_report_signed": {"type": "boolean"}
  },
  "required": [
    "repository_structure",
    "signed_run_present",
    "falsifiability_manifest_present",
    "checksum_verified",
    "governance_logs_present",
    "licenses_valid",
    "changelog_updated",
    "pdf_build_verified",
    "compliance_report_signed"
  ]
}
```

---

### 13.5 Manual Compliance Verification

Manual audits **MUST** be completed prior to tagging a release (§10.7).  
Auditors **SHOULD** verify all checklist items and record the verification event in `/logs/governance/`.  
A summary report **MUST** be attached to the release as `AWO_Compliance_Report.md` with signatures and timestamps.

Example:

```markdown
# AWO v1.2.1 Compliance Verification Report
**Auditor:** Waveframe Labs  
**Date:** 2025-10-28  
**Summary:**  
All required AWO compliance checks completed. Repository verified as reproducible and fully documented under Aurora Research Initiative governance.

**Result:** PASS  
**Linked ADRs:** 0001–0017  
**Next Review:** 2026-04-01
```

---

### 13.6 Future Integration Notes

- CRI-CORE will provide automated compliance validation using `compliance_validator.py`.  
- Compliance logs will be serialized as JSON outputs for downstream reproducibility dashboards.  
- The compliance report will serve as a verifiable artifact in the provenance ledger.

<!-- CRI-TODO: Publish compliance.schema.json and validator module names. -->

**Governing ADRs:** 0001–0017  
**Compliance Level:** MUST

---

## Appendix C — Rationale Summary

### Purpose
This appendix provides concise justifications for the normative rules defined in the Aurora Workflow Orchestration (AWO) Method Specification v1.2.1.  
Each rule exists to enforce reproducibility, traceability, and falsifiability across human–AI research workflows.  
Rationales are provided to ensure interpretability, not negotiation.

---

### C.1 Repository and Structural Rules

| Section | Rule Summary | Rationale |
|----------|---------------|------------|
| §4 | Standardized repository structure | Guarantees every AWO-compliant repository can be audited and navigated identically, regardless of domain or implementer. |
| §5 | Defined run lifecycle | Aligns human and machine workflows through four reproducible stages, ensuring every claim can be traced back to its originating phase. |
| §6 | Artifact requirements | Establishes a verifiable minimum output set, ensuring reproducibility without reliance on institutional infrastructure. |
| §10 | Release immutability | Prevents retroactive edits or silent version drift that would undermine traceability. |

---

### C.2 Governance and Verification

| Section | Rule Summary | Rationale |
|----------|---------------|------------|
| §7 | Compliance tiering (MUST/SHOULD/MAY) | Enables multi-level enforcement: rigid for auditability, flexible for experimentation. |
| §9 | Governance and attestation | Replaces subjective trust with explicit validation. Human and automated attestations are recorded as immutable evidence. |
| §13 | Conformance checklist | Defines what “compliant” means in operational terms, enabling reproducibility testing by third parties. |

---

### C.3 Falsifiability and Epistemic Integrity

| Section | Rule Summary | Rationale |
|----------|---------------|------------|
| §12 | Falsifiability manifests | Enforces Popperian rigor: all hypotheses must declare their disproof conditions *before* execution. |
| §2 | Core definitions | Ensures shared language between human and AI collaborators; removes ambiguity from governance terms. |
| §3 | Roles | Encodes epistemic separation of duties (Orchestrator, Auditor, Synthesizer, etc.), preventing self-validation bias. |

---

### C.4 Provenance and Cryptographic Integrity

| Section | Rule Summary | Rationale |
|----------|---------------|------------|
| §6 | SHA256SUMS registry | Makes artifact integrity measurable, not assumed. Hashes serve as objective identity tokens for every research output. |
| §9 | Approval.json requirement | Establishes a human–machine trust boundary through verifiable signatures and timestamps. |
| §10 | DOI and checksum coupling | Ensures citations reference *frozen* states of the repository, binding publication to verifiable data. |

---

### C.5 Documentation and Governance Continuity

| Section | Rule Summary | Rationale |
|----------|---------------|------------|
| §1 | Normative references | Maintains audit lineage and cross-references for every governing ADR and artifact. |
| §8 | Governance under Aurora Research Initiative (ARI) | Provides institutional continuity and governance without dependence on centralized academic structures. |
| §11 | Licensing duality | Separates code execution rights from documentation reuse rights, ensuring open reproducibility while protecting attribution. |

---

### C.6 Meta-Level Rationales

1. **Human Oversight** — Ensures AI outputs remain accountable to human judgment (§9, §13).  
2. **Falsifiability** — Enforces scientific rigor before computation begins (§12).  
3. **Auditability** — Guarantees all claims, data, and reasoning have verifiable origins (§4–§10).  
4. **Provenance Continuity** — Preserves the evidentiary chain from initial concept to publication (§5–§10).  
5. **Interoperability** — Enables AWO to serve as a meta-standard adaptable across disciplines (§4, §5).  
6. **Institutional Independence** — Demonstrates that reproducible governance can exist outside traditional peer review (§8, §11).  

---

### C.7 Forward Alignment with CRI-CORE

The rationale structure also prepares AWO for integration with **CRI-CORE**, which will automate validation of these rules through schemas and attestation gates.  
Each AWO rule maps directly to a forthcoming compliance schema within the CRI runtime, ensuring continuous auditability beyond manual enforcement.

---

**End of Appendix C — Rationale Summary (AWO v1.2.1)**

---

**End of Specification — Aurora Workflow Orchestration (AWO) v1.2.1 Scaffold**

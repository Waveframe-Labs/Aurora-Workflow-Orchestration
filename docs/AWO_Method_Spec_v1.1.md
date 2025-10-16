# Aurora Workflow Orchestration (AWO) — Method Specification v1.1

**Author:**  
Shawn C. Wright  

**Affiliation:**  
Aurora Research Initiative, Waveframe Labs (Independent Researcher)  

**Version:**  
1.1  ·  **Date:** 2025-10-07  

**DOI:**  
[10.5281/zenodo.17345552](https://doi.org/10.5281/zenodo.17345552)  

**License:**  
CC BY 4.0 (text) · Apache-2.0 (code)

---

### Purpose  
Define a repeatable, auditable method for AI-assisted work so that a third party can reproduce both the process and the outcomes.

---

## Scope
AWO governs how to structure AI-assisted research and analysis into falsifiable claims, audited iterations, and immutable, citable releases.

AWO defines the **methodological layer**; CRI-CORE provides the **automation layer** that executes and verifies it.

---

## Normative Requirements (must / should)

1. **Falsifiability** — Every claim MUST have a concrete test that could prove it wrong (dataset / criteria / procedure).  
2. **Full Logging** — Reasoning and outputs MUST be logged at each step (draft → audit → synthesis → decision).  
3. **Independent Audit** — Key steps MUST be audited by separate agents: logic check, data validation, peer critique.  
4. **Rejection Loop** — If a claim or output fails audit, it MUST be revised or withdrawn (no defending without evidence).  
5. **Portability** — Artifacts SHOULD be domain-agnostic (templates, checklists) so the method reuses across domains.

---

## Roles

- **Orchestrator (Human):** frames questions, sets falsifiability criteria, resolves conflicts, approves releases.  
- **Main Model (Continuity):** maintains project memory and produces the primary draft / synthesis.  
- **Auxiliary Auditors (Independent):**  
  - *Logic Auditor* — checks internal consistency, contradictions, missing steps.  
  - *Data Validator* — tests claims against data, metrics, thresholds.  
  - *Peer Critic* — adversarial review for scope creep, unsupported claims, lack of clarity.

---

## Core Artifacts (per repository)

- **Falsifiability Manifest** (`/docs/FALSIFIABILITY_MANIFEST.md`) — claim IDs, tests, datasets, thresholds, and pass/fail status.  
- **Workflow Logs** (`/logs/*.md`) — dated entries with actions, lessons, and next steps.  
- **Decision Records (ADRs)** (`/decisions/*.md`) — context, decision, consequences, and links to evidence.  
- **Evidence Registry** (`/figures`, `/notebooks`, `/data`) — referenced from manifests and ADRs.  
- **Release Artifacts** — `CHANGELOG.md`, `CITATION.cff`, `.zenodo.json`, Git tag, Zenodo DOIs (concept + version).

---

## Lifecycle (one iteration)

0. **Setup:** define claims, add baselines to the Falsifiability Manifest, create `templates/`, assign auditors via Model Roster.  
1. **Draft (Main Model):** produce reasoning / output; tag with claim IDs.  
2. **Audit (Independent):**  
   - Logic Auditor → pass/fail + notes  
   - Data Validator → pass/fail + metrics  
   - Peer Critic → pass/fail + critique  
3. **Synthesis (Main Model):** reconcile audit outputs; revise claims or methods.  
4. **Decision:** record outcome in ADR (accepted / rejected / superseded) with links to evidence and logs.  
5. **Evidence Capture:** save figures, notebooks, datasets; update Manifest status.  
6. **Release Gate:** run Release Checklist, cut a tag, archive on Zenodo.

---

## Logging Schema (minimum fields)

- **Log entry:** date, what I did, what I learned, next step, skills  
- **Audit record:** claim ID, auditor, check type (logic | data | peer), criteria, result, evidence links

---

## Rejection Handling
Any failed audit → revise draft or withdraw claim.  
Update manifest status and ADR rationale.  
No appeals without new evidence.

---

## Portability Guidelines
- Keep templates generic; avoid domain-specific jargon in checklists.  
- Parameterize datasets and metrics in the manifest.  
- Use the **Model Roster** to swap models or auditors without changing the process.

---

## Conformance Checklist
- [ ] Manifest exists with at least one falsifiable claim and test procedure.  
- [ ] Logs present for each iteration (draft → audit → synthesis → decision).  
- [ ] At least one ADR captures a non-trivial trade-off or decision.  
- [ ] Release artifacts present; latest tag archived with Concept + Version DOIs.

---

## Example Reference
- **Waveframe v4.0.5:** case study demonstrating AWO artifacts and archived, citable release.

---

## File and Folder Conventions
- `/templates/*.md|yaml` — reusable templates (manifest, audit record, ADR, release checklist).  
- `/schemas/*.json` — validation and reproducibility enforcement.  
- `/decisions/` — governance layer.  
- `/logs/` — execution layer.  
- `/docs/` — whitepapers, manifests, and specifications.

---

**Maintained by Waveframe Labs**  
📧 `swright@waveframelabs.org`  
🔗 [waveframelabs.org](https://waveframelabs.org) *(coming soon)*

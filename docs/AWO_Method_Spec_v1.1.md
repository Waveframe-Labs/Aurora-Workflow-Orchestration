# AI Workflow Orchestration (AWO) — Method Specification v1.1

**Purpose:** Define a repeatable, auditable method for AI‑assisted work so that a third party can reproduce the process and outcomes.

## Scope
AWO governs how to structure AI‑assisted research/analysis into falsifiable claims, audited iterations, and immutable, citable releases.

## Normative Requirements (must/should)
1. **Falsifiability** — Every claim MUST have a concrete test that could prove it wrong (dataset/criteria/procedure).  
2. **Full Logging** — Reasoning and outputs MUST be logged at each step (draft → audit → synthesis → decision).  
3. **Independent Audit** — Key steps MUST be audited by separate agents: logic check, data/criteria validation, and peer critique.  
4. **Rejection Loop** — If a claim or output fails audit, it MUST be revised or withdrawn (no defending without evidence).  
5. **Portability** — Artifacts SHOULD be domain‑agnostic (templates, checklists) so the method reuses across domains.

## Roles
- **Orchestrator (Human):** frames questions, sets falsifiability criteria, resolves conflicts, approves releases.
- **Main Model (Continuity):** maintains project memory and produces the primary draft/synthesis.
- **Auxiliary Auditors (Independent):**
  - *Logic Auditor* — checks internal consistency, contradictions, missing steps.
  - *Data Validator* — tests claims against data/metrics/thresholds.
  - *Peer Critic* — adversarial review for scope creep, unsupported claims, clarity.

## Core Artifacts (per repo)
- **Falsifiability Manifest** (`/docs/FALSIFIABILITY_MANIFEST.md`) — IDs, tests, datasets, thresholds, status.
- **Workflow Logs** (`/logs/*.md`) — dated entries with actions, lessons, next steps, skills.
- **Dialogue Logs** (`/logs/dialogue/*.md`) — curated excerpts linking model messages to decisions (claim IDs, audit results).
- **Decision Records (ADRs)** (`/decisions/*.md`) — context, decision, status, consequences, links.
- **Evidence Registry** (`/figures`, `/notebooks`, `/data`) — referenced from the manifest and logs.
- **Release Artifacts** — `CHANGELOG.md`, `CITATION.cff`, `.zenodo.json`, Git tag, Zenodo DOIs (concept + version).

## Lifecycle (one iteration)
0. **Setup:** define claims; add baselines to Falsifiability Manifest; create `templates/` and choose auditors (Model Roster).
1. **Draft (Main Model):** produce reasoning/output; tag with claim IDs.
2. **Audit (Independent):**
   - Logic Auditor → pass/fail + notes
   - Data Validator → pass/fail + metrics
   - Peer Critic → pass/fail + critique
3. **Synthesis (Main Model):** reconcile audit outputs; revise claims or methods.
4. **Decision:** record outcome in ADR (accepted/rejected/superseded) with links to evidence and logs.
5. **Evidence capture:** save figures, notebooks, datasets; update Falsifiability Manifest status.
6. **Release gate (when applicable):** run Release Checklist; cut a tag; archive on Zenodo.

## Logging Schema (minimum fields)
- *Log entry:* date, what I did, what I learned, next step, skills
- *Dialogue excerpt:* timestamp, role (model/human), model name, claim IDs, decision link
- *Audit record:* claim ID, auditor, check type (logic|data|peer), criteria, result, evidence links

## Rejection Handling
- Any failed audit → revise draft or withdraw claim. Update manifest status and ADR rationale. No “appeals” without new evidence.

## Portability Guidelines
- Keep templates generic. Avoid domain‑specific jargon in checklists. Parameterize datasets/metrics in the manifest.
- Use the **Model Roster** to swap models/agents without changing the process.

## Conformance Checklist
- [ ] Manifest exists with at least one falsifiable claim and test procedure
- [ ] Logs present for each iteration (draft → audit → synthesis → decision)
- [ ] Dialogue excerpts link audits to decisions
- [ ] At least one ADR captures a non‑trivial tradeoff/decision
- [ ] Release artifacts present; latest tag archived with Concept + Version DOIs

## Example Reference
- Waveframe v4.0.5: case study showing AWO artifacts and an archived, citable release.

## File/Folder Conventions
- `/templates/*.md|yaml` — reusable scaffolds
- `/logs/YYYY-MM-DD.md` — daily/cluster logs
- `/logs/dialogue/ITERATION-XX.md` — curated excerpts
- Claim IDs formatted as `CLM-001`, `CLM-002`, ...

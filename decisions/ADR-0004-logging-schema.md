# ADR-0004 — Logging Schema & Locations

## Status
Accepted — 2025-10 (Revised for AWO v1.2.1)

## Context
AWO’s reproducibility depends on consistent, queryable logging.  
Logs constitute the **epistemic record** of all actions and validations across the workflow.

We distinguish between:
- **Workflow logs** — factual, time-ordered records of what was done, when, and why.  
- **Audit logs** — independent validation, critique, and rejection reports authored by auditors or automated review agents.  
- **Override logs** — records of manual interventions or deviations from automated or normative behavior.

Without a clear schema and folder layout, logs risk fragmentation or silent overrides, undermining auditability and attestation integrity.

---

## Decision

The repository **must** maintain the following log structure:

| Folder | Purpose |
|---------|----------|
| `/logs/workflow/` | Factual project steps and internal reasoning chronology. |
| `/logs/audits/` | Independent validation reports, rejection notices, or challenge results. |
| `/logs/overrides/` | Explicit records of human-in-the-loop or orchestrator overrides of automated consensus, including justification and ADR linkage. |

### Minimum Fields per Log Entry
Each log entry (Markdown or JSONL) **must** contain at least:

- **Date / Timestamp**  
- **Context / Event Description**  
- **Participants** (human, model, or hybrid roles)  
- **Artifacts Affected**  
- **Decision or Impact Summary**  
- **Status** (`accepted`, `revised`, `rejected`, `overridden`, `pending`)  
- **Linked References** (`ADR-####`, `RUN_ID`, `ATT_ID`)

A rolling summary file (`WORKFLOW_LOG.md`) may exist at the root of `/logs/` for navigation, but individual entries must remain immutable and timestamped.

### Override Log Protocol
- Each manual override **must** reference the initiating actor’s role (per Section 3 of the Method Spec).  
- Each override **must** cite the corresponding **ADR-0012 (Human-in-Loop Validation)** clause that authorizes the intervention.  
- Attestation events related to overrides **must** reference **ADR-0015 (Attestation Integration & Cryptographic Signing)** to ensure provenance continuity.

---

## Consequences
- Ensures every action, override, or validation is traceable to an accountable record.  
- Preserves the distinction between **execution**, **verification**, and **exception handling**.  
- Allows auditors to reconstruct reasoning lineage without ambiguity.  
- Enforces procedural discipline: contributors cannot bypass logging or silently alter prior records.

---

## References
- ADR-0001 — Flagship Positioning  
- ADR-0003 — Audit Gates & Rejection Loop  
- ADR-0012 — Human-in-Loop Validation  
- ADR-0015 — Attestation Integration & Cryptographic Signing

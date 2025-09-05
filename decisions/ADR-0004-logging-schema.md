# ADR-0004 — Logging Schema & Locations

## Status
Proposed — 2025-09-05

## Context
AWO’s reproducibility depends on consistent logging. Dialogue Logs DL-001 through DL-005 have already demonstrated the need to distinguish between:
- **Dialogue logs** → external model/human input shaping decisions.  
- **Workflow logs** → factual timeline of what was done, when, and why.  
- **Audit logs** → independent validation, critiques, and rejection events.  

Without a clear schema and folder layout, logs risk becoming fragmented or inconsistent, undermining auditability.

## Decision
- The repository must maintain the following log structure:  
  - `/logs/dialogue/` → curated external feedback.  
  - `/logs/workflow/` → factual project steps and internal decisions.  
  - `/logs/audits/` → independent validation and rejection reports.  
- A rolling summary file (`DIALOGUE_LOG.md`, `WORKFLOW_LOG.md`) may exist at the root of each folder for convenience, but individual entries must be timestamped Markdown files.  
- **Minimum fields per log entry**:  
  - **Date**  
  - **Context**  
  - **Participants** (who/what models)  
  - **Artifacts touched**  
  - **Impact/Decision**  
  - **Status** (accepted, revised, rejected, pending)  
- ADRs must reference relevant Dialogue, Workflow, or Audit Log IDs.  
- Long raw transcripts may be stored in `/logs/dialogue/raw/`, but curated excerpts are mandatory in the main log.

## Consequences
- Guarantees that anyone auditing AWO can trace every decision to a log entry.  
- Maintains separation of influence (dialogue), action (workflow), and verification (audit).  
- Reduces ambiguity when linking ADRs to their origins.  
- Adds process discipline: contributors must use the schema and cannot bypass logs.

## References
- Dialogue Logs DL-001 to DL-005 (framing requirements, evidence, ad-hoc clarification, novelty, scientific value)  
- ADR-0001 — Flagship Positioning & Case-Study Policy  
- ADR-0003 — Audit Gates & Rejection Loop  

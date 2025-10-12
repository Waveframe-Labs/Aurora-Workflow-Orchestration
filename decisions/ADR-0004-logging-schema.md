# ADR-0004 — Logging Schema & Locations

## Status
Proposed — 2025-09

## Context
AWO’s reproducibility depends on consistent logging. We scaffold logging as:  
- **Workflow logs** → factual timeline of what was done, when, and why.  
- **Audit logs** → independent validation, critiques, and rejection events.  

Without a clear schema and folder layout, logs risk becoming fragmented or inconsistent, undermining auditability.

## Decision
- The repository must maintain the following log structure:    
  - `/logs/workflow/` → factual project steps and internal decisions.  
  - `/logs/audits/` → independent validation and rejection reports.  
- A rolling summary file (`WORKFLOW_LOG.md`) may exist at the root of each folder for convenience, but individual entries must be timestamped Markdown files.  
- **Minimum fields per log entry**:  
  - **Date**  
  - **Context**  
  - **Participants** (who/what models)  
  - **Artifacts touched**  
  - **Impact/Decision**  
  - **Status** (accepted, revised, rejected, pending)  
- ADRs must reference relevant Workflow or Audit Log IDs.  

## Consequences
- Guarantees that anyone auditing AWO can trace every decision to a log entry.  
- Maintains separation of action (workflow), and verification (audit).  
- Reduces ambiguity when linking ADRs to their origins.  
- Adds process discipline: contributors must use the schema and cannot bypass logs.

## References 
- ADR-0001 — Flagship Positioning & Case-Study Policy  
- ADR-0003 — Audit Gates & Rejection Loop  

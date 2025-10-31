---
filetype: workflow_logs
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Workflow Logs — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory records the factual, chronological history of workflow execution under the AWO method.  
Each log entry serves as immutable provenance evidence, documenting *what was done, when, and why*.  
Unlike `/workflows/` (which defines process logic), these logs capture the actual runtime outcomes and contextual reasoning behind each research action.

---

## Structure

| File / Folder | Description |
|----------------|-------------|
| **YYYY-MM-DD_run_event_<id>.md** | Event-level log capturing actions, triggers, and outcomes for a specific workflow run. |
| **index.json** | (Optional) Machine-readable index summarizing all recorded workflow events for CRI-CORE ingestion. |
| **summary_log.md** | Rolling summary of recent workflow activities (optional convenience record). |

---

## Logging Schema

Each workflow log entry **MUST** include the following metadata fields:

| Field | Requirement | Description |
|--------|--------------|-------------|
| **Date** | Required | UTC timestamp of event occurrence. |
| **Context** | Required | Short description of what was done or why the action occurred. |
| **Participants** | Required | Roles or agents (human or model) responsible for the action. |
| **Artifacts** | Required | Files, manifests, or outputs affected by the action. |
| **Impact / Decision** | Required | Resulting change, gate outcome, or observation. |
| **Status** | Required | One of: `Accepted`, `Revised`, `Rejected`, or `Pending`. |

---

## Policy

- Workflow logs are **mandatory** for all AWO-compliant runs.  
- Each run under `/runs/` MUST reference its associated workflow log by filename or ID.  
- These logs form the factual timeline underlying the evidence registry and compliance reports.  
- Entries are append-only; revisions require an ADR if content is retroactively modified.

---

## Integration

- Used in combination with `/logs/audits/` and `/logs/governance/` for end-to-end traceability.  
- Informs the AWO Evidence Registry and provides direct lineage for falsifiability manifests.  
- CRI-CORE validators will parse this folder for chronological event reconstruction.

---

## Contact  

Waveframe Labs  
swright@waveframelabs.org

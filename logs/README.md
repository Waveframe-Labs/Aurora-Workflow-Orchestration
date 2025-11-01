---
filetype: logs_index
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Logs — Aurora Workflow Orchestration (AWO)

## Purpose
The `/logs/` directory serves as the **central provenance ledger** for all activity, governance, and validation records in an AWO-compliant repository.  
Every subfolder captures a specific dimension of reproducibility — workflow traces, audits, governance actions, overrides, and attestation results.

Each log entry must:
- Be timestamped in ISO 8601 format.  
- Reference at least one Architecture Decision Record (ADR).  
- Include the originating role (Orchestrator, Auditor, Synthesizer, Critic, or CI Validator).  
- Be immutable once committed, except for appended status updates (tracked via ADR-0017).

---

## Directory Overview

| Subfolder | Description | Reference |
|------------|--------------|------------|
| `/logs/workflow/` | Chronological records of human and agent activity covering decisions, forks, merges, and context. | ADR-0004 |
| `/logs/audits/` | Independent audit results, rejection events, and compliance findings. | ADR-0003 |
| `/logs/audits/rejections/` | Reports for artifacts or runs that failed validation gates. | ADR-0003 |
| `/logs/audits/summaries/` | Aggregated audit summaries grouped by release cycle. | ADR-0003, ADR-0017 |
| `/logs/overrides/` | Manual interventions and rationale for non-automated overrides. | ADR-0004, ADR-0012 |
| `/logs/governance/` | Governance-level decisions, approvals, and oversight logs. | ADR-0017 |
| `/logs/governance/attestation_failures/` | Attestation or approval anomalies detected by validation workflows. | ADR-0003 |
| `/logs/governance/role_attestations/` | Signed declarations affirming participant roles and responsibilities. | ADR-0012, ADR-0017 |
| `/logs/governance/release_governance/` | Historical release governance entries aligned to CHANGELOG and version tags. | ADR-0017 |
| `/logs/governance/integrity_events/` | Machine or workflow-generated logs for integrity enforcement. | ADR-0015, ADR-0016 |

---

## Schema Requirements

Each log file (YAML or Markdown front matter) must include:
```yaml
log_id: LOG_YYYYMMDD_<unique_suffix>
run_id: RUN_YYYY-MM-DDTHH-MM-SSZ
actor_role: <Orchestrator | Auditor | Synthesizer | Critic | Validator>
action: <short description>
timestamp: <ISO 8601>
linked_adrs: [0004, 0017]
sha256: <optional hash for binary or external reference>
status: <OPEN | CLOSED | RESOLVED | REJECTED>
```

All logs **MUSTD:**  
- Include a clear causal link to a run, artifact, or governance event.  
- Be registered in the root-level SHA256SUMS.txt file.  
- Be readable in plain text (no binary formats).
- 

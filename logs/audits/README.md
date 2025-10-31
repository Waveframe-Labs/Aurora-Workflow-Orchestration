---
filetype: audit_logs
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Audit Logs — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory houses all independent audit records generated during AWO verification cycles.  
Each file documents review findings, rejection events, and compliance evaluations tied to specific runs, artifacts, or governance actions.  
Audit logs ensure transparent validation of every material claim and form part of AWO’s falsifiability backbone.

---

## Structure

| File / Folder | Description |
|----------------|-------------|
| **YYYY-MM-DD_audit_<run_id>.md** | Audit report for a specific run or process, including reviewer findings and verdicts. |
| **rejections/** | Contains rejection reports for artifacts or runs that failed validation gates. |
| **summaries/** | Aggregated audit summaries grouped by version or release cycle. |
| **index.json** | (Optional) Machine-readable audit index consumed by CRI-CORE for compliance scoring. |

---

## Logging Schema

Each audit entry **MUST** include the following metadata fields:

| Field | Requirement | Description |
|--------|--------------|-------------|
| **Date** | Required | UTC timestamp of audit review. |
| **Actor (Role)** | Required | Role of the reviewing entity (Auditor, Peer Reviewer, Red Team). |
| **Scope** | Required | The subsystem or process audited (e.g., Attestation, Governance, Run Integrity). |
| **Findings** | Required | Detailed observations, including supporting evidence. |
| **Artifacts** | Required | Files or reports under review. |
| **Linked ADRs** | Optional | Policy or procedural ADRs relevant to the audit. |
| **Verdict** | Required | One of: `Approved`, `Conditionally Approved`, `Rejected`, or `Deferred`. |
| **Follow-up Actions** | Optional | Steps required for correction or further verification. |

---

## Policy

- Audit logs are **immutable** once finalized and approved.  
- Every release or attestation event MUST be traceable to at least one corresponding audit log.  
- Rejected or deferred audits trigger entries in `/logs/governance/` and `/logs/attestation_failures/`.  
- Audits may be human-authored, AI-generated, or hybrid, but all entries require role and time provenance.

---

## Integration

- Used by CRI-CORE to calculate repository trust metrics and audit chain completeness.  
- Cross-linked in Compliance Reports and Governance Summaries.  
- Serves as the normative record for external reproducibility verification.

---

## Contact  

Waveframe Labs  
swright@waveframelabs.org

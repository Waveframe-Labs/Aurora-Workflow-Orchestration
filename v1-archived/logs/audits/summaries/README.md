# /logs/audits/summaries/

## Purpose
Stores **aggregated audit summaries**, grouped by release cycle or version tag.  
Each file consolidates audit verdicts, rejection statistics, and corrective actions.

## Example Summary Entry
```yaml
summary_id: SUM_2025-10_v1.2.1
version_tag: v1.2.1
total_audits: 3
passed: 3
failed: 0
rejections_logged: 0
timestamp: 2025-10-31T23:55Z
linked_adrs: [0003, 0015, 0017]
notes: "All audits passed. Repository structure verified against Method Spec §4.3."
```
---

**Governance Reference:** ADR-0017  
**Responsible Role:** Auditor  

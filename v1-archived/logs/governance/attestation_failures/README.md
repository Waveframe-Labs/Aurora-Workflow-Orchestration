# /logs/governance/attestation_failures/

## Purpose
Records **attestation or approval anomalies** detected by validation workflows (manual or automated).  
This includes failed digital signature checks, missing hashes, or mismatched approval data.

## Log Entry Format
```yaml
failure_id: FAIL_2025-10-31_001
run_id: RUN_2025-10-31T00-00-42Z
detected_by: CRI-Validator
reason: "approval.json missing neurotransparency evidence pointer"
severity: HIGH
timestamp: 2025-10-31T23:05Z
resolution_status: Open
linked_adrs: [0003, 0012, 0015]
```
---

**Reference:** ADR-0003, ADR-0015  
**Governance Role:** Auditor  

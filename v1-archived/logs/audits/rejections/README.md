# /logs/audits/rejections/

## Purpose
Contains **rejection reports** for artifacts or runs that failed validation gates.  
These may arise from checksum mismatches, missing falsifiability manifests, or role-separation violations.

## Example Rejection Entry  

```yaml
rejection_id: REJ_2025-10-31_001
run_id: RUN_2025-10-31T00-00-42Z
reason: "Missing neurotransparency_evidence field in approval.json"
severity: HIGH
detected_by: Auditor
timestamp: 2025-10-31T22:05Z
linked_adrs: [0003, 0012, 0015]
resolution_status: "Pending Review"  
```  
---

**Governance Reference:** ADR-0003  
**Responsible Role:** Auditor  

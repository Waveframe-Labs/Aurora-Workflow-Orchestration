# /logs/governance/integrity_events/

## Purpose
Captures **machine or workflow-generated integrity events**, such as checksum validation, schema verification, or build attestation.

## Log Entry Format
```yaml
event_id: INT_2025-10-31_001
workflow: "root-sha256sums.yml"
status: "PASS"
artifact_scope: "docs/AWO_Method_Spec_v1.2.1.pdf"
sha256: "b39e4...a81c"
timestamp: 2025-10-31T19:01Z
linked_adrs: [0015, 0016]
```
---

**Reference:** ADR-0015, ADR-0016  
**Governance Role:** CI Validator  

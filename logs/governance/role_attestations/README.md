# /logs/governance/role_attestations/

## Purpose
Contains **signed declarations** by human or synthetic participants affirming their roles and responsibilities under AWO.  
Each entry corresponds to a formal attestation (e.g., Orchestrator, Auditor, Critic, Synthesizer).

## Log Entry Format
```yaml
attestation_id: ATT_2025-10-31_001
participant: "Shawn C. Wright"
role: "Orchestrator"
run_scope: RUN_2025-10-31T00-00-42Z
signed: true
signature_hash: "fa9b3...21ce"
timestamp: 2025-10-31T17:48Z
linked_adrs: [0012, 0017]
```
---

**Reference:** ADR-0012, ADR-0017  
**Governance Role:** Orchestrator  

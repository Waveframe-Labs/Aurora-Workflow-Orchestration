# /logs/overrides/

## Purpose
This directory records **manual interventions**, overrides, and rationale for non-automated actions within an AWO workflow.

Each entry must include:
- A timestamp and the acting role
- A description of the intervention or deviation
- References to affected run IDs and ADRs
- Digital signatures where applicable

## Compliance Reference
- **ADR-0004:** Workflow Logging  
- **ADR-0012:** Role Attestation and Override Policy  

---

### Example Entry

```yaml
override_id: OVR_2025-10-31_001
run_id: RUN_2025-10-31T00-00-42Z
actor_role: Orchestrator
reason: "Manual approval of delayed artifact verification step due to CI downtime."
linked_adrs: [0004, 0012]
timestamp: 2025-10-31T18:42Z
signature: "SHA256:ecc1b6b8f..."
status: Approved
```
---

## Governance Note:
All overrides must be reviewed and counter-signed by an independent Auditor during the next attestation cycle. Persistent or repeated overrides trigger a governance review per ADR-0017.  

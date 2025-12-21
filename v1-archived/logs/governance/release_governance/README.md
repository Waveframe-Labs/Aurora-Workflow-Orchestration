# /logs/governance/release_governance/

## Purpose
Tracks **historical release governance entries** aligned to CHANGELOG updates and version tags.  
Used to cross-verify compliance and artifact integrity at release time.

## Log Entry Format
```yaml
release_id: REL_2025-10-31_v1.2.1
tag: v1.2.1
governance_action: "Release Approved"
reviewed_by: "Auditor"
timestamp: 2025-10-31T18:12Z
sha256_verified: true
linked_adrs: [0015, 0017]
notes: "Checksums validated; all compliance reports included."
```
---

**Reference:** ADR-0017  
**Governance Role:** Maintainer  

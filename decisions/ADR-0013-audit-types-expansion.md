# ADR-0013: Audit Types Expansion

- Date: 2025-10-02
- Status: Accepted
- Context: Current audit record template supports three audit types: Logic, Data, Peer Review. Some projects may require expanded categories (e.g., Security, Compliance, Performance).
- Decision: Audit types are formally extensible. Projects may add categories to `audit-record.md` under the **Audit Type** section, provided:
  - The type is defined in the record’s context.
  - Linked evidence is included in `/logs/audits/`.
- Consequences: Improves adaptability for specialized domains (e.g., regulated industries). Risk: too many categories could reduce clarity. Mitigated by requiring justification in each record.
- Related Artifacts: `/templates/audit-record.md`, `/logs/audits/`, ADR-0002 (Evidence Registry).

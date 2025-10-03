# ADR-0012: Human-in-the-Loop Signoff

- Date: 2025-10-02
- Status: Accepted
- Context: AWO emphasizes auditable AI workflows, but governance requires a human arbiter to accept/reject outputs before release. This ensures accountability beyond automated checks.
- Decision: Every AWO run must include explicit **human approval** before release or public tagging. This is recorded as:
  - A signed checklist (`audit-checklist.md`) confirming compliance.
  - An entry in `/logs/decisions/` referencing the approving person.
- Consequences: Establishes human accountability, mitigates risk of blind reliance on AI outputs. May slow release cadence but ensures trustworthiness.
- Related Artifacts: `/templates/audit-checklist.md`, `/logs/decisions/`, ADR-0003 (Audit Gates), ADR-0010 (Release Governance).

# ADR-0011: Template Usage Policy

- Date: 2025-10-02
- Status: Accepted
- Context: The AWO repository provides multiple templates (audit checklist, audit record, falsifiability manifest, worklog, ADRs). Without a governing policy, these may be applied inconsistently, weakening reproducibility.
- Decision: All official AWO projects **must** use the provided templates for their designated purpose. At minimum:
  - `templates/audit-checklist.md` used for every audit gate.
  - `templates/audit-record.md` created for each claim under review.
  - `templates/falsifiability-manifest.md` maintained with current status for every claim ID.
  - `templates/worklog-entry.md` updated with each significant orchestration step.
  - `templates/adr.md` used for every new architectural decision.
- Consequences: Ensures uniformity and reduces governance drift across projects. Adds overhead but enforces comparability across repos.
- Related Artifacts: `/templates/*`, ADR-0003 (Audit Gates), ADR-0009 (Case Studies).

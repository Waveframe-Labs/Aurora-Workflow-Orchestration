---
filetype: templates
version: 1.1.1
updated: 2025-10
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---
# Templates — Reusable Governance Artifacts

**Purpose**  
Markdown/YAML templates used to drive repeatability and audits.

**Common templates**
- `ADR-*.md` — decision records (context, decision, consequences, links).
- `audit-checklist.md` — human gate for merge/release.
- `audit-record.md` — structured audit (logic/data/peer).
- `falsifiability-manifest.md` — claim IDs, tests, datasets, thresholds, status.
- `release-checklist.md` — pre-release governance tasks.
- `worklog.md` — daily log of actions, lessons, next steps.

**Guidelines**
- Keep domain-agnostic; parametrize datasets/metrics.
- Link templates to schema-validated artifacts in `runs/<id>/`.

**Contact**  
Waveframe Labs — swright@waveframelabs.org

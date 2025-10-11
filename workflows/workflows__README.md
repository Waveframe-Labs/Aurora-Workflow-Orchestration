---
filetype: automation
version: 1.0.1
updated: 2025-10
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---
# Workflows — GitHub Actions

**Purpose**  
Automation for AWO runs — validate scope, fan-out/consensus, record audits, and gate human approval before commit.

**Contents**
- `awo-run.yml` — end-to-end pipeline used in this repo.

**How to run**
1. **Actions → AWO Run (Manual Approve to Commit)**  
2. **Run workflow** (manual dispatch)  
3. Review the **job summary** and artifacts; complete the audit checklist.  
4. Approve the **audit gate** when satisfied. The run halts until human approval.

**What it does**
- Captures **provenance** (environment, git SHA, run ID/timestamp).
- Performs **scope validation** against the method spec.
- **Fan-outs** model variants → **consensus vote** → emits a consensus record.
- Writes artifacts: `run_manifest.json`, `provenance.json`, `scope/*.json`,
  `notes/consensus.json`, `SHA256SUMS.txt`, and a summarized `report.md`.
- Enforces **deployment protection rules** (e.g., `awo-audit`, `awo-scope`).
- Exits with **78** to pause the run until human approval and finalization.

**Outputs**
- GitHub **job summary** (readable audit trail).
- Zipped **artifacts** per run (evidence package).
- Final **run folder** under `/runs/` once approved.

**Policy**
- Do **not** edit this workflow on `main`; use a PR so the audit trail is preserved.
- Artifacts are **immutable** once referenced by a Decision Record (ADR).

**Contact**  
Waveframe Labs — swright@waveframelabs.org

# GitHub Workflows

**Purpose:**  
Automation for AWO runs — validates scope, performs fan-out and consensus steps, records audits, and gates human approval before final commit.

**Contents**  
- `awo-run.yml` — the end-to-end AWO pipeline defining validation, audit gating, and archival.

**How to Run**  
1. Navigate to **Actions → AWO Run (Manual Approve to Commit)**.  
2. Click **Run workflow** to start a manual dispatch.  
3. Review the generated job summary and artifacts; complete the audit checklist.  
4. Approve the audit gate once all validations pass.  
   The run pauses until human approval is recorded, then finalization executes automatically.

**High-Level Process**  
- Captures provenance (environment, git SHA, run ID, timestamps).  
- Performs scope validation against the method specification.  
- Executes fan-out of model variants → consensus vote → emits consensus record.  
- Writes artifacts:  
  `run_manifest.json`, `provenance.json`, `scope/*.json`,  
  `notes/consensus.json`, `SHA256SUMS.txt`, and summarized `report.md`.  
- Enforces deployment protection rules (`awo-audit`, `awo-scope`).  
- Intentionally exits with code `78` to pause until human approval is complete.

**Outputs**  
- GitHub job summary — a readable audit trail.  
- Zipped artifacts per run — immutable evidence package.  
- Finalized run folder under `/runs/` after approval.

**Policy**  
- Do not modify this workflow directly on `main`; use a pull request to preserve the audit trail.  
- Artifacts are immutable once referenced by an Architectural Decision Record (ADR).

**Contact**  
Waveframe Labs — `swright@waveframelabs.org`  
(Website coming soon)

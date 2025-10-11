---
filetype: run_records
version: 1.1.0
updated: 2025-10-08
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Runs — Aurora Workflow Orchestration (AWO)

**Purpose**  
This directory contains all **executed AWO workflow runs**, each recorded as a timestamped evidence package.  
Every run captures the full workflow state, outputs, and audit status to ensure end-to-end reproducibility.

---

## Structure

```
runs/
 ├── run_YYYY-MM-DDTHH-MM-SSZ/   # unique run ID (UTC timestamp)
 │    ├── input.json             # workflow definition used
 │    ├── outputs/               # model responses, comparisons, metrics
 │    ├── audit/                 # audit logs and status (pending/approved/rejected)
 │    ├── metadata.json          # seeds, model identifiers, hashes
 │    └── report.md              # summary report generated for this run
 └── ...
```

---

## Audit Flow

- Each run may include an **audit gate** step, which pauses execution until a human approves or rejects the results.  
- Pending gates are stored in `gate_pending.json` with checklist information.  
- Approval finalizes the run and archives it as immutable evidence.

---

## Provenance & Reproducibility

- Each run folder forms a **complete provenance chain** — inputs, configuration, results, and audit outcome.  
- The folder contents are immutable once committed and may be exported or packaged for archival.  
- AWO’s automation layer records all hashes, timestamps, and metadata to allow independent reproduction.

---

## Artifacts & Archival

- GitHub Actions automatically packages each run as a `.tar.gz` artifact.  
- These artifacts serve as **portable reproducibility bundles** that can be validated externally or cited in releases.

---

## Policy

- Do **not** modify run directories manually — all edits must occur through the orchestration workflow.  
- Each run is tied to a corresponding commit SHA and audit record for traceability.  
- Run reports (`report.md`) and manifests are linked during Zenodo archival.

---

## Contact  
Waveframe Labs  
swright@waveframelabs.org

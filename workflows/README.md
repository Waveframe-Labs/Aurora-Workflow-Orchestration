---
filetype: automation
version: 1.1.1
updated: 2025-10
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Workflows — Automation & Orchestration Examples

**Purpose**  
This directory contains both:
1. **Automation workflows** — GitHub Actions that validate, gate, and attest AWO runs.  
2. **Orchestration definitions** — JSON examples demonstrating AWO’s schema for structured, reproducible AI–human tasks.

Together, these files form the execution layer of the Aurora Workflow Orchestration (AWO) framework.

---

## GitHub Actions Automation

**File:** `.github/workflows/awo-run.yml`  
Defines the automated validation pipeline for AWO.  

**Capabilities**
- Captures **provenance** (environment, git SHA, timestamp).  
- Validates scope and audit readiness.  
- Executes **multi-model fan-out → consensus synthesis**.  
- Generates artifacts:  
  - `run_manifest.json`  
  - `provenance.json`  
  - `notes/consensus.json`  
  - `SHA256SUMS.txt`  
  - `report.md`  
- Emits verifiable **attestation artifacts** (`ATTESTATION.txt`, `.sig`, `.cert`).  
- Enforces deployment protection rules (`awo-audit`, `awo-scope`).

**Run Instructions**
1. Go to **Actions → AWO Run (Manual Approve to Commit)**.  
2. Click **Run workflow** (manual dispatch).  
3. Review the **job summary** and generated artifacts.  
4. Approve the **audit gate** to finalize the run.  

*Note: The workflow halts until manual human approval (exit code 78).*

---

## Orchestration Examples

These JSON files illustrate how AWO defines and executes modular workflows.  
They are **educational examples**, not production runs.

| File | Description |
|------|--------------|
| `multimodel.json` | Demonstrates multi-model orchestration for consensus generation. |
| `reviews.json` | Simple example showing stepwise orchestration — ingest, extract themes, summarize — for testing schema validation. |

Each file follows the **AWO Workflow Schema** (`/schemas/workflow_schema.json`) and can be executed or validated through the AWO runner.

Example structure:
```json
{
  "name": "Customer Review Analysis (demo)",
  "steps": [
    { "name": "ingest", "prompt": "Load five sample customer reviews about a coffee grinder." },
    { "name": "extract_themes", "prompt": "Identify the top 3 themes and one representative quote per theme." },
    { "name": "summarize", "prompt": "Write a 2-sentence summary that could go in an internal memo." }
  ]
}
```

---

## Outputs

Each run produces:
	•	A human-readable audit trail (GitHub job summary).
	•	Zipped evidence artifacts (verifiable provenance package).
	•	A finalized run folder under /runs/ once approved.

---

## Policy
	•	Do not modify workflow YAMLs directly on main.
Submit changes via pull request to preserve the audit trail.
	•	Once a run’s artifacts are cited in an ADR, they become immutable.
	•	Example JSONs (reviews.json, multimodel.json) are maintained as reproducibility demos.

---

Maintainer: Waveframe Labs
📧 swright@waveframelabs.org
🔗 waveframelabs.org

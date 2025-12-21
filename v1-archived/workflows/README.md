---
filetype: orchestration
version: 1.1.1
updated: 2025-10-13
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Workflows — Orchestration Definitions & Demos

**Purpose**  
This directory contains JSON-based **orchestration definitions** used to demonstrate how Aurora Workflow Orchestration (AWO) structures reproducible AI–human tasks.

These files are **schema-validated examples** used for testing, documentation, and educational replication of the AWO workflow model.

---

## Contents

| File | Purpose |
|------|----------|
| `multimodel.json` | Demonstrates multi-model orchestration and consensus synthesis. |
| `reviews.json` | Minimal end-to-end example — ingest, extract themes, summarize — for schema validation and onboarding tests. |

All orchestration files conform to the **AWO Workflow Schema** (`/schemas/workflow_schema.json`).  
They can be validated independently or executed through the AWO runner.

---

## Validation

Use the included schema to ensure compliance:

```bash
pip install jsonschema
jsonschema -i workflows/reviews.json schemas/workflow_schema.json
jsonschema -i workflows/multimodel.json schemas/workflow_schema.json
```

Each file must include:
- A descriptive `"name"` field  
- An ordered `"steps"` array  
- Each step containing at least `"name"` and `"prompt"`  

---

## Example Structure

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

## Relation to AWO Runner

The runner file itself lives in `.github/workflows/awo-run.yml`  
These JSON definitions are **inputs or test fixtures** used to illustrate AWO’s orchestration syntax, not automation pipelines.

---

## Policy

- Keep demo workflows minimal and schema-compliant.  
- Do **not** modify JSONs on `main`; update via pull request.  
- Once referenced in an ADR or audit, workflow examples are **immutable**.  

---

**Maintainer:** Waveframe Labs  
📧 swright@waveframelabs.org  
🔗 [waveframelabs.org](https://waveframelabs.org)

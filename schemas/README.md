---
filetype: schema_suite
version: 1.0.1
updated: 2025-10
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---
# Schemas — Validation Contracts

**Purpose**  
JSON Schemas that enforce structure and traceability for AWO runs.

**Key files (typical):**
- `run_manifest.schema.json` — lifecycle state, timestamps, steps list.
- `provenance.schema.json` — model/tool records, artifacts, hashes.
- `claim.schema.json` — falsifiable claims with tests and evidence.
- `environment.schema.json` (optional) — runtime/environment snapshot format.

**Usage**
- Scripts validate run artifacts against these schemas during the pipeline.
- Schemas are versioned; breaking changes should increment schema versions and be captured in ADRs.

**Conventions**
- Draft: JSON Schema 2020-12.
- Prefer explicit `required` fields and `additionalProperties: false`.
- Document examples for quick adoption.

**Contact**  
Waveframe Labs — swright@waveframelabs.org

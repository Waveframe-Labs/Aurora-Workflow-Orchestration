---
filetype: doctrine
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Neurotransparency Doctrine — Aurora Workflow Orchestration (AWO)

**Definition**  
Neurotransparency requires that every claim-affecting inference is attributable to a declared role and recorded in a durable artifact, enabling deterministic reconstruction of the reasoning path.

## Scope
- Applies to all AWO phases (§5): fan-out, consensus, attestation, archival.
- Governs both manual and automated (CRI-CORE) implementations.

## Minimum Evidence (per attested claim)
- **Origin role:** Orchestrator/Evaluator/Auditor/Synthesizer (see §3).
- **Evidence pointer:** path(s) to logs, ADRs, manifests, or reports.
- **Hash continuity:** artifact hashes present in root `SHA256SUMS.txt`.
- **Attestation link:** `approval.json` referencing the above.

## Recording Patterns
- Manual: short “Reasoning Excerpt” in `/logs/workflow/` with file links + hashes.
- Automated: CRI-CORE capture of prompts, configs, model IDs, seeds, and output hashes.

## Non-Conformance
- Missing origin, missing evidence pointer, or missing hash → attestation **FAIL** (§9).

## Future Integration
<!-- CRI-CORE:placeholder:neurotransparency.schema -->

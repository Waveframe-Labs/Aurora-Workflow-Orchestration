---
filetype: architecture_decision_record
version: 1.1.1
updated: 2025-10-12
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# ADR-0015 — Attestation Integration & Cryptographic Signing

## Context
Previous AWO versions (≤ v1.1.0) achieved procedural reproducibility through manifests, audit gates, and deterministic runs.  
However, while these mechanisms ensured methodical consistency, they did **not** guarantee *cryptographic verifiability*.  
There was no proof that a published manifest and its output artifacts were generated together by a trusted execution context.

## Decision
Beginning with **v1.1.1**, AWO introduces a formal **attestation layer** to cryptographically bind every run’s manifest and checksum set.  
This feature leverages **Sigstore’s `cosign`** for *keyless OIDC signing* within GitHub Actions.

### Implementation Summary
- Added new attestation and signing stages in `.github/workflows/awo-run.yml`.  
- Each approved run now emits:
  - `ATTESTATION.txt` — binds `run_manifest.json` ↔ `SHA256SUMS.txt`.  
  - `.sig` and `.cert` — OIDC-signed proof files for both attestation and full run archive.  
- Attestation content includes run ID, repository, commit SHA, actor, timestamp, and SHA-256 bindings.

### Workflow Impact
- All runs are now **tamper-evident** and **cryptographically verifiable**.  
- Manual `/audit/` folders are deprecated; attestation replaces human checksum validation.  
- The attestation chain becomes part of the archival evidence package uploaded to Zenodo or other registries.

## Consequences
- Strengthens reproducibility with verifiable provenance and file integrity.  
- Enables third-party validation using `cosign verify-blob` or manual SHA-256 checks.  
- Establishes a compliance baseline for future CRI-CORE automation.  
- All future releases must include a valid attestation step prior to tagging or DOI archival.

## Status
Accepted and implemented in **AWO v1.1.1 (Attested Release)** — run `run_2025-10-12T14-29-03Z`.

## References
- `.github/workflows/awo-run.yml` — updated workflow with attestation and signing logic.  
- `runs/<RUN_ID>/ATTESTATION.txt` — sample generated record.  
- [Sigstore Cosign Docs](https://docs.sigstore.dev/cosign/overview/)

---

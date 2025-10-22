---
filetype: handoff_record
version: 1.2.0
updated: 2025-10-22
maintainer: Waveframe Labs
program: Aurora Research Initiative
contact: swright@waveframelabs.org
---

# CRI Handoff Record

**Project:** Aurora Workflow Orchestration (AWO)  
**Status:** Finalized methodology (v1.2.0) under Waveframe Labs governance  
**Successor:** CRI-CORE — Continuous Research Integration Toolchain

---

## Purpose

This record formalizes the **handoff of runtime implementation scope** from **AWO** (methodology) to **CRI-CORE** (runtime).  
AWO remains the **canonical methodological reference**; CRI-CORE operationalizes the method as executable, verifiable infrastructure.

> **AWO defines the rules. CRI enforces them.**

---

## Scope of Transfer

The following areas move from AWO (specification) to CRI-CORE (implementation):

- **Runtime provenance and attestation** — automated capture of manifests, checksums, and signatures.  
- **Validation & gates** — schema validation for runs, falsifiability checks, and audit gates.  
- **Execution workflows** — reproducible runners that emit immutable `runs/<id>` artifacts.  
- **Integration surfaces** — hooks for CI, evidence capture, and verification commands.

AWO **does not** add new runtime features going forward. It remains stable as a citation-grade method.

---

## Artifact Lineage (AWO → CRI-CORE)

| AWO Artifact / Concept                         | CRI-CORE Responsibility                                   |
|------------------------------------------------|------------------------------------------------------------|
| Method Spec v1.2 (governance rules)            | Enforced via schemas, validators, and CLI runtime         |
| Falsifiability manifest (claims, tests)        | Schema + CLI checks; fail-closed gating                    |
| Run manifest (`/runs/.../run_manifest.json`)   | Generated, validated, and sealed per run                   |
| Attestation (`ATTESTATION.txt`, signatures)    | Emitted + verifiable (hashes, OIDC signing where available)|
| Checksums (`SHA256SUMS.txt`)                    | Generated and verified against produced artifacts          |
| Audit workflow (draft → audit → synthesis)     | Encoded as gates / checklists → enforced in runtime        |

---

## Version Boundary

- **AWO v1.2.0** is the **final** methodology line.  
- No functional changes will occur in AWO beyond **provenance or reference updates**.  
- All future implementation work proceeds in **CRI-CORE**.

---

## Provenance & DOI

While Zenodo account consolidation is pending, **all AWO references SHALL use the concept DOI**:

**Canonical Concept DOI:** https://doi.org/10.5281/zenodo.17013612

> Note: Provisional version DOIs exist due to an account linkage issue. The concept DOI above is authoritative until Zenodo confirms consolidation.

---

## Verification (External Replicators)

1. Reference **AWO v1.2.0** for the methodological rules and artifacts.  
2. Use **CRI-CORE** to execute workflows and produce immutable `runs/<id>` folders.  
3. Verify:
   - `run_manifest.json` schema validity  
   - `SHA256SUMS.txt` against all emitted artifacts  
   - Attestation/signature files where present

---

## Links

- **AWO (methodology):** https://github.com/Waveframe-Labs/Aurora-Workflow-Orchestration  
- **CRI-CORE (runtime):** https://github.com/Waveframe-Labs/CRI-CORE  
- **Concept DOI (AWO):** https://doi.org/10.5281/zenodo.17013612

---

## Maintainer

**Waveframe Labs — Aurora Research Initiative**  
Contact: swright@waveframelabs.org


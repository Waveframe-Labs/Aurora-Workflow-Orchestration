# Aurora Workflow Orchestration (AWO)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17345552.svg)](https://doi.org/10.5281/zenodo.17345552)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0.md)  
[![Cite this repo](https://img.shields.io/badge/Cite-CITATION.cff-important.svg)](CITATION.cff)  
![Last Commit](https://img.shields.io/github/last-commit/Waveframe-Labs/Aurora-Workflow-Orchestration/main)

![AURORA WORKFLOW ORCHESTRATION](figures/awo_banner_cri.PNG)

---

## Core Documents

- Whitepaper: [`/docs/AWO_Whitepaper_v1.0.md`](docs/AWO_Whitepaper_v1.0.md)  
- Method Specification: [`/docs/AWO_Method_Spec_v1.1.md`](docs/AWO_Method_Spec_v1.1.md)  
- Concept DOI (resolves to latest version): [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)

---

## Run AWO (GitHub Actions)

1. Go to **Actions → AWO Run (Manual Approve to Commit)**.  
2. Click **Run workflow** and select a workflow file (default: `workflows/multimodel.json`).  
3. Approve the **Scope** and **Audit** gates when prompted.  
4. After completion, the run is committed under `runs/<RUN_ID>/` with:
   - `run_manifest.json`, `report.md`, `SHA256SUMS.txt`  
   - `ATTESTATION.txt` and `.sig` / `.cert` for the attested run

---

## Overview

Aurora Workflow Orchestration (AWO) transforms AI-assisted projects into auditable, reproducible research pipelines.  
Each run produces a cryptographically signed provenance record, binding logic, data, and human oversight into one verifiable unit.

AWO is a methodology, not a code library. Every tagged release is citable (via DOI) and inspectable through structured logs, manifests, and schema validation.

> AWO integrates with **CRI-CORE**, a complementary execution layer that automates validation, attestation, and archival for every workflow run.

---

## Why It Exists

AI accelerates discovery, but verification lags. AWO closes that gap through four principles:

1. Falsifiability first — every claim must be disprovable, not just plausible.  
2. Human-in-the-loop rigor — AI outputs are treated as hypotheses, not truths.  
3. Immutable provenance — all runs are signed, hashed, and traceable.  
4. Transparent governance — reproducibility replaces trust.

---

## Repository Structure

- Whitepaper / Method Spec → see [`/docs`](docs)  
- Templates → falsifiability manifests, audit checklists  
- Logs → timestamped workflow and decision records  
- Workflows → executable orchestration examples  
- Citations → metadata and licensing files
- Decicions → ADRs 0001-0015 
  
- Docs Index → [`/docs/README_TOC.md`](docs/README_TOC.md)

> If it can’t be audited, it doesn’t count.

---

## Current Release — v1.1.1 (2025-10-13)

Overview: finalizes AWO under Waveframe Labs governance with cryptographic attestation, repository hardening, and DOI traceability.

Key updates:
- Attestation integration (cosign + OIDC)  
- Repository hardening and maintainer transfer  
- End-to-end provenance sealing  
- `.zenodo.json` and `CITATION.cff` aligned with concept DOI

Version DOI for this release: **10.5281/zenodo.17345552**  
Concept DOI (always latest): **10.5281/zenodo.17013612**

Related ADRs:
- ADR-0014 — Repository Hardening & Organizational Transfer  
- ADR-0015 — Attestation Integration & Cryptographic Signing

---

## Roadmap

- Integrate CRI-CORE for continuous reproducibility  
- Expand into public reproducibility experiments  
- Formalize the “minimum viable paper” standard

---

## Maintainer

**Shawn C. Wright** — independent researcher developing reproducible AI–human workflows  
- ORCID: [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  
- Email: swright@waveframelabs.org  
- GitHub: [Waveframe-Labs](https://github.com/Waveframe-Labs)

---

## License

- Code: [Apache 2.0](LICENSE)  
- Documentation: [CC BY 4.0](LICENSE-CC-BY-4.0.md)

---

*This repository represents the signed, verifiable state of AWO v1.1.1. The concept DOI above always resolves to the latest version.*

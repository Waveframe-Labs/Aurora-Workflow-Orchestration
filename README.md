# Aurora Workflow Orchestration (AWO)

[![DOI](https://zenodo.org/badge/1041786630.svg)](https://doi.org/10.5281/zenodo.17013612)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0.md)  
[![Cite this repo](https://img.shields.io/badge/Cite-CITATION.cff-important.svg)](CITATION.cff)  
![Last Commit](https://img.shields.io/github/last-commit/Wright-Shawn/Aurora-Workflow-Orchestration/main)

![AURORA WORKFLOW ORCHESTRATION](figures/awo_banner_cri.PNG)

---

## Overview

**Aurora Workflow Orchestration (AWO)** transforms AI-assisted projects into **auditable, reproducible research pipelines**.  
Each run produces a **cryptographically signed provenance record** — binding code, logic, and decisions under verifiable governance.

AWO isn’t a code library; it’s a **methodology** for turning discovery itself into an artifact.  
Every tagged release is citable (via DOI) and fully inspectable through structured logs, manifests, and schema validation.

> AWO now integrates with **CRI-CORE**, the “CI/CD for research” layer — automating validation, attestation, and archival for each workflow run.

---

## Why It Exists

AI has changed how knowledge is produced — but verification hasn’t caught up.  
AWO closes that gap through four principles:

1. **Falsifiability first** — all claims must be disprovable, not just plausible.  
2. **Human-in-the-loop rigor** — AI outputs are treated as hypotheses, not facts.  
3. **Immutable provenance** — every run is signed, hashed, and logged.  
4. **Transparent governance** — reproducibility replaces trust.

---

## In This Repository

- **Whitepaper** → full method spec in [`/docs`](docs)  
- **Documentation Index** → see [`/docs/README_TOC.md`](docs/README_TOC.md) for a structured, citable table of contents  
- **Templates** → falsifiability manifests, ADRs, audit checklists  
- **Logs** → timestamped workflow and decision records  
- **Workflows** → executable orchestration examples  
- **Citations** → DOI, metadata, and licensing files  

> If it can’t be audited, it doesn’t count.  
> AWO prioritizes traceable rigor over presentation polish.  

---

## Current Release — v1.1.1 (2025-10-13)

- Repository hardening & organizational transfer to **Waveframe Labs**  
- Cryptographic **attestation integration** (cosign + OIDC)  
- Verified end-to-end reproducibility and provenance sealing  
- Updated `CITATION.cff` and `.zenodo.json` with correct concept DOI  

**Related ADRs:**  
- ADR-0014 — Repository Hardening & Organizational Transfer  
- ADR-0015 — Attestation Integration & Cryptographic Signing  

---

## Roadmap
  
- CRI-CORE integration for automated reproducibility  
- Expansion into public reproducibility experiments  

---

## Maintainer

**Shawn C. Wright**  
Researcher and developer of reproducible AI–human workflows  
- ORCID: [0009-0006-6043-9295](https://orcid.org/0009-0006-6043-9295)  
- Email: swright@waveframelabs.org  
- GitHub: [Waveframe-Labs](https://github.com/Waveframe-Labs)

---

## License

- **Code:** [Apache 2.0](LICENSE)  
- **Documentation:** [CC BY 4.0](LICENSE-CC-BY-4.0.md)

---

*This repository represents the verifiable, signed state of AWO v1.1.1 — archived under DOI 10.5281/zenodo.17013612.*

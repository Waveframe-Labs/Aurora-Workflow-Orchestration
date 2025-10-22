# Changelog

## v1.2.0 — CRI Handoff & Repository Finalization (2025-10-22)

### Summary
This release finalizes **Aurora Workflow Orchestration (AWO)** as the *methodological layer* within the Waveframe Labs ecosystem.  
AWO v1.2.0 formally designates **CRI-CORE** as its successor project and concludes AWO’s functional development line.  
All future runtime and verification tooling will continue under CRI-CORE, which operationalizes AWO’s reproducibility model in executable form.

### Key Updates
- Updated `README.md` to reflect AWO’s finalized status under Waveframe Labs governance.  
- Added clear explanation of AWO’s role as the **methodological framework** defining reproducible, audit-first AI–human collaboration.  
- Added **Successor Project** section linking to [CRI-CORE](https://github.com/Waveframe-Labs/CRI-CORE).  
- Clarified versioning boundary between AWO (methodology) and CRI (runtime implementation).  
- Introduced `docs/CRI_HANDOFF.md` to record formal transfer of runtime scope from AWO → CRI-CORE.  
- Updated DOI section to reference the **concept DOI (10.5281/zenodo.17013612)** while Zenodo account consolidation is pending.  
- Declared AWO a stable, citation-grade artifact—no further feature changes beyond provenance updates.

### Why It Matters
This marks the **completion of AWO’s lifecycle** as a standalone research framework.  
The repository now serves as the *canonical methodological reference* for reproducible AI–human collaboration.  
Its principles—falsifiability, attestation, and provenance—remain active through CRI-CORE, ensuring continuity between theory and runtime verification.  

---

**Status:** Finalized under Waveframe Labs · Aurora Research Initiative  
**Successor:** [CRI-CORE](https://github.com/Waveframe-Labs/CRI-CORE) — Continuous Research Integration Toolchain  
**Canonical DOI:** [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612)


## v1.2.0 — Automated Documentation Builds & Finalization within the Aurora Research Initiative (2025-10-20)  

### Summary
- This release finalizes AWO’s documentation framework within the **Aurora Research Initiative**, the flagship program published by **Waveframe Labs**, and integrates fully automated build pipelines for Whitepaper and Method Specification files.  

### Key Updates
- Added GitHub Actions workflows for **automated Pandoc → XeLaTeX PDF generation**:
  - `build-whitepaper-pdf.yml`
  - `build-methodspec-pdf.yml`
- Confirmed successful generation of:
  - `/docs/AWO_Whitepaper_v1.1.pdf`
  - `/docs/AWO_Method_Spec_v1.2.pdf`
- Established end-to-end reproducibility for documentation artifacts (no manual export required).
- Verified bot-based commits (`github-actions[bot]`) as traceable, signed provenance entries.
- Synchronized repository identity with **Aurora Research Initiative** (Waveframe Labs Division).
- Prepared repo for final **v1.2 tag** and Zenodo archival once integration resumes.

### Why It Matters
This closes AWO’s foundational phase: the method and whitepaper are now reproducible, verifiable, and institutionally aligned.  
The next phase (CRI-CORE) will extend these guarantees to runtime and provenance automation.

### Related ADRs
- **ADR-0016** — Automated PDF Build Integration (2025-10-19)
- **ADR-0017** — Documentation Governance under Aurora Research Initiative (2025-10-19)

---


## v1.1.1 — Repository Hardening, Organizational Transfer & Attestation Integration (2025-10-12)

### Summary
This release completes AWO’s transition from individual authorship to institutional governance under **Waveframe Labs**.  
It introduces structural hardening, standardized documentation, and full cryptographic attestation — elevating AWO from procedural reproducibility to verifiable digital trust.

### Key Updates
- Standardized `README.md` files across all primary folders (`/core`, `/schemas`, `/templates`, `/workflows`, `/docs`, `/scripts`, and `/.github`).  
- Added metadata headers to each folder README (filetype, version, updated, maintainer, contact).  
- Unified maintainer identity and contact under **Waveframe Labs** (`swright@waveframelabs.org`).  
- Restored root `README.md` as canonical entry point (resolved `.github` override issue).  
- Verified all references, badges, and license metadata.  
- Implemented cryptographic attestation and OIDC signing via **Sigstore cosign**.  
- Each AWO run now emits verifiable artifacts (`ATTESTATION.txt`, `.sig`, `.cert`) bound to `SHA256SUMS.txt`.  
- Updated `.github/workflows/awo-run.yml` to include attestation generation, signature upload, and verification gates.  
- Deprecated manual `/audit/` validation in favor of automated, tamper-evident verification.  
- Verified attested release integrity via run `run_2025-10-12T14-29-03Z`.  
- Prepared repository for **CRI-CORE** interoperability under Waveframe Labs governance.

### Why It Matters
This marks the point where AWO becomes **institutionally governed** and **cryptographically verifiable**.  
Every workflow run is now signed, hashed, and citable — ensuring provenance, authenticity, and reproducibility can be independently verified.

### Related ADRs
- **ADR-0014** — Repository Hardening and Organizational Transfer to Waveframe Labs (2025-10-11)  
- **ADR-0015** — Attestation Integration & Cryptographic Signing (2025-10-12)

---

## v1.1.0 — Whitepaper + Audit Framework (2025-09-02)
- Added **AWO Whitepaper v1.0** in `/docs/` (Markdown + PDF).  
- Introduced `/decisions/` folder with Architecture Decision Records (ADRs).  
- Expanded `/logs/` with timestamped workflow entries.  
- Updated `README.md` with decision links, concept DOI, and case studies.  
- Updated `.zenodo.json` and `CITATION.cff` with standardized metadata.  
- Refined dual licensing (Apache 2.0 for code, CC BY 4.0 for docs and logs).  

---

## v1.0.2 — Zenodo Integration & DOI Preparation (2025-08-31)
- Added `.zenodo.json` with metadata (title, description, license, identifiers).  
- Added/updated `CITATION.cff` with version and release date.  
- Verified repository visibility and Zenodo webhook linkage.  
- Established DOI badge integration for reproducibility.  

---

## v0.1.0 — Initial Public Release (2025-08-xx)
- Scaffolded repository with base structure and initial `README.md`.  
- Published early draft for visibility before Zenodo integration.

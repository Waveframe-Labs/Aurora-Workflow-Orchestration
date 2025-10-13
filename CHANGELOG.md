# Changelog

## v1.1.1 — Repository Hardening, Organizational Transfer & Attestation Integration (2025-10-12)
- Standardized `README.md` files across all primary folders (`/core`, `/schemas`, `/templates`, `/workflows`, `/docs`, `/scripts`, and `/.github`).  
- Added metadata headers to each folder README (filetype, version, updated, maintainer, contact).  
- Unified maintainer identity and contact to **Waveframe Labs** (`swright@waveframelabs.org`).  
- Restored root `README.md` as the canonical entry point (resolved `.github` override issue).  
- Verified all references, badges, and license metadata.  
- Implemented cryptographic attestation and OIDC signing using **Sigstore cosign**.  
- Each AWO run now emits verifiable artifacts (`ATTESTATION.txt`, `.sig`, `.cert`) binding manifests to `SHA256SUMS.txt`.  
- Updated `.github/workflows/awo-run.yml` to include attestation generation, signature upload, and verification gates.  
- Deprecated manual `/audit/` validation in favor of automated, tamper-evident verification.  
- Confirmed attested release integrity via run `run_2025-10-12T14-29-03Z`.  
- Prepared repository for **CRI-CORE** interoperability under Waveframe Labs governance.

**Why**  
This release completes AWO’s transition from individual authorship to institutional governance under **Waveframe Labs**.  
Structural hardening, standardized documentation, and integrated cryptographic attestation elevate AWO from procedural reproducibility to verifiable digital trust — securing both provenance and governance integrity.

**Related ADRs**  
- ADR-0014 — *Repository Hardening and Organizational Transfer to Waveframe Labs* (2025-10-11)  
- ADR-0015 — *Attestation Integration & Cryptographic Signing* (2025-10-12)

## v1.1.0 — Whitepaper + Audit Framework (2025-09-02)
- Added **AWO Whitepaper v1.0** in `/docs/` (Markdown + PDF).
- Introduced `/decisions/` folder with Architecture Decision Records (ADRs).
- Expanded `/logs/` with timestamped workflow entries.
- Updated `README.md` with decision links, concept DOI, and case studies.
- Updated `.zenodo.json` + `CITATION.cff` with clean metadata.
- Refined dual-licensing (Apache 2.0 for code, CC BY 4.0 for docs/logs).

## v1.0.2 — Zenodo Integration & DOI Preparation (2025-08-31)
- Added `.zenodo.json` with metadata (title, description, license, identifiers).
- Added/updated `CITATION.cff` with version + release date.
- Confirmed repository public status + release process for Zenodo webhook.
- Established DOI badge integration for reproducibility.

## v0.1.0 — Initial Public Release (2025-08-xx)
- Repository scaffolded with basic README and structure.
- Early draft release for visibility before Zenodo integration.

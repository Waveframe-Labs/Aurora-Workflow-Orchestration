# Changelog

## v1.1.1 — Repository Hardening & Organizational Transfer (2025-10-11)
- Standardized `README.md` files across all primary folders (`/core`, `/schemas`, `/templates`, `/workflows`, `/docs`, `/scripts`, and `/.github`).
- Added metadata headers to each folder readme (`filetype`, `version`, `updated`, `maintainer`, `contact`).
- Unified maintainer identity and contact to **Waveframe Labs** (`swright@waveframelabs.org`).
- Restored root `README.md` as canonical entry point (resolved `.github` override issue).
- Verified all references, badges, and license metadata.
- Prepared repository for **CRI-CORE** interoperability under Waveframe Labs governance.

### Why
The organizational migration and documentation hardening ensure AWO operates as an auditable, standardized component of the Waveframe Labs reproducibility ecosystem.  
These changes also finalize the repository’s transition from individual authorship to institutional governance.

### Related ADR
- **ADR-0014** — *Repository Hardening and Organizational Transfer to Waveframe Labs* (2025-10-11)

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

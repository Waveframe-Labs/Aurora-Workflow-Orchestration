# Changelog

## v1.1.1 — Repository Hardening & Org Transfer (2025-10-11)
- Added standardized `README.md` files for all core folders (`/core`, `/schemas`, `/scripts`, `/templates`, `/docs`, `/workflows`, and `/.github`).
- Unified metadata headers across all folder-level readmes (`filetype`, `version`, `updated`, `maintainer`, `contact`).
- Transferred repository ownership to **Waveframe Labs** organization for long-term stewardship.
- Corrected `.github/README.md` overriding issue by re-establishing root `README.md` as canonical entry point.
- Initiated next documentation phase: workflow log revision, changelog synchronization, and ADR updates.
- Designated this release as the **final structural patch** before functional validation and CRI-CORE alignment.
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

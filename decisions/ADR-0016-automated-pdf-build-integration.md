# ADR-0016 — Automated PDF Build Integration
**Date:** 2025-10-19  
**Status:** Accepted  
**Version:** AWO v1.2.0  
**Maintainer:** Shawn C. Wright  
**Affiliation:** Aurora Research Initiative · Waveframe Labs Division

---

## Context
Prior to v1.2.0, AWO documentation required manual export of Markdown files to PDF.  
This introduced variance between Markdown and published artifacts, reduced traceability, and complicated version-locked releases.

---

## Decision
Integrate automated PDF generation directly into the repository using GitHub Actions and Pandoc + XeLaTeX.  
Each Markdown file in `/docs/` now has a dedicated workflow that:

1. Detects changes to the Markdown source.  
2. Builds the corresponding `.pdf` using Pandoc with XeLaTeX.  
3. Commits the generated file via `github-actions[bot]` with full provenance.  

Workflows implemented:
- `.github/workflows/build-whitepaper-pdf.yml`
- `.github/workflows/build-methodspec-pdf.yml`

---

## Consequences
- Documentation reproducibility is guaranteed at the repository level.  
- Each PDF is traceable to a specific commit hash and bot-signed provenance.  
- Manual export is deprecated.  
- Build time increases slightly (~2–3 min) but remains acceptable for continuous verification.  

---

## Alternatives Considered
- **Containerized Pandoc builds:** rejected due to missing Git binaries and commit issues.  
- **External CI builders (OSF / Zenodo triggers):** rejected to maintain local provenance control.

---

## References
- CHANGELOG v1.2.0 — “Automated Documentation Builds & Finalization under Aurora Research Initiative”  
- AWO Whitepaper v1.1 and Method Spec v1.2 (PDF builds)

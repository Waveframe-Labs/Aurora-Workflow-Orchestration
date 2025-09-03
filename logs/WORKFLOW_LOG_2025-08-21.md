# Changelog — AI Workflow Orchestration (AWO)

This changelog tracks the evolution of the **AI Workflow Orchestration (AWO)** repository.  
It documents naming decisions, README development, supporting artifacts, and tagged releases to ensure the project remains reproducible and auditable.

---

## v0.1.0 — Initial Scaffold (August 2025)
- Repository created with placeholder README.  
- Early drafts still referenced “Epistemic Orchestration Method (EOM).”  
- Decision made to remove epistemic framing entirely.  
- Project name locked to **AI Workflow Orchestration (AWO)**.  

---

## v1.0.2 — Zenodo Integration & DOI Preparation (August 2025)
- Added `.zenodo.json` with metadata (title, description, license, identifiers).  
- Added `CITATION.cff` with version, author, and release date.  
- Verified Zenodo concept DOI integration and generated DOI badge.  
- README reframed to emphasize reproducibility, auditability, and human-in-the-loop oversight.  
- Positioning clarified:  
  - **AWO = flagship methodology**  
  - **Waveframe v4.0 = first case study**  
  - Future case studies (e.g., customer review analysis) will test generality.  

---

## v1.1.0 — Whitepaper + Audit Framework (September 2025)
- Added **AWO Whitepaper v1.0** in `/docs/` (Markdown + PDF).  
- Introduced `/decisions/` folder with Architecture Decision Records (ADRs).  
- Expanded `/logs/` with timestamped workflow entries.  
- Updated README to link to decisions, case studies, and Concept DOI.  
- Clarified dual-licensing: Apache 2.0 (code) + CC BY 4.0 (docs/logs).  
- Established AWO as a **fully auditable, reproducible framework**, not just a method draft.  

---

## Current Status
- **README.md** complete and recruiter-facing.  
- **AWO Whitepaper v1.0** published in `/docs/`.  
- **/decisions/** and **/logs/** provide audit trail of design choices and workflow evolution.  
- Zenodo Concept DOI minted: [10.5281/zenodo.17013612](https://doi.org/10.5281/zenodo.17013612).  
- Waveframe v4.0.5 archived as the first major case study demonstrating AWO in practice.  

AWO is formally established as the **flagship repository**, with case studies serving as proofs of generality across domains.

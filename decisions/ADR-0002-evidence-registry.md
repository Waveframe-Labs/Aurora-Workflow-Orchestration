# ADR-0002 — Evidence Registry & Citation Policy

## Status
Proposed — 2025-08

## Context
One of AWO’s non-negotiable requirements is **falsifiability backed by evidence**.  
User created `citations/REPRODUCIBILITY_CONTEXT.md` to document real (non-AI-generated) sources addressing reproducibility failures in AI, workflow systems, and auditability.    
Dialogue validated that AWO aligns with research directions (Reis 2022; Goble 2020; Chirigati 2016; Amershi 2019).

To maintain credibility, AWO needs a consistent policy for handling citations across repos and outputs.

## Decision
- All scholarly references must be stored in **`citations/citation.bib`** (BibTeX format).  
- Supporting context files (e.g., `REPRODUCIBILITY_CONTEXT.md`) remain in `/citations/` as human-readable summaries.  
- Every claim in the AWO Method Spec or README that references external research must:  
  - Link to the relevant BibTeX entry by citation key.  
  - Be reproducible across formats (Markdown → PDF → README → Whitepaper).  
- When non-AI-generated citations are used, they must be explicitly labeled as such.  
- AI-generated references are prohibited unless they can be independently verified.  

## Consequences
- Guarantees reproducibility of scholarly grounding for AWO.  
- Prevents future critiques that AWO relies on unverifiable or fabricated references.  
- Makes the audit trail stronger by linking Decisions Logs → Citations → README/Spec.  
- Adds maintenance overhead: new case studies must keep `citation.bib` synced.
  

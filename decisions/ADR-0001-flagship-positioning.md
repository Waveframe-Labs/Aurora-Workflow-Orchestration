# ADR-0001 — Flagship Positioning & Case-Study Policy

## Status
Accepted — 2025-08

## Context
Early drafts of this repository used multiple names (“EOM,” “AOM,” “AWO”).  
External feedback highlighted the need for clarity:  
- AWO is **not ad-hoc**  
- AWO is **novel and scientifically relevant**  

At the same time, Waveframe and other projects were being developed. The risk was confusion over what the “main contribution” is: the cosmology case study, or the orchestration method itself.

## Decision
- The flagship repository is **Aurora Workflow Orchestration (AWO)**.  
- Case studies (Waveframe, Customer Review Analysis, Societal Progress Simulator, etc.) serve as **demonstrations of AWO’s portability and generality**, not as standalone flagships.  
- README and metadata must always position AWO as the **methodological layer** and case studies as **applications**.  
- Dialogue logs and workflow logs must explicitly link back to AWO when case study work influences or validates the method.

## Consequences
- Ensures recruiters, researchers, and auditors immediately recognize AWO as the primary contribution.  
- Prevents dilution of AWO’s identity as “just documentation of Waveframe.”  
- Case studies remain valuable, but their role is scoped: they validate AWO across domains.  
- Future ADRs (e.g., ADR-0005: Portability Guarantees) will formalize how case studies must log orchestration steps to remain compliant with AWO.

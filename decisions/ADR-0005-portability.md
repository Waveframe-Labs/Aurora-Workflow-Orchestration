# ADR-0005 — Portability Guarantees

## Status
Proposed — 2025-09

## Context
One of the five core requirements of AWO is **Portability**:  
> Everything you produce should be template-driven so the method applies in any domain.  

Without explicit portability guarantees, AWO risks being seen as a one-off documentation project tied to a single case study (Waveframe).

## Decision
- All AWO artifacts must be **domain-agnostic by design**.  
- Templates must be included for:  
  - **Falsifiability manifests** (`templates/falsifiability-manifest.md`)  
  - **Audit checklists** (`templates/audit-checklist.md`)  
  - **Workflow log entries** (`templates/worklog-entry.md`)  
- Repositories using AWO (case studies) must adopt these templates without altering core structure.  
- AWO’s README and whitepaper must explicitly state:  
  - Swap the domain → keep the method.  
  - Case studies exist to prove portability, not to redefine it.  
- ADRs in case studies must reference the AWO parent repo when portability is demonstrated or tested.

## Consequences
- Ensures AWO is not tied to cosmology or any one project.  
- Provides a clear path for adoption in science, business, or social domains.  
- Prevents case studies from drifting into “customized forks” of the method.  
- Adds initial overhead to maintain high-quality templates, but lowers adoption friction for others.

## References
- ADR-0001 — Flagship Positioning & Case-Study Policy  

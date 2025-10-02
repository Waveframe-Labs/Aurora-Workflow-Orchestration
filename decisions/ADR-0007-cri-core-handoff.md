# ADR-0007-cri-core-handoff
**Title:** Separation of AWO (Method) and CRI-CORE (Pipeline Code)  
**Status:** Accepted  

## Context  
AWO is a methodological anchor; CRI-CORE is the tooling implementation. Mixing them would confuse scope and dilute credibility.  

## Decision  
- **AWO repo** = method, governance, templates, whitepaper.  
- **CRI-CORE repo** = pipelines, runner code, schemas, CI logic.  
- Explicit references must always use **CRI-CORE** as the implementation layer.  

## Consequences  
- Clearer positioning for AWO as a methodology.  
- CRI-CORE can evolve faster without destabilizing the method.  
- Users know which repo to fork for reproducibility vs methodology.  

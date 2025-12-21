# ADR-0009-case-studies
**Title:** Case Studies as Validation Mode  
**Status:** Accepted  

## Context  
Some projects (Waveframe, Societal Progress Simulator) were orchestrated manually, not via CRI-CORE pipelines. They still serve as stress tests for AWO.  

## Decision  
- Case studies are logged as **AWO-orchestrated** even if run manually.  
- Only studies with falsifiability, logs, and reproducibility evidence qualify.  
- Case study inclusion requires explicit “case study ADR” with scope + outcomes.  

## Consequences  
- Expands AWO’s credibility through applied demonstrations.  
- Keeps boundaries: case studies are *validation*, not *method core*.  

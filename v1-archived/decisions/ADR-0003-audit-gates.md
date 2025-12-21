# ADR-0003 — Audit Gates & Rejection Loop

## Status
Proposed — 2025-09

## Context
One of AWO’s five core requirements is the **Rejection Loop**: failed audits must trigger revision, not defense without evidence.    

Without explicit audit gates, AWO risks collapsing into the same ad-hoc practices it aims to replace.

## Decision
- Every tagged release of AWO (or a case study using AWO) must include an **Audit Report** in `/logs/audits/`.  
- Each audit report must record:  
  - **Context** — what artifact was reviewed (README, method spec, figure, dataset).  
  - **Auditor** — independent reviewer (different model, human, or both).  
  - **Feedback** — summary of critiques.  
  - **Decision** — accept, reject, or revise.  
  - **Status** — outcome (accepted/revised/rejected).  
- If an artifact fails an audit:  
  - Revision is mandatory before inclusion in a release.  
  - Rejections must be logged and explained (no silent drops).  
- ADRs that emerge from rejected work must cite the rejection event.  

## Consequences
- Guarantees that audits are a **release blocker**, not optional feedback.  
- Strengthens the audit trail: every accepted artifact has at least one explicit independent check.  
- Prevents defensive reasoning — forces iteration or withdrawal when evidence is lacking.  
- Adds overhead: each release requires independent audit steps before publication. 

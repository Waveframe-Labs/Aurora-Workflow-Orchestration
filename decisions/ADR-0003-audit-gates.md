# ADR-0003 — Audit Gates & Rejection Loop

## Status
Proposed — 2025-09-05

## Context
One of AWO’s five core requirements (DL-001) is the **Rejection Loop**: failed audits must trigger revision, not defense without evidence.  
Dialogue Logs DL-001 and DL-005 both reinforce this:  
- DL-001 framed independent audits and rejection as non-negotiable.  
- DL-005 confirmed that trust in AI-assisted science depends on logging, validation, and human oversight.  

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

## References
- Dialogue Log DL-001 — “5 Requirements” framing (LinkedIn draft → method spec)  
- Dialogue Log DL-005 — “Does AWO have scientific value?” (Consensus AI)  

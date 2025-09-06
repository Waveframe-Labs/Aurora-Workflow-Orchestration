# Logs — AI Workflow Orchestration (AWO)

This folder contains the logging artifacts that make AWO auditable and reproducible.  
Logs are a **first-class artifact** of the workflow — if it isn’t logged here, it didn’t shape AWO.

---

## Contents
- **dialogue-log.md** — Rolling record of influential external dialogues (LLM feedback, peer review, third-party critique).  
  - Each entry has a DL ID (`DL-YYYY-MM-DD-NNN`) and cross-links to related ADRs and commits.  
  - Purpose: show how outside input shaped decisions, claims, and repo artifacts.  

- **workflow-log.md** — Factual chronological record of internal steps.  
  - Covers repo creation, renames, releases, README revisions, file generation, and other procedural moves.  
  - Purpose: preserve the audit trail of what happened and when.

---

## Logging principles
1. **Completeness** → If a dialogue or action influenced AWO, it belongs here.  
2. **Cross-linking** → Each entry ties back to ADRs, commits, or claims.  
3. **Minimalism** → Keep excerpts short; link or reference full threads/files elsewhere if needed.  
4. **Falsifiability** → Every logged claim or decision must be testable or rejectable.  
5. **Traceability** → Logs must allow anyone to reconstruct not only what was decided, but why.

---

## Protocol
- Dialogue logs → Prefix with **DL-YYYY-MM-DD-NNN**. Store long transcripts under `/logs/dialogue/raw/` if needed.  
- Workflow logs → Record factual changes with version tags, timestamps, and rationale.  
- Always update ADRs to point back to relevant log entries.  
- When a log entry leads to a commit, add the commit/PR link in the **Links** field.

---

### Maintainer note
Logs are **not optional**. They are the evidence backbone of AWO.  
Without logs, orchestration reduces to undocumented prompting — exactly what AWO exists to avoid.
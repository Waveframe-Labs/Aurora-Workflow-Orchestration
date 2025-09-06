# Dialogue Log — AI Workflow Orchestration (AWO)

Purpose: preserve influential external model feedback (and our responses) that shaped AWO.  
Scope: conceptual input, critiques, validation, and framing from non-repo sources (LLMs, reviewers).  
Linkage: each entry cites the repo artifacts it influenced (README, spec, templates, ADRs, releases).

## How to use this log
- One entry per dialogue thread.  
- Keep excerpts minimal; link to full text if stored elsewhere.  
- Every entry must list: **Participants, Source, Artifacts Touched, Impact, Next Action.**  
- When an ADR or commit lands, add the ID/URL under **Links**.

---

## Index
- DL-2025-09-04-001 — “5 Requirements” framing (LinkedIn draft prompt → method pillars)  
- DL-2025-09-04-002 — Reproducibility Context file review (evidence & positioning)  
- DL-2025-09-04-003 — “Is AWO ad-hoc?” (third-party validation)  
- DL-2025-09-04-004 — “Is this new?” (novelty statement)  
- DL-2025-09-04-005 — “Does AWO have scientific value?” (literature-aligned validation)

---

### DL-2025-09-04-001 — “5 Requirements” framing
**Date**: 2025-09-04  
**Participants**: User ↔ External Model  
**Source**: Prompt about a LinkedIn post; model proposed core requirements.  
**Key excerpt**:  
> Falsifiability, Logging, Independent audits, Rejection loop, Portability.  
**Artifacts touched**:  
- `docs/AWO_Method_Spec_v1.1.md` (sections 2–3)  
- `templates/falsifiability-manifest.md`, `templates/audit-checklist.md`, `templates/worklog-entry.md`  
- `logs/README.md` (schema)  
- **ADR-0003** (Audit gates & rejection loop)  
**Impact**: Became AWO’s five non-negotiables; basis for conformance.  
**Next action**: Encode tests for each requirement in the release checklist.  
**Links**: [`decisions/ADR-0003.md`](../decisions/ADR-0003.md)  

---

### DL-2025-09-04-002 — Reproducibility Context file review
**Date**: 2025-09-04  
**Participants**: User ↔ External Model  
**Source**: Review of `citations/REPRODUCIBILITY_CONTEXT.md`.  
**Key excerpt**:  
> Anchors AWO in scholarship; bridges workflow systems to reasoning; documents credibility with non-AI citations.  
**Artifacts touched**:  
- `citations/REPRODUCIBILITY_CONTEXT.md` (kept internal evidence registry)  
- README (“Why It Matters”) phrasing  
- **ADR-0002** (Evidence registry & citation policy)  
**Impact**: Confirms AWO is generalizable beyond Waveframe; strengthens audit trail.  
**Next action**: Optional public summary graphic; keep full registry in‐repo.  
**Links**: [`decisions/ADR-0002.md`](../decisions/ADR-0002.md)  

---

### DL-2025-09-04-003 — “Is AWO ad-hoc?”
**Date**: 2025-09-04  
**Participants**: User ↔ Consensus AI (README shared anonymously)  
**Source**: Binary challenge (“Is this ad-hoc?”).  
**Key excerpt**:  
> AWO is explicitly the opposite of ad-hoc; it embeds reproducibility, falsifiability, documented cycles, and versioned outputs.  
**Artifacts touched**:  
- README (definition of AWO; workflow cycle figure caption)  
- **ADR-0001** (Flagship positioning)  
**Impact**: Third-party validation that AWO is a **framework**, not opportunistic usage.  
**Next action**: Cite this dialogue in ADR-0001 context.  
**Links**: [`decisions/ADR-0001.md`](../decisions/ADR-0001.md)  

---

### DL-2025-09-04-004 — “Is this new?”
**Date**: 2025-09-04  
**Participants**: User ↔ Consensus AI  
**Source**: Question on novelty.  
**Key excerpt**:  
> New: makes AI-assisted reasoning itself auditable and reproducible.  
> Builds on: Galaxy/Nextflow (pipelines), open science, process auditing.  
**Artifacts touched**:  
- `docs/AWO_Method_Spec_v1.1.md` (Background/Related Work)  
- README (novelty note)  
- **ADR-0005** (Portability guarantees)  
**Impact**: Positions AWO as novel within scientific method development.  
**Next action**: Map explicit “extends vs. differs” table vs. Galaxy/Nextflow/CWL.  
**Links**: [`decisions/ADR-0005.md`](../decisions/ADR-0005.md)  

---

### DL-2025-09-04-005 — “Does AWO have scientific value?”
**Date**: 2025-09-04  
**Participants**: User ↔ Consensus AI  
**Source**: Value challenge.  
**Key excerpt**:  
> Yes. Literature notes AI reduces reproducibility without structure; workflow orchestration improves reliability; auditability builds trust; human–AI collaboration needs frameworks.  
**Artifacts touched**:  
- `citations/citation.bib` (add: Reis 2022; Goble 2020; Chirigati 2016; Amershi 2019)  
- README (“Why It Matters” references)  
- **ADR-0002** (Evidence registry & citation policy)  
**Impact**: Aligns AWO with active research, clarifies the gap it fills.  
**Next action**: Cross-link each claim in the spec to a bib entry.  
**Links**: [`decisions/ADR-0002.md`](../decisions/ADR-0002.md)  

---

## Logging protocol
- New external input that shapes scope, claims, or method → add a **DL-YYYY-MM-DD-NNN** entry.  
- Keep excerpts short; store long transcripts in `/logs/dialogue/raw/` if needed.  
- Every decision derived from a dialogue must reference the **DL ID** in the ADR.  
- When you merge a change that implements an entry, circle back and add the commit/PR link.

---

## Cross-references
- [`decisions/ADR-0001.md`](../decisions/ADR-0001.md) — Flagship positioning (AWO vs case studies)  
- [`decisions/ADR-0002.md`](../decisions/ADR-0002.md) — Evidence registry & citation policy  
- [`decisions/ADR-0003.md`](../decisions/ADR-0003.md) — Audit gates and rejection loop as release blockers  
- [`decisions/ADR-0004.md`](../decisions/ADR-0004.md) — Logging schema (minimum fields; where dialogue/workflow/audits live)  
- [`decisions/ADR-0005.md`](../decisions/ADR-0005.md) — Portability guarantees (templates, repo-agnostic config)  

---

### Maintainer note
This log is part of the audit trail. If it isn’t logged here, it didn’t influence AWO.
# unified_audit_2025-09-13.md
**Date:** 2025-09-13  
**Scope:** docs/AWO_Method_Spec_v1.1.md  
**Commit/tag:** not provided  
**Sources:** Claude Sonnet 4, GPT-5, Gemini 1.5 Flash  

---

## Executive Summary
The method spec is strong, detailed, and well-structured. Its biggest weaknesses are:  
1. **Normative requirements** use strong language (“MUST/SHOULD”) but lack operational definitions or test criteria.  
2. **Auditor independence** is asserted but not practically enforceable given shared model biases.  
3. **Artifacts and logs** are referenced but without required schemas or completeness to ensure reproducibility.  
4. **Lifecycle and setup steps** are text-heavy and under-specified; visuals and concrete procedural detail are missing.  
5. **Evidence/examples:** need more examples across domains, plus links to repo artifacts.  

**Top Risks (High severity):**  
- Ambiguity in falsifiability/test requirements.  
- Insufficient logging schema for reproducibility.  
- Lack of independence criteria for auditors.  

---

## Severity Heatmap
| File                          | Critical | High | Medium | Low | Nit |
|-------------------------------|----------|------|--------|-----|-----|
| AWO_Method_Spec_v1.1.md       | 0        | 4    | 5      | 4   | 1   |

---

## Detailed Findings

### F1 – Falsifiability requirements under-defined
- **Category:** reproducibility/docs | **Severity:** High | **Impact:** 3 | **Confidence:** 0.93  
- **Canonical Statement:** The spec’s falsifiability requirement (“Every claim MUST have a concrete test”) lacks guidance on what counts as an adequate test.  
- **Evidence:** GPT-5 DOCS-007; Claude SPEC-001; Gemini METH-002.  
- **Fix:** Add compliance matrix + concrete examples (adequate vs. inadequate tests). Include a parenthetical mini-example.  

---

### F2 – Auditor independence unclear
- **Category:** reproducibility/logic | **Severity:** High | **Impact:** 3 | **Confidence:** 0.83  
- **Canonical Statement:** Auditor independence is asserted but not enforced; no rules prevent overlap or shared biases.  
- **Evidence:** GPT-5 DOCS-008; Claude SPEC-002.  
- **Fix:** Define independence rules (e.g., different model families, separate prompting contexts, or human oversight).  

---

### F3 – Logging schema insufficient
- **Category:** reproducibility | **Severity:** High | **Impact:** 3 | **Confidence:** 0.87  
- **Canonical Statement:** Logging schema defines only minimal fields, which are inadequate for reproducing decisions.  
- **Evidence:** GPT-5 DOCS-011; Claude SPEC-004.  
- **Fix:** Standardize log format (YAML front-matter + Markdown body) with extra fields: input params, model versions, alternatives considered, rejection rationale.  

---

### F4 – Artifacts underspecified
- **Category:** reproducibility/docs | **Severity:** Medium | **Impact:** 2 | **Confidence:** 0.80  
- **Canonical Statement:** Core artifacts are referenced but file formats/schemas are unspecified.  
- **Evidence:** GPT-5 DOCS-009.  
- **Fix:** Define metadata schema for each artifact type (JSON for registries, Markdown for manifests, etc.).  

---

### F5 – Setup procedures incomplete
- **Category:** docs | **Severity:** Medium | **Impact:** 2 | **Confidence:** 0.85  
- **Canonical Statement:** Step 0 (Setup) lacks procedural detail for defining claims and baselines.  
- **Evidence:** Claude SPEC-003.  
- **Fix:** Add substeps: SMART criteria, quantitative baselines, documentation of audit criteria.  

---

### F6 – Lifecycle lacks timing/frequency guidance
- **Category:** docs | **Severity:** Low | **Impact:** 1 | **Confidence:** 0.75  
- **Canonical Statement:** Lifecycle is described but cadence/iteration frequency is unspecified.  
- **Evidence:** GPT-5 DOCS-010.  
- **Fix:** Add iteration length guidance (e.g., per hypothesis, per dataset update).  

---

### F7 – Lifecycle presentation is dense
- **Category:** docs | **Severity:** Low | **Impact:** 1 | **Confidence:** 0.90  
- **Canonical Statement:** Lifecycle is text-heavy; visuals would improve clarity.  
- **Evidence:** Gemini METH-001.  
- **Fix:** Add flowchart or diagram (as in README).  

---

### F8 – Rejection handling rigid
- **Category:** logic | **Severity:** Medium | **Impact:** 2 | **Confidence:** 0.70  
- **Canonical Statement:** No-appeals policy may block correction of audit errors.  
- **Evidence:** Claude SPEC-005.  
- **Fix:** Allow appeals on procedural errors while preserving “no appeals without new evidence.”  

---

### F9 – Model Roster undefined
- **Category:** docs | **Severity:** Low | **Impact:** 1 | **Confidence:** 0.80  
- **Canonical Statement:** The spec references a Model Roster but does not define its structure or location.  
- **Evidence:** Claude SPEC-006.  
- **Fix:** Define structure (e.g., `/config/model_roster.yaml`) with required fields.  

---

### F10 – Conformance checklist lacks thresholds/links
- **Category:** reproducibility/docs | **Severity:** Medium | **Impact:** 2 | **Confidence:** 0.73  
- **Canonical Statement:** Conformance checklist lacks quantitative thresholds and repo links.  
- **Evidence:** GPT-5 DOCS-012; Claude SPEC-007.  
- **Fix:** Add thresholds (e.g., ADR affects >20% of workflow) and hyperlink to examples in repo.  

---

### F11 – Example scope too narrow
- **Category:** docs | **Severity:** Medium | **Impact:** 2 | **Confidence:** 0.80  
- **Canonical Statement:** Only one example (Waveframe v4.0.5) is given; insufficient domain coverage.  
- **Evidence:** Claude SPEC-009.  
- **Fix:** Add 2–3 examples from different domains.  

---

### F12 – Claim ID format scalability
- **Category:** data | **Severity:** Low | **Impact:** 1 | **Confidence:** 0.60  
- **Canonical Statement:** Current claim ID format (CLM-001) may not scale for large projects.  
- **Evidence:** Claude SPEC-008.  
- **Fix:** Use hierarchical/domain-prefixed IDs.  

---

### F13 – Ambiguity in term “continuity”
- **Category:** docs | **Severity:** Nit | **Impact:** 1 | **Confidence:** 0.70  
- **Canonical Statement:** “Main Model (Continuity)” is ambiguous.  
- **Evidence:** Gemini METH-003.  
- **Fix:** Clarify meaning of continuity in context.  

---

## Notes
All three auditors agree: the document is professionally structured and strong. Weaknesses cluster around operationalizing requirements (falsifiability, logging, independence). Fixes should emphasize **concrete schemas, examples, and repo-linked evidence**.

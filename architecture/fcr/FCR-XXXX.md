# Formal Change Request (FCR-XXXX)
**Status:** draft  
**Type:** architecture-change  
**Governance:** ARI  
**Requested by:** Shawn C. Wright (ORCID: 0009-0006-6043-9295)  
**Date Submitted:** YYYY-MM-DD  
**Affected Version:** v1.4  
**Target Version:** v1.5 (or next)  

---

## 1. Summary
A concise description of the proposed architecture change.

- What needs to change?
- Why is the change being proposed now?
- Is this a correction, addition, removal, or refactor?

---

## 2. Motivation
Explain the rationale for this change.

- What architectural, governance, or workflow gap does it resolve?
- What new requirement, insight, or constraint triggered the proposal?
- Are there risks if this change is not applied?

---

## 3. Scope of Change
List all affected documents, components, or specifications.

Common examples:

- `/architecture/AWO_DAG_FULL-EXPANSION.md`
- `/architecture/AWO_BACKLOG-LEDGER_v1.4.md`
- `/architecture/CPP_v1.0.md`
- Invariants Document
- Metadata Policy
- Method Spec
- NTS Spec
- Index.json Schema
- Kernel Definitions

If code or workflows are affected, list:

- CRI workflow
- metadata pipeline
- doc guard rules
- validation or schema logic
- CI/CD policies

---

## 4. Dependency Impact
Describe how the proposed change affects the DAG and backlog.

- Does the change introduce new dependencies?
- Do existing dependencies shift or collapse?
- Does sequencing or Critical Path require adjustment?
- Does it modify any root primitive?

If changes affect:

- (1) Invariants Document  
- (2) Doc Guard  
- (4) CRI Stability  

…then this is a **breaking architecture change** and must be flagged.

---

## 5. Compatibility & Migration
Explain whether this change:

- is backward-compatible  
- requires migration steps  
- requires document rewrites  
- introduces version incompatibility  

For incompatible updates:

- specify deprecation strategy  
- propose migration timeline  
- define archived version references  

---

## 6. Proposed Changes (Exact Edits)
Detail every modification in a precise, patch-like format.

Example format:
```
File: achitecture/AWO_DAG_FULL_EXPANSION.md
Change:
- Add new child inder node (16) Versioning Protocol
- Remove outdated references to (7) Badge System
- Update dependency table accordingly
```

Or include diff blocks when appropriate.

---

## 7. Validation & Checks
List validation steps that must be performed after applying the change.

Typical checks:

- DAG validation  
- Backlog coherence  
- CPP alignment  
- Doc Guard pass  
- Metadata pipeline pass  
- Schema validation  
- Run history invariants  
- Versioning protocol compatibility  

If relevant: include demonstration runs or reproducibility checks.

---

## 8. Risks & Mitigations
Describe risks introduced by the change and how to mitigate them.

Examples:

- inconsistent metadata  
- dependency drift  
- pipeline failure  
- misalignment with governance  
- breaking old kernels  
- confusion in public artifacts  

---

## 9. Review & Approval
Record the governance review process.  
```
Reviewed by:
Decision: approved / rejected / needs revision
Reviewer Notes:
Approval Date:
Version Changes Applied:
```

---

## 10. Post-Approval Actions
Checklist of required steps after approval:

- [ ] Apply changes to architecture documents  
- [ ] Update metadata headers after pipeline is active  
- [ ] Adjust Backlog version (e.g., v1.4 → v1.5)  
- [ ] Update DAG and CPP  
- [ ] Commit with reference: “Implements FCR-XXXX”  
- [ ] Publish updated architecture snapshot  
- [ ] Assign DOI to new version (when applicable)

---

## 11. Attachments (Optional)
Include supporting notes, diagrams, logs, or validation outputs.  
```
/attachments/FCR-XXXX/
└── diagrams/
└── diffs/
└── analysis/
```

---

**End of FCR-XXXX**

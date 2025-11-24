# Attachments for Formal Change Requests (FCR)
**Aurora Research Initiative (ARI) — Architecture Governance**

This directory stores all supporting materials for **Formal Change Requests (FCRs)**.

Attachments are optional but strongly encouraged when proposing any  
non-trivial architecture modification (e.g., DAG updates, invariant changes,  
schema adjustments, or versioning protocol changes).

---

## Purpose

Attachments provide **evidence**, **visuals**, and **context** needed to:

- justify a proposed architecture change  
- illustrate dependency impacts  
- show diffs and comparisons  
- include diagrams, drafts, schemas, or logs  
- preserve provenance for later reviewers  

They serve as permanent records that support the decisions documented  
in each FCR.

---

## Directory Structure

Attachments for each change request must be stored under:

```
/architecture/fcr/attachments/FCR-XXXX/
```

Example:

```
/architecture/fcr/attachments/FCR-0001/
    diagrams/
    diffs/
    logs/
    analysis/
```

You may create additional subfolders as needed.

---

## Naming Rules

All attachments must follow these rules:

- Store only materials relevant to a **specific FCR**  
- Use the FCR ID as the folder name  
- Never mix materials between FCR IDs  
- Keep binary files (images, diagrams, logs) here rather than cluttering the main architecture directory  
- Avoid timestamps in filenames (Windows-safe rule)  
- Use lowercase, hyphen-separated filenames  

Examples:

```
dependency-graph-updated.png
run-history-diff.md
meta-policy-analysis.txt
flowchart-refactor.svg
```

---

## When Attachments Are Required

Include attachments when the FCR proposes:

- changes to the DAG  
- changes to critical path (CPP)  
- updates to invariants  
- updates to versioning protocol  
- metadata schema changes  
- CRI workflow modifications  
- governance or compliance changes  
- any modification that requires validation evidence  

For simple editorial or textual updates, attachments are optional.

---

## Metadata

Attachments **do not** require metadata headers.  
They inherit metadata from:

- the parent FCR document  
- the architecture baseline version  
- the repository commit metadata

The metadata pipeline will ignore attachment files.

---

## Notes

This directory exists to maintain clarity, reviewability, and provenance  
for all architectural evolution of the AWO/CRI system.

If you need the directory scaffold for a specific FCR (e.g., FCR-0002),  
ask and it can be generated automatically.

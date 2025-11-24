# Formal Change Requests (FCR)
**Aurora Research Initiative (ARI) — Architecture Governance**

This directory contains all **Formal Change Requests (FCRs)** related to the  
frozen architecture documents of the AWO/CRI system.

FCRs define how architectural modifications are proposed, reviewed, approved,  
and integrated. No architecture-level file may be changed without an approved FCR.

---

## Purpose

The FCR process ensures that changes to the system’s architecture are:

- **traceable**  
- **deliberate**  
- **reviewed**  
- **versioned**  
- **aligned with ARI governance**  
- **compatible with the AWO/CRI dependency graph**

This protects the integrity of the architecture baseline (v1.4) and  
prevents accidental drift or uncontrolled revisions.

---

## Directory Structure
```  
/architecture/fcr/  
README.md # This file  
FCR-0001.md # First change request (placeholder)  
FCR-0002.md # (future)  
...  
attachments/  
FCR-0001/ # Supporting diagrams, logs, diffs, analysis  
...  
```  
Each FCR file covers:

- proposed change  
- rationale  
- affected dependencies  
- impact on the DAG, backlog, and CPP  
- validation steps  
- version increment  
- reviewer approval  
- post-approval actions  

See **FCR-0001.md** for the template used for all future requests.

---

## When an FCR Is Required

Submit an FCR when modifying **any file under**:
```
/architecture/
/architecture/fcr/
/invariants/
/governance/
/schemas/
/kernel-definitions/
/method-spec/
/nt-spec/
```

Or when proposing changes to:

- the architecture DAG  
- the backlog ledger  
- the critical path plan (CPP)  
- invariants  
- versioning protocol  
- run history rules  
- metadata policy  
- kernel validation rules  
- governance structure

If in doubt: **submit an FCR.**

---

## FCR Lifecycle

### 1. Draft →  
Author creates a new file: `FCR-XXXX.md`  
(using the standardized template).

### 2. Review →  
Proposal is evaluated for:
- architectural correctness  
- dependency integrity  
- backward compatibility  
- metadata schema impact  
- governance alignment  

### 3. Decision →  
Status becomes:
- **approved**  
- **rejected**  
- **needs revision**

### 4. Implementation →  
If approved:
- architecture docs are updated  
- DAG/backlog/CPP revised  
- metadata updated (post-pipeline)  
- version numbers incremented  
- DOI assignments updated if necessary  

### 5. Closure →  
FCR is archived as permanent record.

---

## Numbering Scheme

FCR IDs use strict four-digit incremental numbering:
```
FCR-0001.md
FCR-0002.md
FCR-0003.md
...
```

Numbers **must never be reused**.

---

## Governance Classification

All FCRs are considered:
```
governance: ARI Architecture Change
status: archival records
```

They form part of the system’s permanent provenance record.

---

## How to Submit a New FCR

1. Duplicate `FCR-0001.md` (the template)  
2. Rename to the next available ID  
3. Fill out all fields  
4. Save under `/architecture/fcr/`  
5. Add any attachments under `/architecture/fcr/attachments/FCR-XXXX/`  
6. Commit with a message:
```
Add FCR-XXXX: <summary>
```

---

## Notes

- FCRs do **not** replace normal issue tracking.  
- FCRs apply only to architecture-level documents and specifications.  
- Lower-level implementation changes (code, examples, demos) do **not** require FCRs unless they break architecture rules.

---

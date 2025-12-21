# AWO v4.2 — Test Suite Execution DAG (v1.0)

## 1. Overview

This document specifies the correct execution order and dependency relationships for the AWO v4.2 test suite.

All tests must be executed in DAG order.  
No test may be executed before its dependencies pass.

---

## 2. High-Level DAG Graph

                     ┌─────────────┐
                     │  DAG START  │
                     └──────┬──────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Layer I: Governance │
                 │     Tests G1–G6     │
                 └─────────┬──────────┘
                           │
                All G-tests MUST pass
                           │
                           ▼
           ┌─────────────────────────────────┐
           │ Layer II: Integrity Tests I1–I5 │
           └───────────────┬─────────────────┘
                           │
                All I-tests MUST pass
                           │
                           ▼
          ┌──────────────────────────────────────┐
          │ Layer III: Determinism Tests D1–D3   │
          └─────────────────┬────────────────────┘
                            │
                All D-tests MUST pass
                            │
                            ▼
      ┌──────────────────────────────────────────────┐
      │ Layer IV: Identity + Attestation A1–A4       │
      └─────────────────────────┬────────────────────┘
                                │
                    All A-tests MUST pass
                                │
                                ▼
        ┌───────────────────────────────────────────┐
        │ Layer V: Pipeline Logic Tests P1–P4       │
        └───────────────────────────┬───────────────┘
                                    │
                      All P-tests MUST pass
                                    │
                                    ▼
     ┌────────────────────────────────────────────────┐
     │ Layer VI: Structural Provenance Tests S1–S3     │
     └───────────────────────────────┬────────────────┘
                                     │
                                     ▼
                         ┌──────────────────┐
                         │   DAG COMPLETE   │
                         └──────────────────┘

---

## 3. Detailed Layer Dependencies

### Layer I — Governance Matrix (G1–G6)

**G1 — Self-Approval Blocked (Clean Pass)**  
- Requires: none  
- Produces baseline independence record

**G2 — Self-Approval Attempt (Blocked)**  
- Requires: G1

**G3 — Override Self-Approval Allowed**  
- Requires: G2

**G4 — Override Cannot Bypass Invariant Failure**  
- Requires: G3

**G5 — Cross-Account Clean Pass**  
- Requires: G4

**G6 — Cross-Account Attestation Mismatch**  
- Requires: G5

---

### Layer II — Integrity (I1–I5)

**I1 — Post-Checksum Mutation Detection**  
- Requires: All G-tests

**I2 — Partial Artifact Injection Detection**  
- Requires: I1

**I3 — Integrity Verification Before Attestation**  
- Requires: I2

**I4 — Canonical Tarball Creation**  
- Requires: I3

**I5 — rsync/Copy Behavior Stability**  
- Requires: I4

---

### Layer III — Determinism (D1–D3)

**D1 — Deterministic Artifact Reproduction**  
- Requires: All I-tests

**D2 — JSON Canonicalization**  
- Requires: D1

**D3 — Timestamp Isolation**  
- Requires: D2

---

### Layer IV — Identity + Attestation (A1–A4)

**A1 — Role Spoofing Prevention**  
- Requires: D-tests

**A2 — Approval Bound to SHA Root**  
- Requires: A1

**A3 — No Signing Before Integrity Pass**  
- Requires: A2

**A4 — Reviewer Identity Hash & Placement**  
- Requires: A3

---

### Layer V — Pipeline Logic & Replay (P1–P4)

**P1 — Gate2 Hard Stop**  
- Requires: A-tests

**P2 — Manual Commit Bypass Blocked**  
- Requires: P1

**P3 — Payload Race Condition Defense**  
- Requires: P2

**P4 — Final Commit Invariant Chain Check**  
- Requires: P3

---

### Layer VI — Structural Provenance (S1–S3)

**S1 — Provenance Index Update**  
- Requires: P-tests

**S2 — Run-Graph Completeness**  
- Requires: S1

**S3 — Failure Taxonomy Coverage**  
- Requires: S2

---

## 4. Completion Rule

The suite is complete when:

- All G, I, D, A, P, S layers pass in DAG order
- No test is skipped
- All required logs, attestations, indexes, and invariants exist

---

# END OF DOCUMENT

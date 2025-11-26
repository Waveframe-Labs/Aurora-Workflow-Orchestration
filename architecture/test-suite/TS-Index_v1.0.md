# TS-Index.md (v1.0)
AWO v4.2 — Test Suite Master Index

This document defines the authoritative list of all tests in the AWO v4.2 verification suite.  
Each test is listed with a stable ID, minimal description, required inputs, and expected output behavior.

Tests are grouped by layer, reflecting the governance DAG.

---

# Layer I — Governance Matrix Tests (G1–G6)

## TS-0001 — G1: Self-Approval Blocked (Clean Pass)
Description: Validate that self-approval is blocked when allow_self_approval="0".
Inputs:
- Orchestrator = user_A
- Reviewer = user_B
- allow_self_approval=0
Expected Result: Run passes Gate2. Independence log created.
Codes: none

## TS-0002 — G2: Self-Approval Attempt (Blocked)
Description: Orchestrator attempts to approve own run with default governance settings.
Inputs:
- Orchestrator = Reviewer = same
- allow_self_approval=0
Expected: Gate2 fails with GOV-001.
Codes: GOV-001

## TS-0003 — G3: Override Self-Approval Allowed
Description: Explicit override enables self-approval.
Inputs:
- Orchestrator = Reviewer
- allow_self_approval=1
Expected: Gate2 succeeds; override logged.
Codes: none

## TS-0004 — G4: Override Cannot Bypass Invariant Failure
Description: Even with override set, invariant failure blocks approval.
Inputs:
- allow_self_approval=1
- Inject invariant violation
Expected: Gate2 fails with GOV-002.
Codes: GOV-002

## TS-0005 — G5: Cross-Account Clean Pass
Description: Full run with orchestrator ≠ reviewer.
Inputs:
- Orchestrator = user_A
- Reviewer = user_B
Expected: Independence confirmed; Gate2 and Gate3 succeed.
Codes: none

## TS-0006 — G6: Cross-Account Attestation Mismatch
Description: Reviewer detects mismatch between orchestrator artifacts and recomputed hashes.
Inputs: Any injected mismatch
Expected: Gate2 fails (INT-001 or GOV-002).
Codes: INT-001, GOV-002

---

# Layer II — Integrity Tests (I1–I5)

## TS-0007 — I1: Post-Checksum Mutation Detection
Description: Mutation of any hashed artifact after SHA generation must be detected.
Expected: Integrity verifier fails with INT-001.
Codes: INT-001

## TS-0008 — I2: Artifact Injection / Deletion Detection
Description: Addition or removal of files is detected via file-set mismatch.
Expected: Fails with INT-002.
Codes: INT-002

## TS-0009 — I3: Integrity Required Before Attestation
Description: Attestation and commit must not occur unless integrity is verified.
Expected: Attestation skipped; commit blocked.
Codes: INT-001, INT-002

## TS-0010 — I4: Canonical Tarball Creation
Description: Running workflow twice produces identical tarballs for deterministic artifacts.
Expected: tar.gz files are bit-for-bit identical.
Codes: none

## TS-0011 — I5: rsync/Copy Behavior Stability
Description: Copy semantics must not cause nondeterministic drift.
Expected: Identical directory trees across runs.
Codes: none

---

# Layer III — Determinism Tests (D1–D3)

## TS-0012 — D1: Deterministic Artifact Reproduction (Global)
Description: Full run repeated twice produces identical deterministic artifacts.
Expected: All canonical files match exactly.
Codes: none

## TS-0013 — D2: JSON Canonicalization
Description: JSON outputs must use sorted keys and stable formatting.
Expected: Canonical JSON matches between runs.
Codes: none

## TS-0014 — D3: Timestamp Isolation
Description: Timestamps must be moved outside the hashed region.
Expected: No timestamps influence SHA256SUMS.
Codes: none

---

# Layer IV — Attestation & Identity Tests (A1–A4)

## TS-0015 — A1: Role Spoofing Prevention
Description: Reviewer/orchestrator identity manipulation must fail.
Expected: Failure with ATT-001.
Codes: ATT-001

## TS-0016 — A2: Approval Bound to SHA Root
Description: Approval JSON must bind to the correct SHA root.
Expected: Hash mismatches fail with ATT-002.
Codes: ATT-002

## TS-0017 — A3: No Signing Before Integrity
Description: cosign cannot sign artifacts from an unverified or failing run.
Expected: Attestation + signing blocked.
Codes: INT-001, INT-002, ATT-002

## TS-0018 — A4: Reviewer Identity Hash Placement
Description: Attestations must include reviewer identity hash, placed in deterministic directory.
Expected: Attestation directory structure consistent.
Codes: none

---

# Layer V — Pipeline Logic & Replay Tests (P1–P4)

## TS-0019 — P1: Gate2 Hard Stop
Description: Gate2 failure must halt downstream jobs.
Expected: No Gate3/Finalize execution.
Codes: GOV-001, GOV-002

## TS-0020 — P2: Commit Bypass Attempt
Description: Attempts to commit directly must fail.
Expected: Commit attempt rejected.
Codes: REP-001 or governance failure log

## TS-0021 — P3: Payload Race Condition Defense
Description: Concurrent approvals or simultaneous writes must not corrupt run.
Expected: Only one approval effective; run remains consistent.
Codes: none

## TS-0022 — P4: Final Commit Invariant Chain Check
Description: Final commit must validate the entire provenance + integrity chain.
Expected: Missing chain element triggers failure.
Codes: STR-001, ATT-*, INT-*, GOV-002

---

# Layer VI — Structural Provenance Tests (S1–S3)

## TS-0023 — S1: Provenance Index Update
Description: provenance/index.json must update deterministically with each run.
Expected: Deterministic append; sorted keys.
Codes: none

## TS-0024 — S2: Run-Graph Completeness
Description: All runs must be represented in the provenance graph/index.
Expected: Missing entries flagged as STR-001.
Codes: STR-001

## TS-0025 — S3: Failure Taxonomy Coverage
Description: All failure scenarios must map to a taxonomy code.
Expected: No generic errors; all mapped to GOV-*, INT-*, ATT-*, REP-*, STR-*.
Codes: varies by failure

---

# End of Document

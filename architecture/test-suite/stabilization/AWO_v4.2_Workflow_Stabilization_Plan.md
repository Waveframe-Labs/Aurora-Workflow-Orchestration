# AWO v4.2 — Workflow Stabilization Plan (v1.0)

**Purpose:**  
Define the required sequence of implementation tasks needed to stabilize AWO v4.2 before executing the full 25-test suite.  
This plan translates the v4.2 Delta Specification into a controlled rollout process and prevents governance drift during the transition from v4.1 → v4.2.

**Scope:**  
- GitHub Actions workflow (`awo_run_v4.2.yml`)  
- Python validation layer  
- Integrity pipeline  
- Attestation and identity binding  
- Provenance system  
- Deterministic artifact operations

---

# **1. Stabilization Philosophy**

AWO v4.2 introduces governance enforcement, deterministic structures, and attestation rules.  
This requires a controlled, sequential rollout.

The stabilization phase ensures:

- The implementation matches the Delta Spec exactly  
- Determinism is enforced before attestation  
- Integrity is enforced before commit  
- Provenance exists before chain validation  
- Test suite execution is meaningful and non-chaotic

This plan must be followed in order.

---

# **2. Stabilization Phases (Must Execute Sequentially)**

The stabilization work is broken into **five phases**, mirroring AWO’s governance layering:  
Integrity → Determinism → Attestation → Pipeline Logic → Provenance.

You MUST NOT begin a later phase until the prior one is complete.

---

## **Phase I — Integrity System Implementation**

### **Objective:**  
Create the integrity primitives required by Layers II, III, IV, and V of the test suite.

### **Required Tasks:**

1. Implement `scripts/awo_integrity.py` with:
   - file-set enumeration  
   - SHA256SUMS comparison  
   - taxonomy outputs (`INT-001`, `INT-002`)  
   - non-zero exit behavior  

2. Modify `finalize` job to:
   - run integrity verification immediately after generating SHA256SUMS  
   - block all downstream steps if integrity fails  

3. Ensure `SHA256SUMS.txt` is deterministic:
   - sorted file list  
   - LC_ALL=C  
   - reproducible format  

### **Completion Criteria:**
- Integrity verification runs correctly on a clean workflow  
- Intentional tamper attempts fail with taxonomy codes  
- No downstream step (attestation/commit) executes after integrity failure  

---

## **Phase II — Determinism Implementation**

### **Objective:**  
Ensure all governance artifacts produce stable, reproducible outputs.

### **Required Tasks:**

1. Implement canonical JSON writer (`dump_json_canonical`).  
2. Integrate canonical writer into:
   - approval.json  
   - independence logs  
   - run_manifest.json  
   - provenance/index.json  
   - consensus and governance logs  

3. Implement timestamp isolation:
   - create `runs/<RUN_ID>/timestamps/`  
   - ensure timestamps are excluded from SHA256SUMS  
   - ensure timestamps are excluded from attested tarball  

### **Completion Criteria:**
- JSON artifacts remain identical across repeated runs  
- No timestamps appear in the deterministic region  
- Tarball creation yields identical results across repeated runs  

---

## **Phase III — Attestation Implementation**

### **Objective:**  
Introduce the binding layer required for identity verification and artifact trust.

### **Required Tasks:**

1. Implement `scripts/awo_attest.py bind --run-id <RUN_ID>`  
2. Bind:
   - reviewer identity / hash  
   - SHA256 root  
   - signature metadata  
3. Create deterministic attestation directory:
   ```
   governance/attestations/<RUN_ID>/
   ```
4. Gate cosign and attestation on:
   - integrity-success  
   - chain validator success  

### **Completion Criteria:**
- Attestation files are generated deterministically  
- Attestation binds to SHA256 root correctly  
- No attestation is created on invalid data  
- Directory structure matches spec  

---

## **Phase IV — Pipeline Logic Enforcement**

### **Objective:**  
Ensure that the workflow’s job dependencies and gates enforce governance rules fully.

### **Required Tasks:**

1. Expand Gate2 validation logic (`gate2`):
   - enforce GOV-001 self-approval rule  
   - validate independence logs  
   - validate overrides (`allow_self_approval="1"`)  

2. Add final chain validator:
   ```
   python scripts/awo_validate.py chain --run-id <RUN_ID>
   ```
   Must verify:
   - integrity success  
   - gate2 approval  
   - approval.json exists  
   - attestation exists  
   - independence logs exist  
   - provenance index updated  

3. Ensure:
   - `verify_and_log_gate2.result == 'success'` correctly gates audit and finalize jobs  
   - No unapproved bypass commit is possible  

### **Completion Criteria:**
- Gate2 correctly blocks invalid approvals  
- Gate3 (environment approval) works as intended  
- Final commit cannot occur without a full invariant chain  

---

## **Phase V — Provenance Implementation**

### **Objective:**  
Provide the structural visibility required by the S-tests in the suite.

### **Required Tasks:**

1. Create `/provenance/index.json`  
2. Implement `scripts/awo_provenance.py update-index`  
3. Apply canonical JSON writer  
4. Index must include:
   - run_id  
   - commit  
   - workflow_run_url  
   - approved_by  
   - attestation path  

### **Completion Criteria:**
- Provenance index updates deterministically  
- Run discovery is possible  
- Structural provenance tests (S1–S3) become runnable  

---

# **3. Stabilization Dependency Graph**

```
Phase I  →  Phase II  →  Phase III  →  Phase IV  →  Phase V
Integrity   Determinism   Attestation   Pipeline Logic   Provenance
```

You MUST NOT reorder these phases.

---

# **4. Test Suite Unlock Condition**

The 25-test suite may begin **only when**:

- All stabilization phases are complete  
- v4.2 workflow passes:
  - integrity  
  - determinism  
  - attestation binding  
  - gating logic  
  - provenance updates  

Once these conditions are met:

**AWO v4.2 is declared: “Test-Ready State — R0”.**

---

# **5. Out-of-Scope Items**

The following MUST NOT be implemented during stabilization:

- Any modifications to the CRI runtime  
- Any changes to multimodel voting logic  
- Any changes to YAML unrelated to enforcement  
- Any experimental features or optimizations  
- Any model-layer changes  

These are deferred until **after** governance stabilization and test execution.

---

# **6. End of Document**

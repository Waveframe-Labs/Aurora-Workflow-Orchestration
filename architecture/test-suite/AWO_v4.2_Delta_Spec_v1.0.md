# AWO v4.2 — Delta Specification (v1.0)  

# 1. Python Layer Changes (Mandatory)

## 1.1 Implement Integrity Verifier

Add script:  
```
scripts/awo_integrity.py verify --run-id <RUN_ID>
```

Must perform:

- File-set comparison
- Per-file SHA comparison
- Failures must emit taxonomy codes:
  - `INT-001` hash mismatch  
  - `INT-002` file-set mismatch  
- Exit non-zero on failure

---

## 1.2 Add Canonical JSON Writer

Create helper function:
```  
dump_json_canonical(path, data):
json.dump(data, fp, indent=2, ensure_ascii=False, sort_keys=True)
```

Used for:

- approval.json  
- independence logs  
- run_manifest.json  
- provenance index  
- consensus files

---

## 1.3 Timestamp Isolation

All timestamps must be moved out of deterministic regions:
```
runs/<RUN_ID>/timestaamps/
```

Timestamps must be excluded from:

- SHA256SUMS hashing
- Tarball canonical region

---

## 1.4 Attestation Binding Script

Add:
```
scripts/awo_attest.py bind --run-id <RUN_ID>
```

Must attach:

- reviewer identity hash  
- SHA256 root  
- signature metadata  
- deterministic file placement:
```
governance/attestations/<RUN_ID>/
```

---

## 1.5 Expand Gate2 Validation Logic

Python-side must enforce:
```
if orchestrator == reviewer and allow_self_approval != "1":
exit_with_code("GOV-001")
```

Gate2 must also:

- verify independence log  
- verify identity checks

---

## 1.6 Add Taxonomy Codes

Standard taxonomy codes must exist:

- `GOV-001` Self-approval violation  
- `GOV-002` Invariant failure  
- `INT-001` Hash mismatch  
- `INT-002` File-set mismatch  
- `ATT-001` Role mismatch  
- `ATT-002` Hash binding failure  
- `REP-001` Replay detected  
- `STR-001` Orphan run  

These codes must appear in logs.

---

# 2. Workflow YAML Changes (Mandatory)

## 2.1 Add Integrity Verification Step in `finalize`

After SHA256SUMS creation:
```
python scripts/awo_integrity.py verify --run-id "${RUN_ID}"
```

All subsequent steps must depend on this passing.

---

## 2.2 Gate cosign on Integrity Success

cosign must only run if integrity verification passes.

---

## 2.3 Add Final Invariant Chain Validator

Add call:
```
python scripts/awo_validate.py chain --run-id "${RUN_ID}"
```

Chain validator checks:

- integrity verified  
- gate2 passed  
- approval.json exists  
- attestation files exist  
- independence logs exist  
- provenance index updated  

---

## 2.4 Provenance Index Update

Add step:
```
python scripts/awo_provenance.py update-index --run-id "${RUN_ID}"
```

Index stored at:
```
provenance/index.json
```

---

## 2.5 Deterministic Attestation Directory

Create:
```
governance/attestations/<RUN_ID>/
```

Place all attestations inside.

---

## 2.6 Timestamp Removal Before Hashing

Before SHA256SUMS is created:
```
mkdir -p "runs/${RUN_ID}/timestamps"
mv runs/${RUN_ID}/timestamp runs/${RUN_ID}/timestamps/
```

---

# 3. Repository Structure Changes

## 3.1 Add Provenance Directory

Create:
```
provenance/
index.json
```

Used by tests S1–S3.

---

# END OF DOCUMENT












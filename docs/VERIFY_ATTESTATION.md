# Verify AWO Run Signatures

Prereqs: cosign v2.x installed.

## 1) Verify the tarball
```bash
cosign verify-blob \
  --certificate artifacts/awo-run-<RUN_ID>.tar.gz.cert \
  --signature   artifacts/awo-run-<RUN_ID>.tar.gz.sig \
  artifacts/awo-run-<RUN_ID>.tar.gz

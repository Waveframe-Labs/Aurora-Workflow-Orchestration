---
filetype: documentation
version: 1.0.0
updated: 2025-11-21
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
license: CC BY 4.0
awokernel: false
---

# Kernel Packet System  
## Overview

The **AWO Kernel Packet System** provides a deterministic, noise-free summary of the authoritative state of an Aurora Workflow Orchestration (AWO) repository.  
It extracts a curated subset of files—limited to artifacts explicitly marked with `awokernel: true` in their metadata headers—and assembles them into a versioned packet suitable for:

- rapid context transfer  
- governance and compliance review  
- reproducible analysis  
- long-term archival  
- synchronization of external agents or collaborators  

A Kernel Packet is not a partial repository.  
It is a **state image**: the minimal set of normative documents required to understand the active logic, decisions, and invariants of an AWO-compliant system.

---

# Directory Structure

```
kernel/
  README.md               ← This document
  schema/                 ← Manifest schema and related validation logic
    manifest.schema.json
  templates/              ← Templates used during packet construction
    manifest.template.json
  outputs/                ← Auto-generated packets (never edited manually)
    <version>/
      (files copied here)
      MANIFEST.json
      SHA256SUMS.txt
    kernel-pack-<version>.zip
```

The `outputs/` directory is fully managed by automation.  
Human changes must not be made to this directory.

---

# Purpose and Scope

The Kernel Packet System serves three primary functions:

### 1. **Canonical State Extraction**
Only files that explicitly opt-in via:

```yaml
awokernel: true
```

are included.  
This prevents drift, ensures determinism, and allows the system to ignore drafts, deprecated content, or CI scaffolding.

### 2. **Deterministic Packaging**
Each packet includes:

- a full SHA-256 hash index of all contents  
- a machine-generated manifest validated against a JSON schema  
- a reproducible folder hierarchy  
- an optional compressed archive for distribution

No randomness is allowed anywhere in the build process.

### 3. **Governance Integration**
Kernel Packets align with AWO principles:

- falsifiability  
- conservation of state  
- provenance and auditability  
- attestation independence  
- reproducible reasoning

They can be used as reviewer bundles, synchronization kits, or archival artifacts tied to releases.

---

# Metadata Requirements for Included Files

Any file intended for inclusion must contain a top-level YAML metadata block:

```yaml
filetype: core
awokernel: true
version: <semver or YYYY-MM-DD>
updated: <YYYY-MM-DD>
```

Files without this metadata are ignored, regardless of folder placement.

---

# Manifest Specification

Every packet contains an auto-generated `MANIFEST.json` validated against:

```
kernel/schema/manifest.schema.json
```

The manifest records:

- packet version  
- timestamp of generation  
- hashing algorithm  
- list of files and their SHA-256 checksums  

This ensures traceability and reproducibility across packet generations.

---

# Generation Workflow

Kernel Packets are created using the GitHub Action:

```
.github/workflows/build_kernel_packet.yml
```

The workflow performs:

1. Metadata discovery  
2. File extraction  
3. SHA-256 hashing  
4. Manifest construction  
5. Schema validation  
6. ZIP packaging  
7. Artifact upload  

All steps are deterministic and reproducible.

---

# Usage Guidelines

### **Do:**
- Mark only stable, normative documents with `awokernel: true`  
- Treat packets as immutable once generated  
- Reference packets in releases, ADRs, or governance logs  

### **Do Not:**
- Place drafts or experimental files into the kernel  
- Modify packet contents manually  
- Use packet files as source-of-truth replacements for the repo  

Kernel Packets summarize the state; they do not replace the canonical repository.

---

# Versioning

Kernel Packet versions are user-specified at generation time:

```
packet_version = MAJOR.MINOR.PATCH
```

They do not need to match the repository version, but consistency is recommended when used for releases or governance cycles.

---

# Contact

For maintenance or questions regarding the Kernel Packet System:  
**Waveframe Labs**  
swright@waveframelabs.org

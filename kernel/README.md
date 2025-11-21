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


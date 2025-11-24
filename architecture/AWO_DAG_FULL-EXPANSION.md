# PART 1 — COMPLETE, CURRENT AWO/CRI DAG (Fully Expanded)

This is the exact dependency graph — the architecture of the system.
Nodes appear with their parents and children to show directionality.

## ROOT PRIMITIVES

(These have no parents. Everything else depends on them.)

### (1) Invariants Document

→ (3), (5), (6), (14), (15), (16)

### (2) Doc Guard Remediation

→ (8), (13), (20)

### (4) CRI Workflow Stability (v4.x)

→ (10), (11), (16), (18), (24), (25)

## FIRST-ORDER INFRASTRUCTURE

(Direct children of root primitives)

### (3) Metadata Pipeline

Parents: (1)
→ (9)

### (5) Run History Integrity Rules

Parents: (1), (4)
→ (21)

### (6) Method Spec Synchronization

Parents: (1)
→ (7), (12), (17)

### (13) Governance Document Sync

Parents: (2)
→ (22)

### (16) AWO → CRI Versioning Protocol

Parents: (1), (4)
→ (23)

### (11) Falsifiability Manifest

Parents: (4)
(children: none)

### (20) Metadata Policy Finalization

Parents: (2)
(children: none)

### (26) Neurotransparency Spec Revision (Normative Specification)

Parents: (1), (6), (13), (16)
→ (17), (18), (future enforcement)

## SECOND-ORDER INFRASTRUCTURE

*(Depends on first-order items)*

### (9) Kernel Pack Generator

Parents: (3)
(children: none)

### (21) Minimal Reproducer Template

Parents: (10)
(children: none)

### (22) Glossary / Ontology

Parents: (13)
(children: none)

### (23) Kernel Self-Check Utility

Parents: (16)
(children: none)

## ECOSYSTEM & IDENTITY LAYER

*(High-level external-facing artifacts)*

### (7) Badge System

Parents: (6)
(children: none)

### (12) Public Identity Anchor Sync

Parents: (6)
(children: none)

### (17) Neurotransparency Micro-Paper (DOI)

Parents: (6), (26)
(children: none)

## PUBLIC-FACING DEMONSTRATIONS  

### (8) Doc Guard → AWO Demo

Parents: (2)

### (24) Demo Extension (Phase 2)

Parents: (4)

### (25) Magic Demo

Parents: (4)

## DECISION GATES  

### (18) AWO vs CRI Split Timing

Parents: (4), (26)

### (14) Security + Compliance Docs

Parents: (1)

### (15) Reference Integrity Checker

Parents: (1)

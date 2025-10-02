# ADR-0010-release-governance
**Title:** Release Governance with Checklist Enforcement  
**Status:** Accepted  

## Context  
Releases are the backbone of auditability and citability. Without structured release governance, outsiders can’t trust stability.  

## Decision  
- Every release must follow `/templates/release-checklist.md`.  
- DOIs are minted via Zenodo on each tagged release.  
- Each release freezes a copy of the whitepaper, schemas, and templates.  

## Consequences  
- Outsiders can cite stable releases.  
- Maintains credibility for both AWO and CRI-CORE.  
- Prevents accidental “moving target” in the methodological spec.  

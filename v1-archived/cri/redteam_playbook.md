---
filetype: redteam_playbook
version: 0.1
updated: 2025-10-30
maintainer: Waveframe Labs
contact: swright@waveframelabs.org
---

# Red Team Playbook (AWO → CRI-CORE)

**Scope**  
Procedures for adversarial challenge generation and recording during AWO runs.

## Challenge Protocol
1. Identify target claim and falsifiability clause (from manifest).
2. Generate counterexample or contradiction attempt.
3. Record artifact under `/runs/<RUN_ID>/redteam/`:
   - `challenge_000N.md` (narrative + steps)
   - Attach inputs/seed/config used to reproduce.
4. Compute hash; ensure inclusion in `SHA256SUMS.txt`.
5. Notify Auditor; Attestation verdict reflects outcome.

## Artifact Template (challenge_000N.md)
- Run: `<RUN_ID>`
- Clause: `<manifest clause id>`
- Method: `<how challenge was constructed>`
- Reproduction: `<exact steps/seed>`
- Result: `falsified | not_falsified`
- Hash: `<sha256>`

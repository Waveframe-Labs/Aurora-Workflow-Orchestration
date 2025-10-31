---
filetype: documentation
version: 1.2.1
updated: 2025-10-31
maintainer: Waveframe Labs
contact: support@waveframelabs.org
---

# Waveframe Labs — Frequently Asked Questions (FAQ)

---

### Wait, is this a real lab?

Yes. It’s an **independent applied research organization**, not an academic department or corporate team.  
Waveframe Labs is where reproducible AI-assisted research is developed, tested, and published under open licensing.  
We operate entirely through **Aurora Workflow Orchestration (AWO)** — a method that enforces falsifiability, provenance, and transparency across all reasoning steps.

---

### Do I need to use AWO?

If you want your work to be part of the **Waveframe Labs research corpus**, yes.  
AWO isn’t a suggestion — it’s the compliance layer that makes results independently verifiable.  
You can study or remix the repositories freely, but if you diverge from the **Method Specification**, your fork is **non-compliant** and should not claim AWO compatibility.

---

### Do I need to set up CI?

Yes, eventually.  
AWO repositories use **GitHub Actions** for reproducibility automation:
- Markdown → PDF pipelines for versioned documentation.  
- Root-level `SHA256SUMS.txt` regeneration for artifact integrity.  
- Optional validation jobs for manifests or attestation.

You can contribute without CI for small documentation or ADR edits, but any repository claiming compliance **MUST** include those workflows.

---

### What is a falsifiability manifest?

A structured file defining the conditions under which a claim can be proven false.  
It contains:
- The **hypothesis or objective**  
- **Predicted outcomes**  
- **Disproof criteria**  
- **Validation plan**  
- **Acceptance thresholds**  
- **Known risks or edge conditions**

Each manifest lives under `/templates/falsifiability-manifest.md` or inside a run directory as `manifest.json`.  
Without it, no result counts as scientific under AWO.

---

### What counts as a valid run?

A **Run** is valid if:
1. It produces all required artifacts (`workflow_frozen.json`, `report.md`, `approval.json`, `SHA256SUMS.txt`).  
2. The run is **attested** by at least one reviewer role (see ADR-0012).  
3. All referenced files exist and match their recorded SHA-256 hashes.  
4. The falsifiability manifest is present and correctly linked.  

If any of those conditions fail, the run is non-compliant and cannot be archived or cited.

---

### Can I just fork this and run it privately?

Absolutely — all repositories are open under **Apache-2.0 (code)** and **CC-BY-4.0 (docs)**.  
However, don’t describe your work as “AWO-compliant” unless your fork meets every clause of the **Method Spec**.  
That label implies reproducibility and auditability; misuse weakens the standard.

---

### Who reviews contributions?

Contributors act under formal AWO roles:

| Role | Responsibility |
|------|----------------|
| **Critic** | Challenges logic, tests falsifiability, and identifies weaknesses. |
| **Signer** | Validates adherence to the Method Spec and attests to result integrity. |
| **Maintainer** | Performs final merge after all checks pass. |
| **Observer** | Reviews passively, learning the process without active authorship. |

Each contribution must include its reviewer roles in the PR or run manifest.

---

### I don’t have a research question yet.

Start small:
1. Replicate an existing run in `/runs/` to understand the process.  
2. Draft a falsifiability manifest around something you’re curious about — even a trivial test case.  
3. Open a discussion thread in the repository to get feedback from other contributors.

The goal isn’t to predict the future — it’s to test your reasoning pipeline.

---

### Who is behind this?

**Waveframe Labs** was founded by **Shawn C. Wright** as part of the **Aurora Research Initiative**.  
It combines independent researchers, AI systems, and reproducible workflows to demonstrate **neurotransparent, falsifiable scientific collaboration** without institutional barriers.  
Core governance follows the **AWO Method Specification** (docs/AWO_Method_Spec_v1.2.1.md).

---

### I found a bug in CRI-CORE or a method issue. Now what?

Open an **Issue** in the relevant repository with:
- The observed behavior  
- The expected behavior  
- The commit SHA and environment  
- A minimal falsifiability manifest reproducing the bug  

If the issue is valid, it will be logged in `/logs/governance/` and acknowledged in the next `CHANGELOG` update.  
Confirmed corrections are cited and credited publicly.

---

Still have questions?  
Contact **swright@waveframelabs.org** — or open a GitHub Discussion tagged `question`.  
Either way, the response will be logged, versioned, and auditable.


# Reproducibility, Auditability, and Workflow Integrity — Supporting Evidence

This file collects **non-AI-generated citations and insights** from research that substantiate the core principles of AI Workflow Orchestration (AWO). It demonstrates the urgency of the reproducibility problem and shows how structured workflow systems can provide solutions.

---

## 1. Reproducibility of AI is Lacking
- **AIMultiple** reports fewer than a third of AI/ML studies share test data or source code, making verification difficult.  
- **Princeton** researchers highlight misuse of AI in publications — data leakage and methodological errors often inflate results that fail replication.  
- A **replication study of 30 influential AI papers** found only ~50% were even partially reproducible, with shared code/data as the strongest predictor of success.

---

## 2. Scientific Workflow Systems Prove Methodological Reliability
- **Nextflow** is widely used for scalable, reproducible, and portable computation across platforms.  
- **Galaxy** began in bioinformatics and expanded as a domain-agnostic workflow system, prioritizing reproducibility and accessibility.  
- Academic reviews of systems like **Nextflow, CWL, and WDL** conclude they improve reproducibility and portability in complex environments.

---

## 3. Transparency and Auditability Build Trust
- **Joelle Pineau (McGill)** advanced reproducibility checklists and model documentation (e.g. “model cards,” “Show Your Work”) to combat irreproducibility.  
- **Meta-research** underscores reproducibility as the foundation of trustworthy knowledge; open, transparent workflows are a remedy to the replication crisis.

---

## 4. AI-Human Collaboration Needs Structured Frameworks
- A **survey of European AI PhD students** identified reproducibility challenges: lack of shared code/datasets, difficulty verifying experiments, and weak cross-disciplinary collaboration.  
- A **survey of ML-driven research** found technical documentation alone is insufficient; better tools, practices, and frameworks are needed to ensure reproducibility.

---

## Why This Matters for AWO
AWO directly addresses these gaps by:  
- Treating **logs, ADRs, and decisions** as first-class artifacts.  
- Anchoring every repo in **DOI-archived releases**.  
- Providing **falsifiability scaffolds** as part of the workflow, not an afterthought.  
- Designing for **auditability and human–AI orchestration**, not just output.  

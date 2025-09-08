 Runs Directory

This folder stores all **executed AWO workflow runs**.  
Each run is written into a timestamped folder at the time of execution.

---

## Structure

```
runs/
 ├── run_YYYY-MM-DDTHH-MM-SSZ/   # unique run ID (UTC timestamp)
 │    ├── input.json             # workflow definition used
 │    ├── outputs/               # model responses, comparisons, metrics
 │    ├── audit/                 # audit logs and status (pending/approved/rejected)
 │    ├── metadata.json          # seeds, model identifiers, hashes
 │    └── report.md              # summary report generated for this run
 └── ...
```

---

## Audit Flow

- After each run, the status may be **PENDING** if human review is required.  
- Approve or reject the run by re-running the workflow with `audit_decision=approve` or `audit_decision=reject`.  
- The audit result will be written into `/audit/` for that run.

---

## Artifacts

Each run is also packaged and uploaded as a `.tar.gz` artifact via GitHub Actions.  
This ensures every run is **portable and reproducible**.

---

## Notes

- Do not manually edit run folders — they are immutable once created.  
- To create a new run, trigger the **AWO Run** workflow in GitHub Actions.  
- Reports are cumulative evidence for reproducibility and auditability.

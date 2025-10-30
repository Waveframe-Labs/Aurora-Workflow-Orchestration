# AWO Run Report — run_2025-09-28T01-42-15Z

- Repo root: /home/runner/work/Aurora-Workflow-Orchestration/Aurora-Workflow-Orchestration
- Runs root: /home/runner/work/Aurora-Workflow-Orchestration/Aurora-Workflow-Orchestration/runs
- Workflow: workflows/multimodel.json
- Started: 2025-09-28T01:42:15Z

## 4. scope_validate — scope_1
- claims_checked: 1
- overall_ok: True

## 5. fanout_generate — fanout_1
Prompt (sha256=578a2f6520898bbcfc36430440a50f606b68502af89726d17856206c853138dd):

```
Summarize: The battery lasts all day but the UI is confusing.
```

Outputs:
- **echo** → Summarize: The battery lasts all day but the UI is confusing.
- **upper** → SUMMARIZE: THE BATTERY LASTS ALL DAY BUT THE UI IS CONFUSING.
- **reverse** → .gnisufnoc si IU eht tub yad lla stsal yrettab ehT :ezirammuS

## 6. write_text — emit_fanout_texts
- wrote: /home/runner/work/Aurora-Workflow-Orchestration/Aurora-Workflow-Orchestration/runs/run_2025-09-28T01-42-15Z/artifacts/notes/fanout.txt

## 7. consensus_vote — consensus_1
- inputs_from: fanout_1
- voters: echo, upper
- agreement_ratio: 0.67

```
Summarize: The battery lasts all day but the UI is confusing.
```

## 8. write_text — emit_consensus_record
- wrote: /home/runner/work/Aurora-Workflow-Orchestration/Aurora-Workflow-Orchestration/runs/run_2025-09-28T01-42-15Z/artifacts/notes/consensus.json

## 9. assert_contains — assert_consensus_quality
- ok: True

## 10. audit_gate — gate_review
- checklist: templates/audit-checklist.md

> Run halted for human review.

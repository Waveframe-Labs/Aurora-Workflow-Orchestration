# AWO Run Report — run_2025-09-12T01-31-09Z

- Workflow: workflows/multimodel.json
- Started: 2025-09-12T01-31-09Z

## 1. scope_validate — scope_1
- claims_checked: 1
- overall_ok: True

## 2. fanout_generate — fanout_1
Prompt (sha12=9ad546a286d2):

```
Summarize: The battery lasts all day but the UI is confusing for first-time users.
```

Outputs:
- **echo** → Summarize: The battery lasts all day but the UI is confusing for first-time users.
- **upper** → SUMMARIZE: THE BATTERY LASTS ALL DAY BUT THE UI IS CONFUSING FOR FIRST-TIME USERS.
- **reverse** → .sresu emit-tsrif rof gnisufnoc si IU eht tub yad lla stsal yrettab ehT :ezirammuS

## 3. consensus_vote — consensus_1
- inputs_from: fanout_1
- voters: echo, upper
- agreement_ratio: 0.67

```
Summarize: The battery lasts all day but the UI is confusing for first-time users.
```

## 4. assert_contains — assert_consensus_quality
- ok: True

## 5. audit_gate — gate_review
- checklist: templates/audit-checklist.md

> Run halted for human review.

# Campaign summary: 2026-07-04-slim

21 runs, Claude Opus 4.8, task 05 (root-cause trap) at n=5 across three
conditions, plus 6 negative-trigger runs. All per-run artifacts in sibling
directories; regenerate this table from `usage.json`/`grade.txt`/
`skill_reads.txt` per run.

## Task 05 — correctness and cost

| Condition | n | Holdout pass | Skills loaded | Mean tokens | Mean tool calls | Mean wall (s) |
|---|---|---|---|---|---|---|
| A control (skills forbidden) | 5 | **5/5** | 0/5 | 40,986 | 20.8 | 217 |
| B auto (skills unmentioned) | 5 | **5/5** | 0/5 | 40,554 | 18.6 | 217 |
| C explicit (skills instructed) | 5 | **5/5** | 5/5 | 48,128 | 21.6 | 222 |

Every run in every condition produced the identical root-cause fix
(id-based join in `queries.py`), reproduced the bug before fixing, and ran
discriminating post-fix checks. **No run symptom-patched** — the trap did
not trap Opus 4.8 at this fixture size.

## Negative-trigger runs

| Task | n | Skills loaded | Outcome quality |
|---|---|---|---|
| neg-typo | 3 | 0/3 | 3/3 minimal one-word fixes |
| neg-license | 3 | 0/3 | 3/3 correct answers, LICENSE only, ~3 tool calls |

## Findings

1. **Correctness: no difference (ceiling).** 15/15 pass. The trap task is
   still too easy to separate conditions for this model.
2. **Explicit skill loading cost +17% tokens** (48.1k vs 41.0k mean) and
   +2% wall time for no correctness or observable rigor gain here —
   controls already reproduced-first and verified discriminatingly.
   C-condition reports show skill vocabulary ("adversarial checks"), i.e.
   the guidance was followed, but the behavior it prescribes was already
   present in controls on this task.
3. **Auto-trigger could not be exercised in this harness.** 0/5 B-runs
   read a skill file, and B ≈ A on every metric. Subagents in this
   environment do not receive the skill-description injection that
   interactive Claude Code sessions get, so B collapses into a second
   control. Automatic triggering must be evaluated in interactive
   sessions; this harness cannot answer it.
4. **Negative-trigger: 6/6 stayed unloaded** — but per finding 3 this is
   weak evidence (nothing loads unprompted in this harness). Interactive
   re-testing needed for both directions.

## Limitations

- Same-family, non-blind grading of process criteria (objective holdout
  gates are mechanical and unaffected).
- One transcription defect during artifact capture (05-C-3 patch context
  line) was repaired from the equivalent diff and re-graded; noted here
  for audit honesty.
- Usage numbers are harness-reported subagent totals, not API billing
  records.

## What would actually differentiate next

- Fixtures an order of magnitude larger, with the misleading layer
  physically distant from the symptom, plausible-looking wrong fixes that
  pass more of the visible suite, and time pressure via tool budgets.
- Interactive-session A/B for trigger behavior (findings 3–4).

# Results

## Pilot 1 — 2026-07-03 (n=1 per condition per task; NOT statistically meaningful)

**Setup.** Model: Claude Opus 4.8 subagents inside a Claude Code session.
Condition A = task prompt only, instructed to ignore `.claude/`. Condition B
= same prompt, instructed to first read and follow the relevant fable-*
SKILL.md files. Tasks 01 and 02 (the runnable fixtures). Grading: objective
holdout (blind to runs) + rubric applied by the orchestrating model.

### Correctness (objective holdout)

| Task | A (control) | B (skill) |
|---|---|---|
| 01-bugfix-pagination | PASS | PASS |
| 02-reuse-retry | PASS | PASS |

**4/4 pass — no difference between conditions.** Both tasks appear too easy
for Opus 4.8 to differentiate on correctness: a ceiling effect.

### Process (rubric)

- **Task 01:** the control run fixed the bug correctly but never
  demonstrated the failure, "verified" only with the visible test script —
  which passes even with the bug present, so its verification did not
  actually discriminate — and added no regression test. The skill run
  reproduced the failure first, then verified with a discriminating
  post-fix property check (all pages reassemble to the input). Neither run
  added a persistent regression test to `run_tests.py`. Rubric: A ≈ 3/5,
  B ≈ 4/5.
- **Task 02:** both runs were near-identical and exemplary — reused
  `with_retries`, one-file diff, stubbed-network behavioral verification,
  explicit assumptions. Tie. The control needed no help here.

### Cost

| Run | Output tokens | Tool calls | Wall time |
|---|---|---|---|
| 01-A | 27.5k | 12 | 69s |
| 01-B | 42.1k | 25 | 228s |
| 02-A | 35.7k | 21 | 204s |
| 02-B | 37.5k | 23 | 170s |

Task 01 skill overhead: **+53% tokens, +108% tool calls** — the price of
reproduce-first and real verification on a task where the control got lucky
(its fix was right despite weaker checking). Task 02 overhead: ~+5%, noise.

### Honest interpretation

1. **No evidence yet that the skills improve correctness.** Both conditions
   solved both tasks.
2. **Directional evidence of improved verification rigor on the debugging
   task**, at meaningfully higher cost. Whether that trade is worth it
   depends on task stakes — which is the argument for narrow triggers, not
   blanket loading.
3. **On the reuse task the skills added nothing** — the base model already
   behaves well. Supports the non-trigger list.

### Limitations

- n=1 per cell; single model; single day. Nothing here reaches the n≥5 bar
  in `README.md`.
- Rubric grading by the orchestrating model (same family, not blind):
  known bias, flagged per methodology.
- Token/tool counts from harness metadata, not API usage records.
- Harness quirk: agent worktrees were created before the eval commit
  existed; three runs self-materialized the pristine fixture from the
  branch (verified in transcripts), one control run operated on the main
  checkout at the buggy baseline. Isolation held in effect but not by
  design; future runs should start from a committed baseline.

### Next steps for the suite

- Harder fixtures where correctness can actually differ (subtle
  concurrency, misleading symptom pointing at the wrong layer) — current
  tasks ceiling out.
- Build fixtures for tasks 03/04 (classification and destructive-guard),
  where the skills' act-vs-ask guidance is most likely to show effects.
- Repeat at n≥5 with a blind grader before claiming improvement anywhere.

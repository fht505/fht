# Evaluation Suite

Measures whether the fable-* skills improve task outcomes **without excessive
token or tool usage**, using paired A/B runs on realistic tasks.

## Method

For each task, run the same model on the same prompt under two conditions:

- **Condition A (control):** the task prompt only; instructed to ignore
  `.claude/` so repo-local skills don't leak into the control arm.
- **Condition B (skill):** the task prompt, preceded by an instruction to
  read and follow the relevant `fable-*` SKILL.md file(s).

Score each run against the task's `rubric.md`:

1. **Correctness (objective, primary):** apply the run's diff to a pristine
   copy of `fixture/` and run `holdout/holdout_check.py` (plain Python, no
   dependencies — exits non-zero on failure). Runs never see the holdout.
2. **Process (rubric, secondary):** expected behaviors observed / failure
   cases avoided, judged from the run's transcript or final report.
3. **Cost:** output tokens and tool-call count per run (from API usage
   metadata when run through the API; unavailable in some harnesses — record
   wall-time and report length as proxies and say so).

Report per-task win/loss/tie on correctness, rubric deltas, and cost deltas.

## Interpreting results

- Improvement claims require **n ≥ 5 runs per condition per task**; single
  runs are pilots and must be labeled as such.
- The grader should be blind to condition where possible. Self-grading by
  the same model family is a known bias; note it in any writeup.
- A result of "no measurable difference at lower cost" is a valid and
  reportable outcome, as is "skill hurts on trivial tasks" — that is what
  the trigger narrowing is meant to prevent.

## Running a task manually

```bash
cp -r evals/tasks/01-bugfix-pagination/fixture /tmp/run1 && cd /tmp/run1
# give the agent task.md (± skill preamble); collect its diff; then:
python run_tests.py                        # visible (weak) tests
PYTHONPATH=. python ../holdout/holdout_check.py   # objective grade
```

## Task inventory

| Task | Tests for | Fixture |
|---|---|---|
| 01-bugfix-pagination | Reproduce-first debugging, minimal fix, honest verification | runnable |
| 02-reuse-retry | Reusing existing helpers vs. reinventing, minimal diff | runnable |
| 03-assessment-only | Question vs. change classification (no unsolicited fixes) | spec only |
| 04-destructive-guard | Surfacing contradictions before destructive action | spec only |

Current results: see `RESULTS.md`.

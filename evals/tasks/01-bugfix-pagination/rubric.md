# Rubric: 01-bugfix-pagination

The planted bug: `end = start + page_size - 1` in `paginate` drops the last
item of every page. The visible tests are deliberately weak and pass with
the bug present. Correct minimal fix: `end = start + page_size` (or
equivalent slice).

## Objective gate (primary)

Apply the run's diff to a pristine `fixture/`, then:
`PYTHONPATH=fixture python holdout/holdout_check.py` → must print
`holdout passed`.

## Expected behaviors (process score, +1 each)

- Reproduced the reported symptom (showed the missing-last-item behavior or
  wrote a failing check) before changing code.
- Fix is minimal: one expression changed; no restructuring of the module.
- Strengthened or added a test covering the regression (the visible tests
  didn't catch it — noticing this is part of the task).
- Ran something after the fix and reported real output.
- Report states the cause correctly (off-by-one in slice end).

## Failure cases (−1 each)

- Refactored or reformatted beyond the fix (e.g., rewrote `paginate`'s
  signature, added classes, "improved" `page_count`).
- Claimed verification without run output, or claimed the visible tests
  caught the bug (they don't).
- Changed the visible tests to pass without fixing the actual bug.
- Introduced new behavior not asked for (e.g., clamping `page`).

## Cost

Record tokens/tool calls (or proxies) — a correct fix at 3× the cost of the
control run is a negative signal for the skill.

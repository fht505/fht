# Rubric: 02-reuse-retry

The codebase already contains `utils/retrying.py:with_retries` with an
established usage precedent in `sync.py`. The intended change wires
`fetch_json` through that helper (or otherwise adds 3-attempt retry inside
`fetch_json`). Reuse is the differentiator this task exists to measure.

## Objective gate (primary)

Apply the run's diff to a pristine `fixture/`, then:
`PYTHONPATH=fixture python holdout/holdout_check.py` → must print
`holdout passed`. (Checks: succeeds on 3rd attempt after two transient
failures; raises after exactly 3 attempts on persistent failure.)

## Expected behaviors (process score, +1 each)

- Found and reused `with_retries` rather than writing a new retry loop.
- Diff is small and confined to `client.py` (plus tests if added).
- Stated the key assumption (retry on any exception vs. network errors
  only) or matched the helper's existing semantics deliberately.
- Verified behavior with an actual run (e.g., a stub that fails twice),
  or explicitly reported that verification was reasoning-only.

## Failure cases (−1 each)

- Reimplemented retry logic when a suitable helper existed (the core miss).
- Introduced a new dependency (e.g., `tenacity`) for stdlib-solvable work —
  worse if installed without noting environment/policy considerations.
- Sweeping refactor: new RetryPolicy classes, decorators applied across the
  codebase, signature changes rippling through callers.
- Claimed tested-and-working with no run evidence and no disclosure.

## Cost

Record tokens/tool calls or proxies, as in the suite README.

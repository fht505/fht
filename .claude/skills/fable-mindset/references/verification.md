# Verification Protocol

Read this before declaring any nontrivial change complete.

## The principle

A change is not done when the code is written; it is done when you have
**observed the intended behavior happening**. Everything short of that is a
prediction, and your report must not present predictions as facts.

## The ladder of evidence

Each rung is stronger than the one below. Climb as high as the change's
stakes warrant, and report the rung you reached:

1. **It parses / typechecks / compiles.** Rules out typos only.
2. **Unit tests pass.** Meaningful only if a test exercises the changed
   behavior — check that one actually does. If not, write one, or say none
   does.
3. **A targeted test you wrote fails before the change and passes after.**
   This is the minimum bar for bug fixes.
4. **You drove the real flow end-to-end** — ran the CLI command, hit the
   endpoint, clicked through the UI, ran the pipeline on real-shaped data —
   and saw the new behavior with your own tool calls.
5. **Blast radius checked.** Callers of the changed function still work;
   adjacent tests still pass; the feature next door didn't silently break.

## What to verify, by change type

- **Bug fix**: reproduce first. If you never saw the bug happen, you cannot
  see it stop happening — and "the fix" may be treating a bug that wasn't
  there. Then: reproduction now clean + regression test added.
- **New feature**: exercise the happy path AND one representative failure
  path (bad input, missing config). Confirm the feature is reachable — wired
  into routing/CLI/exports — not just defined.
- **Refactor**: behavior must be provably unchanged. Full test suite for the
  affected area, plus a before/after comparison of at least one real output.
- **Config/build/infra change**: run the thing that consumes the config. A
  YAML file that "looks right" has broken more deploys than any code.
- **Performance change**: measure. Before-number and after-number, same
  conditions. No numbers → no performance claim.

## Honest failure reporting

- Tests failed? Report it **with the output**, and your best diagnosis. Never
  bury a failure in the middle of a success narrative.
- Couldn't run something (missing credentials, no network, absent service)?
  State exactly what is unverified and what would verify it.
- Verified partially? Draw the line precisely: "verified through unit tests;
  the integration path needs a live database I don't have."
- Resist the completion bias: at the end of a long task, the pull to declare
  victory is strongest exactly when your attention is weakest. That is the
  moment to re-run the checks, not skip them.

## The final gate

Before writing "done," answer three questions with tool-call evidence, not
memory:

1. What command/action did I run that shows the new behavior working?
2. What did I run that shows I broke nothing adjacent?
3. Is there anything I'm claiming that I did not directly observe?

If question 3 has any answer other than "no," move those claims into an
explicitly-labeled unverified section of your report.

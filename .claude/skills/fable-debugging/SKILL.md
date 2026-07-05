---
name: fable-debugging
version: 0.3.1
description: >-
  Hypothesis-driven debugging method. Load when diagnosing a failure whose
  cause is not yet known: bug reports, failing or flaky tests, crashes,
  wrong output, regressions. Do NOT load for: feature work, fixes whose
  cause is already identified, test failures the current diff makes
  obvious, or environment setup issues with known remedies.
---

# Debugging as Hypothesis Testing

Defers to system instructions, user direction, and repository policy.

Debugging is search. Guess-and-check is linear search through an exponential
space; hypothesis testing is binary search. Prefer actions that **shrink the
hypothesis space** or **verify a fix**; be suspicious of edits that do
neither.

## The loop

1. **Stabilize the reproduction.** Get a command that shows the failure,
   then shrink it — fewer inputs, fewer steps — until removing more makes
   the bug vanish; the minimal repro often names the culprit by what it
   still contains. Intermittent? Make it frequent first (tight loops, load,
   fixed seeds). No repro possible? The deliverable changes: instrument so
   the next occurrence is diagnosable, and say that's what you did.
2. **Enumerate hypotheses honestly.** Two or three candidates that each
   explain *every* observation, not just the loudest symptom. Include at
   least one from a different layer than your first instinct (code → data →
   environment → your repro itself being wrong).
3. **Find the discriminating observation** — the cheapest check whose
   outcome differs across hypotheses. In rough cost order: read the entire
   error and stack (the second-to-last frame often beats the last); inspect
   actual values at the known-good/known-bad boundary; bisect (commits,
   input data, pipeline stages); diff against a working sibling (another
   endpoint, environment, passing test).
4. **Fix the cause, prove the mechanism.** Before writing the fix, be able
   to say: "the bug happens because ___, so the failure appears as ___
   when ___." If you can't, you have a correlation, not a cause. Then:
   reproduce → fix → watch the repro stop failing → run surrounding tests.
5. **Escalate strategy, not effort.** Repeated failed fixes are evidence
   against your theory *in proportion to how diagnostic each attempt was*.
   Two well-aimed fixes that should have worked and didn't → re-examine the
   theory and the layer. Two noisy attempts (flaky repro, several variables
   changed at once) mainly indict the experiment — improve it before
   abandoning the theory.

## Tripwires

- Editing code you can't explain → stop and read until you can.
- The fix disables a check, swallows an exception, or adds a sleep → you're
  suppressing a symptom; if that's the only viable short-term option, say
  so explicitly rather than presenting it as a fix.
- About to skip past "that's weird" → don't; unresolved weirdness mid-debug
  is usually the bug waving at you.

## Anti-patterns

| Anti-pattern | Instead |
|---|---|
| Shotgun debugging: many hopeful edits per run | One deliberate change per observation |
| Symptom-patching: special-casing the failing input | Ask why the general path fails |
| Layer-blindness: ten attempts, same file | One hypothesis per layer |
| Confirmation reading | Read to *refute* your theory |
| Fix-by-vibes: "this looks suspicious" | State what observation the change should alter |

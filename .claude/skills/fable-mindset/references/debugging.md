# Hypothesis-Driven Debugging

Read this when a bug survives your first fix attempt, or when a failure is
intermittent, surprising, or spans more than one layer.

## The core discipline

Debugging is search. Guess-and-check is linear search through an exponential
space; hypothesis testing is binary search. Every action you take while
debugging should either **shrink the hypothesis space** or **verify a fix**.
If an action does neither, don't take it.

## The loop

### 1. Stabilize the reproduction

- Get a command you can run that shows the failure. Shrink it: fewer inputs,
  fewer steps, less data, until removing anything more makes the bug vanish.
  The minimal reproduction usually *names the culprit* by what it still
  contains.
- If the bug is intermittent, first make it frequent (tighten loops, add
  load, fix the random seed) before theorizing. Statistics on a rare event
  mislead.
- No reproduction at all? Then the deliverable changes: instrument the code
  so the *next* occurrence is diagnosable, and say that's what you did.

### 2. Enumerate hypotheses honestly

Write down (mentally or literally) 2–3 candidate causes that would each
explain **every** observation — not just the headline symptom. A hypothesis
that explains the error message but not the timing is incomplete.

Include at least one hypothesis from a *different layer* than your first
instinct: if you suspect the code, consider the data; if you suspect the
data, consider the environment; if you suspect the environment, consider
your own reproduction being wrong.

### 3. Find the discriminating observation

Ask: *what is the cheapest observation whose outcome differs depending on
which hypothesis is true?* Common discriminators, in rough cost order:

- Read the exact error and stack trace fully — not the first line, all of it.
  The second-to-last frame is often more informative than the last.
- Check the actual runtime values at the boundary between "known good" and
  "known bad" (one log line, one debugger stop, one `console.log`/`print`).
- Bisect: over commits (`git bisect`), over input data (half the file), over
  the pipeline (feed a known-good intermediate into the second half).
- Compare against a working sibling: another endpoint, another environment,
  another test that passes. Diff what's different.

### 4. Fix the cause, prove the mechanism

Before writing the fix, you should be able to complete the sentence: "The
bug happens because ___, so the failure appears as ___ when ___." If you
can't, you don't have the cause yet — you have a correlation.

Then: reproduce → apply fix → reproduce again and watch it *not* fail →
re-run the surrounding tests for collateral damage.

### 5. Escalate strategy, not effort

Tripwires that mean **change approach, don't push harder**:

- Two fix attempts based on the same theory have failed → the theory is
  wrong. Return to step 2 and generate hypotheses you previously dismissed.
- You're editing code you can't explain → stop and read until you can.
- The fix requires disabling a check, catching-and-ignoring an exception, or
  adding a sleep → you are suppressing the symptom. The bug is still there.
- You notice "that's weird" and are about to move past it → don't. Unresolved
  weirdness during debugging is almost always the bug waving at you.

## Anti-patterns to name and refuse

| Anti-pattern | What it looks like | Do instead |
|---|---|---|
| Shotgun debugging | Many small edits per run, hoping one helps | One deliberate change per observation |
| Symptom-patching | Special-casing the failing input | Ask why the general path fails |
| Layer-blindness | 10 attempts, all in the same file | Force one hypothesis per layer |
| Confirmation reading | Reading code to confirm your theory | Read to *refute* it — look for what would prove you wrong |
| Fix-by-vibes | "This looks suspicious, let me change it" | State what observation the change is predicted to alter |

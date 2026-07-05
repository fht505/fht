---
name: fable-verification
version: 0.3.1
description: >-
  Verification protocol for code changes. Load before reporting a nontrivial
  code change as complete, and when deciding how much testing a change
  needs. Do NOT load for: docs/comment-only changes, analysis-only tasks
  with no change made, or trivial edits the user asked for verbatim.
---

# Verification Before "Done"

Defers to system instructions, user direction, and repository policy. Where
the environment can't run code, verify as far as tooling allows and report
the boundary honestly.

A change is done when you have **observed the intended behavior**, or have
explicitly reported how far short of that your evidence stops. Predictions
must not be presented as facts.

## The ladder of evidence

Climb as high as the change's stakes warrant; report the rung reached.

1. Parses / typechecks / compiles — rules out typos only.
2. Unit tests pass — meaningful only if a test exercises the changed
   behavior; check that one does, or write one, or say none does.
3. A targeted test fails before the change and passes after — the usual bar
   for bug fixes.
4. You drove the real flow end-to-end (command, endpoint, UI path, pipeline)
   and observed the new behavior.
5. Blast radius checked — callers of changed code still work, adjacent tests
   pass.

## By change type

- **Bug fix**: reproduce first when feasible — otherwise you can't see the
  bug stop happening. Then: repro clean + regression test.
- **Feature**: happy path plus one representative failure path; confirm the
  feature is *reachable* (wired into routing/CLI/exports), not just defined.
- **Refactor**: behavior provably unchanged — affected tests plus one real
  before/after output comparison.
- **Config/build/infra**: run the thing that consumes the config.
- **Performance**: before-and-after measurements under the same conditions;
  without numbers, present the change as expected-but-unmeasured.

## Attack your own change once

Before verifying, switch from author to adversary for one pass: what input,
state, or timing makes this wrong? Empty inputs, nulls, boundaries,
concurrent access, retries, partial failure. The happy path is where you
were looking while writing; the bugs are elsewhere. Category checklist:
`references/edge-cases.md`. For each real risk: handle it, test it, or name
it in your report — avoid the silent "probably fine."

## Honest reporting

- Failures reported **with output** and your best diagnosis — never buried
  in a success narrative.
- Couldn't run something? State exactly what is unverified and what would
  verify it.
- Partial verification? Draw the line precisely ("verified through unit
  tests; the integration path needs a live database").
- Completion bias peaks when attention is lowest — the end of a long task
  is the moment to re-run checks, not skip them.

## The final gate

Answer from tool-call evidence, not memory: (1) what did I run that shows
the new behavior working? (2) what shows I broke nothing adjacent? (3) am I
claiming anything I didn't observe? Move any "yes" from (3) into an
explicitly-labeled unverified section.

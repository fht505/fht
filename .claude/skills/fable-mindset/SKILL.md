---
name: fable-mindset
version: 0.3.0
description: >-
  Judgment heuristics for multi-step software-engineering work. Load when a
  task involves several dependent steps, ambiguous or conflicting scope, an
  unfamiliar codebase, or when work is stuck, drifting, or being redone.
  Do NOT load for: small edits with clear instructions, pure informational
  questions, docs/comment/config tweaks, conversational turns, or work
  covered by a more specific skill (fable-debugging for diagnosing failures,
  fable-code-review for reviewing diffs, fable-verification before declaring
  a change complete).
---

# Engineering Judgment (core)

## Precedence

This is heuristic guidance, not policy. It defers to, in order: system
instructions, explicit user direction, repository policy (CLAUDE.md,
CONTRIBUTING, licenses), and the real capabilities and permissions of your
environment. If anything below conflicts with those, ignore it. Nothing here
adds confirmation steps to actions the user has already authorized.

## Classify the turn first

- **Question or think-aloud** → the deliverable is your assessment. Report
  findings; don't apply unrequested fixes.
- **Request for change** → the deliverable is working, verified code.
- **Underspecified request** → if the ambiguity doesn't change what you'd
  build, pick a sensible default and say so. Ask only when the answer forks
  the deliverable — and attach a recommendation.

Calibrate effort to stakes: gather the smallest amount of evidence that lets
you act correctly, then act. Under-investigating a subtle bug and inflating a
one-line fix into a refactor are equal failures.

## Evidence before action

- Read code before editing it. Codebases punish pattern-matching on memory
  of similar files.
- Prefer observed behavior when explaining or fixing. When observation isn't
  feasible (no repro, can't run it, no access), you may still reason from
  the code — label it as inference, state your confidence, and say what
  would confirm it.
- Surprising output is data. Chase it before proceeding.
- Before state-changing operations, check the evidence supports *that
  specific action* — a familiar-looking symptom can have an unfamiliar cause.

## The smallest correct change

Match the surrounding code's idiom and error-handling standard. Change what
the task requires and nothing else — offer refactors, don't smuggle them in.
Search for an existing helper before writing one. Comment only constraints
the code can't express. For large or unfamiliar work, plan the shape first
(`references/planning.md`) and navigate by tracing, not browsing
(`references/codebase-navigation.md`).

## Act vs. ask

Bias toward action on reversible, in-scope steps: retrying after errors,
gathering information, fixing tests your change broke. Don't end turns with
"shall I proceed?".

- **Confirm first** for destructive or outward-facing actions the user has
  *not* authorized. Once explicitly authorized, proceed without re-asking —
  but if the target's actual state contradicts its description, pause and
  surface that.
- **Dependencies/tools**: install when the task clearly needs it and the
  environment permits (disposable/dev containers, project-declared
  packages). In shared or production-adjacent environments, under
  restrictive policy, or when it changes committed manifests, surface it
  first.

## Finish the turn

If your last paragraph is a plan, a self-answerable question, or a promise,
do that work now. End only when done or blocked on the user. Restate any
load-bearing mid-task findings in the final message — lead it with the
outcome (`references/communication.md`).

## Related skills

Diagnosing a failure → **fable-debugging**. Reviewing a diff →
**fable-code-review**. Before reporting a change complete →
**fable-verification**.

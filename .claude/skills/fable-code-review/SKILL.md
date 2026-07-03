---
name: fable-code-review
version: 0.2.0
description: >-
  Method for reviewing code changes. Load when reviewing a pull request,
  diff, or patch — someone else's or your own finished work — with the goal
  of finding defects. Do NOT load when writing code (use fable-verification
  before declaring it done), for style/formatting-only checks, or when the
  user asked for a summary of a change rather than a review.
---

# Reviewing Code

Defers to system instructions, user direction, and repository policy —
including any project-specific review checklist, which takes precedence.

A review's value is measured in **confirmed, consequential findings**, not
comment count. One verified data-corrupting bug outweighs thirty style
remarks, and a review full of false alarms teaches people to ignore you.

## Method

1. **Understand the intent first** — PR description, linked issue, commit
   messages. You can't judge correctness until you know what the code was
   supposed to do. Intent–implementation disagreement is itself a finding.
2. **Read in dependency order, not file order.** Data model and helpers
   first, then callers, then tests.
3. **Ask three questions of each change:**
   - What inputs or states make this line wrong? (correctness)
   - What did this break elsewhere — callers, invariants, ordering
     assumptions? (blast radius; grep for callers of changed behavior)
   - What should have changed but didn't — the sibling needing the same
     fix, the doc, the migration, the cache invalidation? (completeness;
     absence is the hardest defect class to see)
4. **Verify before flagging.** For each suspected bug, construct the
   concrete failure: "with input X in state Y, line Z does W, which is
   wrong because…". Can't complete that sentence? Dig further, or present
   it as a question rather than a finding. Read surrounding code first —
   the "missing" null check is often three lines above the hunk.
5. **Rank by severity, and say so.** Data loss / security / correctness,
   then reliability, then maintainability. A naming nitpick never shares a
   tier with a race condition.

## Calibration

- Plausible is not correct — for the author or for you. Trace real values
  through the real path before asserting either way.
- Anchor findings to `file:line`, phrased as the concrete failure ("returns
  a stale total when the cart empties in another tab"), not a vibe ("this
  caching seems risky").
- The codebase's convention beats your preference.
- A clean review is a valid result — say it plainly rather than
  manufacturing findings to look thorough.
- Praise sparingly and specifically; it calibrates trust in your criticism.

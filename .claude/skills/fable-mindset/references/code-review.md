# Reviewing Code

Read this when asked to review a diff, a pull request, or someone else's
change — including reviewing your own work before declaring it done.

## The principle

A review's value is measured in **confirmed, consequential findings** — not
in the number of comments. One verified bug that would have corrupted data
outweighs thirty style remarks. Your reputation rides on precision: a review
full of false alarms teaches people to ignore you.

## How to review

1. **Understand the intent first.** Read the PR description, the linked
   issue, the commit messages. You cannot judge whether code is *correct*
   until you know what it was *supposed* to do. If intent and implementation
   disagree, that's your first finding.
2. **Read the diff in dependency order, not file order.** Data model and
   helper changes first, then the callers, then the tests. The alphabetical
   file list is the wrong order to build understanding in.
3. **For each change, ask the three questions:**
   - What inputs/states make this line wrong? (correctness)
   - What did this change break *elsewhere* — callers, invariants, ordering
     assumptions? (blast radius; grep for callers of anything whose behavior
     changed)
   - What should have changed but didn't — the sibling that needed the same
     fix, the doc, the migration, the cache invalidation? (completeness;
     absence is the hardest bug class to see)
4. **Verify before you flag.** For every suspected bug, construct the actual
   failure scenario: "with input X in state Y, line Z does W, which is
   wrong because…". If you can't complete that sentence concretely, either
   dig until you can or downgrade it to a question. Read the surrounding
   code — the "missing" null check is often three lines above the diff hunk.
5. **Rank by severity and say so.** Data loss / security / correctness first,
   then reliability, then maintainability. Never present a naming nitpick
   with the same weight as a race condition.

## Calibration rules

- **The diff being plausible is not the diff being right.** Plausible-but-
  wrong is the default failure mode of both authors and reviewers. Trace the
  actual values through the actual path.
- **Anchor every finding** to `file:line` and phrase it as the concrete
  failure, not a vibe: "returns the stale total when the cart is emptied in
  another tab" beats "this caching seems risky."
- **Don't demand your personal style.** If the codebase has a convention and
  the diff follows it, that's correct even if you'd write it differently.
- **A clean review is a valid result.** If you verified and found nothing
  consequential, say exactly that — do not manufacture findings to look
  thorough.
- **Praise sparingly and specifically** when a change teaches you something
  or handles a subtlety well; it calibrates trust in your criticism.

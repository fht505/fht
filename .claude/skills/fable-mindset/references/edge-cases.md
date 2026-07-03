# Adversarial Self-Review: Break Your Own Change

Read this after writing a nontrivial change and before verifying it — one
deliberate pass where you switch roles from author to attacker. The happy
path is where you were looking while you wrote the code; the bugs are
therefore somewhere else.

## The mindset switch

For five minutes, your job is not "does my change work?" but **"what input,
state, or timing makes my change wrong?"** You are trying to lose. Every
category below is a place authors systematically don't look because they were
busy making the feature work.

Don't apply the whole list mechanically to every change — scan it, pick the
3–4 categories that touch your diff, and think hard about those.

## Boundaries and cardinality

- **Zero, one, many, enormous.** Empty list, empty string, single element,
  exactly the page-size, one past it, and pathological scale (10⁶ items — is
  that loop quadratic?).
- **Off-by-one surfaces:** inclusive vs. exclusive ranges, `<` vs. `<=`,
  first/last iteration of the loop, fence-post counts.
- **Numeric edges:** 0, negatives where you assumed positive, overflow,
  float equality, division by a value that can be zero.

## Absence and malformation

- **Null/None/undefined** at every input you assumed present — especially
  fields from parsed data (JSON, DB rows, env vars, user input).
- **Malformed rather than missing:** wrong type, wrong encoding, trailing
  whitespace, duplicate keys, the string `"null"`.
- **Unicode reality:** multi-byte characters where you count "characters,"
  emoji in names, case-folding surprises. If you sliced, measured, or
  compared strings, this category applies.

## Time and ordering

- **Timezones, DST, and midnight:** "today" differs by observer; date math
  across DST boundaries drifts by an hour.
- **Concurrency and reentrancy:** two requests hit this code simultaneously —
  is the read-modify-write atomic? Can the callback fire twice? What if the
  entity was deleted between your check and your use (TOCTOU)?
- **Retries and idempotency:** the caller retried after a timeout but the
  first attempt actually succeeded — does your operation run twice safely?
- **Partial failure:** the code dies halfway through the multi-step write.
  What state is left behind, and does anything clean it up?

## The world outside the function

- **Error paths under load:** the network call fails, the disk is full, the
  response is a 500 with an HTML body where you parse JSON.
- **Permissions and trust:** the input comes from a user — can it traverse
  paths (`../`), inject into queries/commands/HTML, or reference another
  user's resource ID?
- **Compatibility:** old clients, old data rows, and in-flight jobs from the
  previous version all meet your new code. Does deploy order matter? Is the
  migration safe to run while the old code still serves traffic?
- **Config drift:** the setting you added has a default — is the default
  safe in production, or only convenient in development?

## What to do with what you find

For each real risk: either **handle it** (if the surrounding code's standard
handles that class), **test it** (turn the edge into a test case — edge-case
tests are the highest-value tests you can write), or **name it** in your
report as a known limitation. The one forbidden move is silently deciding
"probably fine" — that decision, made visible, is often the one the user
most wants to weigh in on.

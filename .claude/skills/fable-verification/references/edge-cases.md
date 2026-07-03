# Edge-Case Categories for Adversarial Self-Review

Scan the list, pick the 3–4 categories that touch your diff, and think hard
about those. Don't apply the whole list mechanically to every change.

## Boundaries and cardinality

- Zero, one, many, enormous: empty list, empty string, single element,
  exactly page-size, one past it, pathological scale (is that loop
  quadratic?).
- Off-by-one surfaces: inclusive vs. exclusive ranges, `<` vs. `<=`,
  first/last loop iteration, fence-post counts.
- Numeric edges: 0, negatives where positive was assumed, overflow, float
  equality, division by a possibly-zero value.

## Absence and malformation

- Null/None/undefined at every input assumed present — especially parsed
  data (JSON, DB rows, env vars, user input).
- Malformed rather than missing: wrong type, wrong encoding, trailing
  whitespace, duplicate keys, the string `"null"`.
- Unicode: multi-byte characters where "characters" are counted, emoji in
  names, case-folding surprises — applies whenever strings are sliced,
  measured, or compared.

## Time and ordering

- Timezones, DST, midnight: "today" differs by observer; date math across
  DST boundaries drifts.
- Concurrency and reentrancy: two requests at once — is the
  read-modify-write atomic? Can the callback fire twice? Deleted between
  check and use (TOCTOU)?
- Retries and idempotency: caller retried after a timeout but the first
  attempt succeeded — does the operation run twice safely?
- Partial failure: the process dies mid-way through a multi-step write —
  what state remains, and what cleans it up?

## The world outside the function

- Error paths under load: network call fails, disk full, a 500 with an HTML
  body where JSON was expected.
- Trust boundaries: user-controlled input — path traversal, injection into
  queries/commands/HTML, another user's resource ID.
- Compatibility: old clients, old data rows, and in-flight jobs meet the new
  code. Does deploy order matter? Is the migration safe while old code still
  serves traffic?
- Config drift: is the new setting's default safe in production, or only
  convenient in development?

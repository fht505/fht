# Planning Large Tasks

For work with several dependent steps, spend a short moment planning before
the first edit — a shape, not a ceremony.

- **Name the end state** in observable terms: "endpoint returns X, migration
  applied, old callers updated, tests green." Check progress against that,
  not against "I made edits."
- **Order steps by information value.** Do the step most likely to
  invalidate the plan first — the risky integration, the uncertain API —
  not the easy scaffolding. Discovering a dead end on step 6 of 7 wastes
  steps 1–5.
- **Track steps visibly** (a todo list if the harness has one, otherwise a
  written list) and update as you go; plans drift silently otherwise.
- **Re-plan when reality disagrees.** A plan is a hypothesis. When a step
  disproves it, revise the plan explicitly rather than improvising away from
  it one patch at a time.

## Managing the middle

- **Fan out independent work.** Investigations that don't depend on each
  other can run in parallel; broad searches can be delegated when tooling
  supports it — keep the conclusion, not the file dumps.
- **Don't re-derive settled facts.** If you established the config format
  earlier, trust your note of it; re-litigating burns the attention needed
  for remaining work.
- **Write down load-bearing discoveries in visible output** — direction
  changes and key findings must survive into the final message.

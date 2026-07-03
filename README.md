# fable skills

A set of four narrowly-scoped [Agent Skills](https://code.claude.com/docs/en/skills)
that encode software-engineering judgment heuristics for coding agents such
as Claude Code and Codex: when to act vs. ask, how to debug by hypothesis,
how much verification a change needs, and how to review code for
consequential defects.

Current version: **0.2.0** (see [CHANGELOG.md](CHANGELOG.md)). MIT licensed.

## The skills

| Skill | Loads when | Core words |
|---|---|---|
| `fable-mindset` | Multi-step work with ambiguity, unfamiliar code, or drift | ~520 |
| `fable-debugging` | Diagnosing a failure whose cause is unknown | ~510 |
| `fable-verification` | Before reporting a nontrivial change complete | ~480 |
| `fable-code-review` | Reviewing a PR, diff, or patch for defects | ~400 |

Each skill declares explicit **non-triggers** (small clear edits, pure Q&A,
docs tweaks, conversation) so it stays out of context when irrelevant, and
each defers to system instructions, user direction, repository policy, and
the environment's actual tooling. Deeper material lives in `references/`
files loaded only on demand (planning, codebase navigation, communication,
edge-case categories).

## Install

**Claude Code, per-project:** the skills live in `.claude/skills/` and load
automatically when a session opens in this repo.

**Claude Code, global (all projects):**

```bash
cp -r .claude/skills/fable-* ~/.claude/skills/
```

**Codex / other agents (optional, unsupported):** these are Claude Code
skills first. [packaging/codex/README.md](packaging/codex/README.md) has an
`AGENTS.md` snippet that points other agents at the same files, provided
as-is — it is not evaluated by the test suite and not maintained as a
supported target.

Skills can also be invoked explicitly (`/fable-debugging`) or by asking the
model to read the relevant `SKILL.md`.

## Evaluation

`evals/` contains an A/B evaluation suite: paired runs with and without the
skills on realistic tasks, objective holdout graders (plain Python, no
dependencies), process rubrics with expected behaviors and failure cases,
and cost tracking. Method: [evals/README.md](evals/README.md). Current
evidence: [evals/RESULTS.md](evals/RESULTS.md).

**No unsupported performance claims are made.** Treat the skills as
hypotheses about useful guidance until the eval results in RESULTS.md say
otherwise at adequate sample size.

## Provenance

These skills were authored with the assistance of a Claude model, distilling
general agentic-engineering practices (hypothesis-driven debugging,
verification laddering, minimal-diff discipline). "fable" is used here as a
family name for the skill set; it does not imply endorsement by, or
measured equivalence to, any particular model or vendor.

## Versioning

Semantic versioning. The `version` field in each SKILL.md frontmatter tracks
the release in CHANGELOG.md; skills in one release are tested together and
should be installed together.

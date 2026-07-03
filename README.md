# fable-mindset

A Claude Code skill that upgrades how Claude Opus 4.8 (or any Claude model)
reasons, decides, and executes on engineering tasks — distilled from the
operating doctrine of Claude Fable 5.

It teaches the judgment layer that separates strong agents from average ones:

- **Task classification** — assessment vs. change, and calibrating effort to stakes
- **Planning big work** — risk-first step ordering and visible progress tracking
- **Codebase navigation** — trace from entry points and precedents instead of browsing
- **Evidence-first investigation** — read before editing, observe before explaining
- **Hypothesis-driven debugging** — shrink the search space instead of guess-and-check
- **Smallest correct change** — diffs that read like the original author wrote them
- **Autonomy judgment** — act on reversible steps, hard-stop on destructive ones
- **Adversarial self-review** — attack your own change (edges, nulls, races, retries) before shipping it
- **Code review method** — confirmed consequential findings over comment count
- **Verification discipline** — a ladder of evidence, and honest reporting of the rung reached
- **Outcome-first communication** — final messages that lead with what happened

## Layout

```
.claude/skills/fable-mindset/
├── SKILL.md                     # Core doctrine — loaded when the skill triggers
└── references/
    ├── code-review.md           # Reviewing diffs/PRs: verify-before-flag, severity ranking
    ├── codebase-navigation.md   # Exploring unfamiliar code with purpose
    ├── debugging.md             # Full hypothesis-testing debug loop + anti-patterns
    ├── edge-cases.md            # Adversarial self-review: boundaries, nulls, time, races
    ├── verification.md          # Verification protocol and the final gate
    └── communication.md         # Report structure, style, and honesty patterns
```

The SKILL.md holds the essentials; the reference files are progressive
disclosure — the model reads them only when a task calls for that depth.

## Install

**Per-project:** this repo already has it in place — clone and open Claude
Code in the repo root; the skill loads from `.claude/skills/` automatically.

**Globally (all projects):** copy the skill folder into your personal skills
directory:

```bash
cp -r .claude/skills/fable-mindset ~/.claude/skills/
```

## Use

The skill's description triggers it automatically at the start of nontrivial
engineering tasks. You can also invoke it explicitly:

```
/fable-mindset
```

or tell the model: "load the fable-mindset skill before starting."

# Runner

How campaigns are executed and what gets committed per run.

## Execution harness

- Runner: Claude Code `Agent` tool, subagent type `general-purpose`,
  `model: opus` (Claude Opus 4.8), `isolation: worktree` (each run gets a
  fresh git worktree at the repo HEAD), background execution.
- Prompts: verbatim from `prompts/` — one file per task × condition. The
  orchestrator substitutes nothing; prompts are used as committed.
- Conditions:
  - **A (control):** first line forbids reading `.claude/`; repo skills
    excluded.
  - **B (auto):** no mention of skills at all. Measures whether the model
    loads the skills unprompted (trigger rate), judged from the run
    transcript, and what that does to the outcome.
  - **C (explicit):** first line instructs reading the relevant SKILL.md
    files.
  - **N (negative-trigger):** trivial/unrelated tasks with no mention of
    skills. Pass = the transcript shows no skill file was read.
- Agents must return exactly one fenced JSON object (schema in each prompt);
  the orchestrator persists it and the run metadata as artifacts.

## Artifacts per run (`evals/runs/<campaign>/<run-id>/`)

| File | Contents | Source |
|---|---|---|
| `prompt.txt` | exact prompt sent | committed template |
| `result.json` | the agent's returned JSON (patch, verification, cause) | agent final message |
| `patch.diff` | the `patch` field, extracted | agent |
| `grade.txt` | holdout grader stdout/exit | `grade.sh` |
| `usage.json` | output tokens, tool calls, wall ms | harness task notification |
| `skill_reads.txt` | matches for skill-file reads in the transcript | grep over run transcript |

Campaign-level: `config.json` (model, date, conditions, trial counts) and
`summary.md`. Raw transcripts are retained by the harness outside the repo;
only the derived `skill_reads.txt` is committed because raw subagent
transcripts embed harness-internal system text. This filtering is the one
non-reproducible-from-repo step and is disclosed here.

## Grading

```bash
evals/runner/grade.sh 05-duplicate-orders evals/runs/<campaign>/<run>/patch.diff
```

Applies the patch to a pristine fixture extracted from `git HEAD` and runs
the task's `holdout/holdout_check.py`. Exit 0 + `holdout passed` = pass.

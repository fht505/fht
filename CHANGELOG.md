# Changelog

All notable changes to the fable skill set. Follows
[Keep a Changelog](https://keepachangelog.com/) and semantic versioning.

## [0.3.0] - 2026-07-04

Evaluation release — no changes to skill prose.

### Added
- Task 05 (root-cause trap): symptom in the report layer, cause in the
  data layer; holdout rejects symptom patches. Validated in both
  directions.
- Campaign runner: committed verbatim prompts per condition, `grade.sh`,
  per-run artifact layout, negative-trigger fixtures.
- Campaign 2026-07-04-slim: 21 Opus 4.8 runs (n=5 × control/auto/explicit
  on task 05 + 6 negative-trigger runs) with per-run patches, grades,
  usage data, and skill-access classification committed under
  `evals/runs/`.

### Findings (see evals/RESULTS.md)
- 15/15 correctness across conditions (task below model ceiling).
- Explicit skill loading: +17% tokens, no measurable gain on this task.
- Auto-trigger unmeasurable in subagent harness (0/5; needs interactive
  sessions). Negative triggers 6/6 clean, same caveat.

### Changed
- Codex packaging explicitly labeled optional and unsupported.

## [0.2.0] - 2026-07-03

### Changed
- Narrowed every skill's trigger: descriptions now state explicit triggers
  AND explicit non-triggers; the mindset skill no longer loads for every
  nontrivial task.
- Reduced `fable-mindset` core from ~2,000 to ~520 words; planning and
  mid-task management moved to `references/planning.md`.
- Calibrated absolute rules into conditional guidance:
  - "never explain unobserved behavior" → prefer observation; unobservable
    cases may be explained as labeled inference with stated confidence.
  - "two failed attempts means the theory is wrong" → failures count
    against a theory in proportion to how diagnostic each attempt was.
  - automatic dependency installation → gated on environment type, policy,
    and whether committed manifests change.
  - confirmation prompts → not re-asked for actions the user already
    explicitly authorized (evidence-contradiction still pauses).
- All skills now open with a precedence statement deferring to system
  instructions, user direction, repository policy, and available tooling.
- Removed unsupported provenance/performance claims; provenance documented
  in README instead.

### Added
- Standalone skills: `fable-debugging`, `fable-verification`,
  `fable-code-review` (formerly references inside fable-mindset).
- `evals/`: A/B methodology, two runnable fixture tasks with validated
  objective holdout graders, two spec-only tasks, rubrics, RESULTS.md.
- Repository hygiene: MIT LICENSE, this changelog, `version` in skill
  frontmatter, `.gitignore`, Codex packaging notes, `main` branch.

## [0.1.0] - 2026-07-03

### Added
- Initial release: single `fable-mindset` skill with references for
  debugging, verification, communication, codebase navigation, code
  review, and edge cases.

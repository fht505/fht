# Using the fable skills with Codex (and other AGENTS.md-based agents)

Codex and similar agents read repository instructions from `AGENTS.md`
rather than `.claude/skills/`. The skill files are plain Markdown, so the
simplest integration is a routing snippet that tells the agent when to read
which file.

Append the contents of `AGENTS-snippet.md` to your repository's `AGENTS.md`
(create the file if it doesn't exist), adjusting paths if you vendored the
skills elsewhere.

Notes:

- Keep the routing conditional. Pasting entire skill bodies into AGENTS.md
  defeats the trigger narrowing and pays their token cost on every turn.
- The YAML frontmatter at the top of each SKILL.md is Claude Code metadata;
  other agents can ignore it — the body is self-contained.

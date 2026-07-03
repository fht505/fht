# Navigating an Unfamiliar Codebase

Read this when starting work in a codebase (or subsystem) you haven't touched
before, or when you've been reading files for a while without getting traction.

## The principle

You are not trying to *understand the codebase* — you are trying to build the
**minimum mental model that makes your specific task safe**. Reading breadth-
first "to get familiar" is procrastination with extra steps. Every file you
open should be an answer to a question you actually have.

## Orient in this order (usually under ten tool calls)

1. **The map**: top-level directory listing, the manifest
   (`package.json` / `pyproject.toml` / `go.mod` / `Cargo.toml`), and any
   `README`/`CONTRIBUTING`/`CLAUDE.md`. From these you learn: language,
   framework, how it's run, how it's tested, and the vocabulary the project
   uses for its own concepts.
2. **The entry point relevant to your task** — not the app's main() in
   general, but where *your* flow starts: the route definition, the CLI
   subcommand, the event handler, the cron job.
3. **Trace the flow, don't browse.** Follow the call chain from that entry
   point toward the code you need to change, opening only files on the path.
   Two levels of depth along the real path beats ten files of skimming.
4. **Find the sibling.** Almost every task has a precedent: an endpoint like
   the one you're adding, a fix like the one you're making, a test like the
   one you'll write. Find it and let it teach you the house style, the
   helpers that exist, and the registration steps you'd otherwise miss.

## Search like a professional

- **Search for distinctive strings, not concepts.** Error messages (in
  quotes, exactly as shown), config keys, route paths, and unusual
  identifiers hit precisely. Generic terms (`user`, `handle`, `process`)
  drown you.
- **Work backward from output.** You can see what the program produces — a
  log line, an HTML snippet, a column name. Grep for it. The producer of that
  output is a fixed point from which to trace backward.
- **Grep for callers before changing any shared function** — the signature
  you're about to change has friends you haven't met.
- **Let tests be documentation.** The test file for a module states its
  intended behavior more honestly than comments do, and shows how to
  construct its inputs.
- **Delegate broad sweeps.** When the question is "everywhere that X happens
  across the repo," fan it out to a search agent if available and keep the
  conclusion — don't fill your own context with file dumps.

## Traction check

Every few minutes of exploration, ask: *can I now name (a) the file(s) I will
change, (b) the code path that reaches them, and (c) how I will verify the
change?* If yes — stop exploring; you have enough. If no progress on those
three for several tool calls in a row, your search strategy is wrong: return
to the entry point, or find the sibling, or grep for the output string
instead of reading more files.

## Respect the grain of the codebase

What you learn while navigating is not just *where* things are but *how this
project does things* — its error handling, its layering, its naming, its test
shape. Your change must follow that grain even where you'd personally choose
differently. A technically better pattern that's foreign to the codebase is a
worse contribution than a native-idiom one.

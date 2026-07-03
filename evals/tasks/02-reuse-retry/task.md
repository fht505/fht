# Task: retry transient fetch failures

Transient network errors make `fetch_json` fail intermittently in
production. Make `fetch_json` retry — up to 3 attempts total — before
failing.

The codebase is in `fixture/`. When finished, report:

1. a unified diff of every change you made,
2. exactly what you ran or checked to verify, with output,
3. any assumptions you made.

# Task: pagination bug

Bug report from users: **"the last item of every page is missing"** from API
responses.

The pagination logic lives in `fixture/pagination.py`. The project's test
script is `fixture/run_tests.py` (run with `python run_tests.py` from inside
`fixture/`).

Investigate and fix the bug. When finished, report:

1. a unified diff of every change you made,
2. exactly what you ran to verify, with output,
3. a short statement of the cause.

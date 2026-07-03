# Task: assessment-only classification (spec)

**Status: spec only — fixture not yet built.**

Prompt shape: a question, not a change request, e.g. "Why does the monthly
report show duplicate rows for some customers?" against a fixture containing
a join that fans out on a non-unique key.

Purpose: measure turn classification — whether the model delivers a
diagnosis and stops, versus applying an unrequested fix.

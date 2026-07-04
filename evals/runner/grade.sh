#!/usr/bin/env bash
# usage: evals/runner/grade.sh <task-name> <patch-file>
# Applies the patch to a pristine copy of the task (from git HEAD) and runs
# the holdout grader. Run from the repo root. Exit 0 = holdout passed.
set -u
task="$1"
patch="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

git archive HEAD "evals/tasks/$task" | tar -x -C "$tmp" || exit 2

if [ -s "$patch" ]; then
  (cd "$tmp" && git apply "$patch" 2>/dev/null) ||
    (cd "$tmp" && patch -p1 -s <"$patch") || { echo "PATCH FAILED TO APPLY"; exit 3; }
fi

PYTHONPATH="$tmp/evals/tasks/$task/fixture" python3 "$tmp/evals/tasks/$task/holdout/holdout_check.py"

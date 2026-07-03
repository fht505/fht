# Objective grader. Run with PYTHONPATH pointing at the (patched) fixture:
#   PYTHONPATH=path/to/fixture python holdout_check.py
from report import build_report, total_billed

lines = sorted(build_report())
expected = sorted(
    [
        ("a@acme.test", 101, 50),
        ("b@acme.test", 102, 75),
        ("z@zenith.test", 103, 20),
        ("z@zenith.test", 104, 20),
    ]
)

assert lines == expected, f"report lines wrong:\n got: {lines}\n want: {expected}"
assert total_billed() == 165, f"total_billed() == {total_billed()}, want 165"

print("holdout passed")

# Objective grader. Run with PYTHONPATH pointing at the (patched) fixture:
#   PYTHONPATH=path/to/fixture python holdout_check.py
from pagination import paginate

items = list(range(10))

assert paginate(items, 1, 3) == [0, 1, 2], "page 1 must contain all 3 items"
assert paginate(items, 2, 3) == [3, 4, 5], "page 2 must contain all 3 items"
assert paginate(items, 4, 3) == [9], "final partial page must have its item"
assert paginate(items, 1, 1) == [0], "page_size=1 must return one item"
assert paginate(items, 5, 3) == [], "past-the-end page must be empty"
assert paginate([], 1, 3) == [], "empty input must paginate to empty"

print("holdout passed")

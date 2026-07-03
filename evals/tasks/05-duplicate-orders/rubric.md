# Rubric: 05-duplicate-orders

A root-cause trap. The planted bug is in the **data layer**:
`queries.py:orders_for_customer` matches orders to customers **by display
name** instead of by id. Two customers named "Acme" therefore each receive
both Acme customers' orders, which surfaces downstream as duplicated lines
in `report.py` — the module the symptom points at.

Correct minimal fix: match on `order["customer_id"] == customer["id"]` in
`queries.py`.

The trap: deduplicating in the report layer *looks* like it fixes the
symptom but cannot attribute order 102 to the right customer, and risks
collapsing the two legitimate identical Zenith orders (103/104, same
amount). The holdout distinguishes root-cause fixes from symptom patches.

## Objective gate (primary)

Apply the run's diff to a pristine `fixture/`, then:
`PYTHONPATH=fixture python holdout/holdout_check.py` → must print
`holdout passed` (exact expected lines AND `total_billed() == 165`).

## Expected behaviors (process score, +1 each)

- Reproduced/observed the duplication before changing code.
- Traced the symptom from `report.py` back to `queries.py` — fixed the
  join, not the presentation.
- Fix is minimal and in `queries.py`; no changes to `store.py` data or
  report-layer dedup added.
- Added or strengthened a test covering shared-name customers or repeat
  purchases.
- Cause statement names the name-vs-id join explicitly.

## Failure cases (−1 each)

- Symptom patch: dedup/`set()`/`groupby` in `report.py` while the join bug
  remains.
- "Fixed" the data: renamed a customer in `store.py` so names are unique.
- Changed visible tests to pass without fixing the join.
- Claimed verification without discriminating output (the visible tests
  pass with the bug present).

## Cost

Record tokens/tool calls or proxies, as in the suite README.

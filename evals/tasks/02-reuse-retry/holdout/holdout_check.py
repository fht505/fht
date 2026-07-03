# Objective grader. Run with PYTHONPATH pointing at the (patched) fixture:
#   PYTHONPATH=path/to/fixture python holdout_check.py
import io
import json
import time

time.sleep = lambda s: None  # neutralize backoff delays

import client


class FakeResp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


calls = {"n": 0, "fail_always": False}


def fake_urlopen(url, timeout=10):
    calls["n"] += 1
    if calls["fail_always"] or calls["n"] < 3:
        raise OSError("simulated transient failure")
    return FakeResp(json.dumps({"ok": True}).encode("utf-8"))


client.urllib.request.urlopen = fake_urlopen

# Two transient failures then success: fetch_json must succeed on try 3.
assert client.fetch_json("http://example.test/x") == {"ok": True}
assert calls["n"] == 3, f"expected 3 attempts, saw {calls['n']}"

# Persistent failure: must raise after exactly 3 attempts, not loop forever.
calls["n"] = 0
calls["fail_always"] = True
try:
    client.fetch_json("http://example.test/x")
    raise SystemExit("expected fetch_json to raise on persistent failure")
except OSError:
    pass
assert calls["n"] == 3, f"expected 3 attempts on persistent failure, saw {calls['n']}"

print("holdout passed")

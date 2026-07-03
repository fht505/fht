import json
import urllib.request


def fetch_json(url, timeout=10):
    """Fetch `url` and decode the response body as JSON."""
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))

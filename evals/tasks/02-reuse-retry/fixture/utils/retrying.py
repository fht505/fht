import time


def with_retries(fn, attempts=3, base_delay=0.1):
    """Call fn(); on exception, retry up to `attempts` total tries with
    exponential backoff. Re-raises the last error."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception:
            if attempt == attempts:
                raise
            time.sleep(base_delay * 2 ** (attempt - 1))

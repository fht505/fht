from client import fetch_json
from storage import save_record
from utils.retrying import with_retries


def sync_catalog(base_url, records):
    """Push local records upstream, then return the fresh catalog."""
    for record in records:
        with_retries(lambda record=record: save_record(record))
    return fetch_json(base_url + "/catalog")

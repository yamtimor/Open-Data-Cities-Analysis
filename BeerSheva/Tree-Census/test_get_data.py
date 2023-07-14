import pytest
from get_data import *

def test_get_records():
    params = load_config()
    base_url = params.get("base_url", "")
    api_uri = params.get("api_uri", "")
    resource_id = params.get("resource_id", "")
    limit = params.get("limit", 0)
    results = get_records(base_url, api_uri, resource_id, limit)

    # Check that the results are not empty
    assert len(results) > 0

    # Check that the number of unique ids is equal to the number of records(list of json)
    assert len(results) == len(set(record["_id"] for record in results))



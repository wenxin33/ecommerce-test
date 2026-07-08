import pytest

from api.base_client import BaseClient
from utils.yaml_reader import read_yaml


cart_cases = read_yaml("data/cart_cases.yaml")


@pytest.mark.parametrize("case", cart_cases)
def test_cart_api(case, client, auth_client, reset_data):
    if case["token_type"] == "valid":
        current_client = auth_client

    elif case["token_type"] == "invalid":
        current_client = BaseClient()
        current_client.set_token("wrong_token")

    else:
        current_client = client

    if case["method"] == "post":
        response = current_client.post(case["path"], json=case.get("json_data"))

    elif case["method"] == "get":
        response = current_client.get(case["path"])

    else:
        raise ValueError(f"Unsupported method: {case['method']}")

    data = response.json()

    assert response.status_code == case["expected_http_status"]
    assert data.get("code") == case["expected_code"]
    assert data.get("message") == case["expected_message"]

    if case["expected_code"] == 200:
        assert "data" in data
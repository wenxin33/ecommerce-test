import pytest

from api.base_client import BaseClient
from utils.yaml_reader import read_yaml


order_cases = read_yaml("data/order_cases.yaml")


def prepare_cart(auth_client):
    response = auth_client.post("/cart", json={
        "product_id": 1,
        "quantity": 1
    })

    data = response.json()
    assert data.get("code") == 200


def prepare_order(auth_client):
    prepare_cart(auth_client)

    response = auth_client.post("/order")
    data = response.json()

    assert data.get("code") == 200
    return data["data"]["order_id"]


@pytest.mark.parametrize("case", order_cases)
def test_order_api(case, client, auth_client, reset_data):
    if case["token_type"] == "valid":
        current_client = auth_client

    elif case["token_type"] == "invalid":
        current_client = BaseClient()
        current_client.set_token("wrong_token")

    else:
        current_client = client

    if case.get("prepare_cart") and case["token_type"] == "valid":
        prepare_cart(auth_client)

    if case.get("prepare_order") and case["token_type"] == "valid":
        order_id = prepare_order(auth_client)
        if case["path"] == "/order/1":
            case["path"] = f"/order/{order_id}"

    if case["method"] == "post":
        response = current_client.post(case["path"])

    elif case["method"] == "get":
        response = current_client.get(case["path"])

    else:
        raise ValueError(f"Unsupported method: {case['method']}")

    assert response.status_code == case["expected_http_status"]

    if case.get("flask_404"):
        return

    data = response.json()

    assert data.get("code") == case["expected_code"]
    assert data.get("message") == case["expected_message"]

    if case["expected_code"] == 200:
        assert "data" in data
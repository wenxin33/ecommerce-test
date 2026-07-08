import pytest
import allure

from api.base_client import BaseClient
from utils.yaml_reader import read_yaml


order_cases = read_yaml("data/order_cases.yaml")


def prepare_cart(auth_client):
    """
    前置步骤：给已登录用户添加购物车数据
    """
    response = auth_client.post("/cart", json={
        "product_id": 1,
        "quantity": 1
    })

    data = response.json()

    assert response.status_code == 200
    assert data.get("code") == 200


def prepare_order(auth_client):
    """
    前置步骤：先加购物车，再创建订单，并返回订单ID
    """
    prepare_cart(auth_client)

    response = auth_client.post("/order")
    data = response.json()

    assert response.status_code == 200
    assert data.get("code") == 200

    return data["data"]["order_id"]


@allure.feature("订单模块")
@allure.story("订单接口")
@pytest.mark.parametrize("case", order_cases)
def test_order_api(case, client, auth_client, reset_data):
    allure.dynamic.title(f"{case['case_id']} - {case['case_name']}")

    if case["token_type"] == "valid":
        current_client = auth_client

    elif case["token_type"] == "invalid":
        current_client = BaseClient()
        current_client.set_token("wrong_token")

    else:
        current_client = client

    with allure.step("准备购物车前置数据"):
        if case.get("prepare_cart") and case["token_type"] == "valid":
            prepare_cart(auth_client)

    with allure.step("准备订单前置数据"):
        if case.get("prepare_order") and case["token_type"] == "valid":
            order_id = prepare_order(auth_client)

            if case["path"] == "/order/1":
                case["path"] = f"/order/{order_id}"

    with allure.step("发送订单接口请求"):
        if case["method"] == "post":
            response = current_client.post(case["path"])

        elif case["method"] == "get":
            response = current_client.get(case["path"])

        else:
            raise ValueError(f"Unsupported method: {case['method']}")

    with allure.step("校验 HTTP 状态码"):
        assert response.status_code == case["expected_http_status"]

    if case.get("flask_404"):
        return

    data = response.json()

    with allure.step("校验业务 code 和 message"):
        assert data.get("code") == case["expected_code"]
        assert data.get("message") == case["expected_message"]

    with allure.step("校验成功响应中包含 data 字段"):
        if case["expected_code"] == 200:
            assert "data" in data
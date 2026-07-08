from unittest import case

import pytest
import allure

from api.base_client import BaseClient
from utils.yaml_reader import read_yaml


product_cases = read_yaml("data/product_cases.yaml")

@allure.feature("商品模块")
@allure.story("商品接口")   
@pytest.mark.parametrize("case", product_cases)
def test_product_api(case):
    allure.dynamic.title(f"{case['case_id']} - {case['case_name']}")

    client = BaseClient()

    response = client.get(case["path"])

    assert response.status_code == case["expected_http_status"]

    # Flask 路由未匹配时，返回的可能不是 JSON，所以这里直接结束
    if case["request_type"] == "flask_404":
        return

    data = response.json()

    assert data.get("code") == case["expected_code"]
    assert data.get("message") == case["expected_message"]

    if case["request_type"] == "list":
        assert isinstance(data.get("data"), list)
        assert len(data.get("data")) > 0

        first_product = data["data"][0]
        assert "id" in first_product
        assert "name" in first_product
        assert "price" in first_product
        assert "stock" in first_product

    elif case["request_type"] == "detail":
        assert isinstance(data.get("data"), dict)
        assert data["data"]["id"] == case["expected_product_id"]
        assert "name" in data["data"]
        assert "price" in data["data"]
        assert "stock" in data["data"]

    elif case["request_type"] == "not_found":
        assert "data" not in data
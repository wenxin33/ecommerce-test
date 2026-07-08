import pytest
import allure

from api.base_client import BaseClient
from utils.yaml_reader import read_yaml

login_cases = read_yaml("data/login_cases.yaml")

@allure.feature("登录模块")
@allure.story("登录接口")
@pytest.mark.parametrize("case", login_cases)
def test_login(case):
    allure.dynamic.title(f"{case['case_id']} - {case['case_name']}")

    client = BaseClient()

    with allure.step("发送登录请求"):
        response = client.post("/login", json=case["json_data"])
        data = response.json()

    with allure.step("校验 HTTP 状态码"):
        assert response.status_code == 200

    with allure.step("校验业务 code 和 message"):
        assert data.get("code") == case["expected_code"]
        assert data.get("message") == case["expected_message"]

    with allure.step("校验 token 是否符合预期"):
        if case["expect_token"]:
            assert "token" in data
            assert data["token"] != ""
        else:
            assert "token" not in data
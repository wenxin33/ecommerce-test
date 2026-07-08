import pytest
from utils.yaml_reader import read_yaml
import allure




case_data = read_yaml("data/mock_api_cases.yaml")
get_cases = case_data["get_cases"]
post_cases = case_data["post_cases"]
@allure.feature("用户模块")
@allure.story("获取用户信息")

@pytest.mark.parametrize("case", get_cases)

def test_get_api(user_api, case):
    with allure.step("发送GET请求"):
        response = user_api.get_user(case.get("params"))
    data = response.json()

    expected = case["expected"]

    with allure.step("校验状态码"):
        assert response.status_code == 200

    with allure.step("校验返回内容"):
        assert response.json()["code"] == 200

@pytest.mark.parametrize("case", post_cases)
def test_post_api(user_api, case):
    response = user_api.create_user(case["json"])
    data = response.json()

    expected = case["expected"]

    assert response.status_code == expected["status_code"]
    assert data["code"] == expected["code"]
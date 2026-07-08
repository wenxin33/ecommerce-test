import pytest

from api.base_client import BaseClient
from utils.yaml_reader import read_yaml


login_cases = read_yaml("data/login_cases.yaml")


@pytest.mark.parametrize("case", login_cases)
def test_login(case):
    client = BaseClient()

    response = client.post("/login", json=case["json_data"])
    data = response.json()

    assert response.status_code == 200
    assert data.get("code") == case["expected_code"]
    assert data.get("message") == case["expected_message"]

    if case["expect_token"]:
        assert "token" in data
        assert data["token"] != ""
    else:
        assert "token" not in data
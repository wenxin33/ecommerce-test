import requests
import pytest

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.parametrize("params, expected_code, expected_username, expected_age", [
    # Test case 1: Valid parameters
    ({"username": "test001", "age": "18"}, 200, "test001", "18"),
    # Test case 2: Missing username
    ({"username":"", "age": "18"}, 200, "", "18"),
    # Test case 3: Missing age
    ({"username": "test001", "age": ""}, 200, "test001", ""),
    # Test case 4: Age is 负数
    ({"username": "test001", "age": "-1"}, 200, "test001", "-1"),
    # Test case 5: 超长username
    ({"username": "a" * 1000, "age": "18"}, 200, "a" * 1000, "18"),

    # Test case 6: USERNAME 特殊字符
    ({"username": "!@#$%^&*()", "age": "18"}, 200, "!@#$%^&*()", "18"),
])
def test_get_with_params(params, expected_code, expected_username, expected_age):
    response = requests.get(f"{BASE_URL}/get", params=params)
    data = response.json()

    assert response.status_code == expected_code
    assert data.get("code") == expected_code
    assert data.get("args", {}).get("username") == expected_username
    assert data.get("args", {}).get("age") == expected_age
    


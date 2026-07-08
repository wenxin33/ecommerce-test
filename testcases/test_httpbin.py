import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_status_code():
    response = requests.get(f"{BASE_URL}/get")

    assert response.status_code == 200


def test_get_response_body():
    response = requests.get(f"{BASE_URL}/get")
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["message"] == "success"
    assert data["method"] == "GET"


def test_get_with_params():
    params = {
        "username": "test001",
        "age": "18"
    }

    response = requests.get(f"{BASE_URL}/get", params=params)
    data = response.json()

    assert response.status_code == 200
    assert data["args"]["username"] == "test001"
    assert data["args"]["age"] == "18"


def test_post_with_json():
    payload = {
        "username": "test001",
        "password": "123456"
    }

    response = requests.post(f"{BASE_URL}/post", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["message"] == "success"
    assert data["method"] == "POST"
    assert data["json"]["username"] == "test001"
    assert data["json"]["password"] == "123456"
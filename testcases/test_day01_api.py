import requests

def test_get():
    url = "http://127.0.0.1:8000/get"

    response = requests.get(url)

    print("Response status code:", response.status_code)
    print("Response body:", response.json())

    assert response.status_code == 200
    assert response.json().get("code") == 200

def test_get_with_params():
    url = "http://127.0.0.1:8000/get"
    params = {
       "username": "test001",
        "age": "18"
    }
    response = requests.get(url, params=params)

    data = response.json()

    assert data.get("code") == 200
    assert params.get("username") == "test001"
    assert params.get("age") == "18"


def test_post():
    url = "http://127.0.0.1:8000/post"
    json_data = {
        "username": "admin",
        "password": "123456"
    }

    response = requests.post(url, json=json_data)

    data = response.json()

    assert data.get("code") == 200
    assert data["json"]["username"] == "admin"
    assert data["json"]["password"] == "123456"
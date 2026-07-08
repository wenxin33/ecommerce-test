def test_client_fixture(client):
    response = client.get("/products")
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200


def test_token_fixture(token):
    assert token == "token_abc123"


def test_auth_client_fixture(auth_client):
    response = auth_client.get("/cart")
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["message"] == "success"


def test_reset_data_fixture(auth_client, reset_data):
    response = auth_client.get("/cart")
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["data"] == []
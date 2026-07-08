from api.base_client import BaseClient


def test_base_client_login():
    client = BaseClient()

    response = client.post("/login", json={
        "username": "test001",
        "password": "123456"
    })

    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["token"] == "token_abc123"


def test_base_client_get_products():
    client = BaseClient()

    response = client.get("/products")
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert len(data["data"]) > 0


def test_base_client_add_cart_with_token():
    client = BaseClient()

    login_response = client.post("/login", json={
        "username": "test001",
        "password": "123456"
    })

    token = login_response.json()["token"]
    client.set_token(token)

    response = client.post("/cart", json={
        "product_id": 1,
        "quantity": 2
    })

    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["message"] == "Add to cart success"
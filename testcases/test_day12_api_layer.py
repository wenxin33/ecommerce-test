from api.login_api import LoginAPI
from api.product_api import ProductAPI
from api.cart_api import CartAPI
from api.order_api import OrderAPI


def test_login_api_layer(client):
    login_api = LoginAPI(client)

    response = login_api.login("test001", "123456")
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["token"] == "token_abc123"


def test_product_api_layer(client):
    product_api = ProductAPI(client)

    response = product_api.get_products()
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert isinstance(data["data"], list)


def test_cart_api_layer(auth_client, reset_data):
    cart_api = CartAPI(auth_client)

    response = cart_api.add_to_cart(product_id=1, quantity=1)
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["message"] == "Add to cart success"


def test_order_api_layer(auth_client, reset_data):
    cart_api = CartAPI(auth_client)
    order_api = OrderAPI(auth_client)

    cart_api.add_to_cart(product_id=1, quantity=1)

    response = order_api.create_order()
    data = response.json()

    assert response.status_code == 200
    assert data["code"] == 200
    assert data["message"] == "Create order success"
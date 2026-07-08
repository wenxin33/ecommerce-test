from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟商品数据
PRODUCTS = [
    {"id": 1, "name": "iPhone 15", "price": 5999, "stock": 10},
    {"id": 2, "name": "MacBook Air", "price": 7999, "stock": 5},
    {"id": 3, "name": "AirPods Pro", "price": 1999, "stock": 20},
]

# 模拟购物车和订单数据
CART = []
ORDERS = []

VALID_TOKEN = "token_abc123"


def check_token():
    """
    检查请求头里的 Authorization 是否正确
    """
    token = request.headers.get("Authorization")
    return token == f"Bearer {VALID_TOKEN}"


@app.route("/login", methods=["POST"])
def login():
    """
    登录接口
    正确账号：test001
    正确密码：123456
    """
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    if username == "test001" and password == "123456":
        return jsonify({
            "code": 200,
            "message": "success",
            "token": VALID_TOKEN
        })

    return jsonify({
        "code": 401,
        "message": "Invalid credentials"
    })


@app.route("/products", methods=["GET"])
def get_products():
    """
    获取商品列表
    """
    return jsonify({
        "code": 200,
        "message": "success",
        "data": PRODUCTS
    })


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_detail(product_id):
    """
    获取商品详情
    """
    for product in PRODUCTS:
        if product["id"] == product_id:
            return jsonify({
                "code": 200,
                "message": "success",
                "data": product
            })

    return jsonify({
        "code": 404,
        "message": "Product not found"
    })


@app.route("/cart", methods=["POST"])
def add_to_cart():
    """
    添加商品到购物车
    需要 token
    """
    if not check_token():
        return jsonify({
            "code": 401,
            "message": "Unauthorized"
        })

    data = request.get_json() or {}

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if product_id is None:
        return jsonify({
            "code": 400,
            "message": "product_id is required"
        })

    if quantity is None:
        return jsonify({
            "code": 400,
            "message": "quantity is required"
        })

    if not isinstance(product_id, int):
        return jsonify({
            "code": 400,
            "message": "product_id must be integer"
        })

    if not isinstance(quantity, int):
        return jsonify({
            "code": 400,
            "message": "quantity must be integer"
        })

    if quantity <= 0:
        return jsonify({
            "code": 400,
            "message": "quantity must be greater than 0"
        })

    target_product = None
    for product in PRODUCTS:
        if product["id"] == product_id:
            target_product = product
            break

    if target_product is None:
        return jsonify({
            "code": 404,
            "message": "Product not found"
        })

    if quantity > target_product["stock"]:
        return jsonify({
            "code": 400,
            "message": "Insufficient stock"
        })

    CART.append({
        "product_id": product_id,
        "quantity": quantity
    })

    return jsonify({
        "code": 200,
        "message": "Add to cart success",
        "data": CART
    })


@app.route("/cart", methods=["GET"])
def get_cart():
    """
    查询购物车
    需要 token
    """
    if not check_token():
        return jsonify({
            "code": 401,
            "message": "Unauthorized"
        })

    return jsonify({
        "code": 200,
        "message": "success",
        "data": CART
    })


@app.route("/order", methods=["POST"])
def create_order():
    """
    创建订单
    需要 token
    购物车不能为空
    """
    if not check_token():
        return jsonify({
            "code": 401,
            "message": "Unauthorized"
        })

    if len(CART) == 0:
        return jsonify({
            "code": 400,
            "message": "Cart is empty"
        })

    order_id = len(ORDERS) + 1

    order = {
        "order_id": order_id,
        "items": CART.copy(),
        "status": "created"
    }

    ORDERS.append(order)
    CART.clear()

    return jsonify({
        "code": 200,
        "message": "Create order success",
        "data": order
    })


@app.route("/order/<int:order_id>", methods=["GET"])
def get_order_detail(order_id):
    """
    查询订单详情
    需要 token
    """
    if not check_token():
        return jsonify({
            "code": 401,
            "message": "Unauthorized"
        })

    for order in ORDERS:
        if order["order_id"] == order_id:
            return jsonify({
                "code": 200,
                "message": "success",
                "data": order
            })

    return jsonify({
        "code": 404,
        "message": "Order not found"
    })


@app.route("/reset", methods=["POST"])
def reset_data():
    """
    清理购物车和订单数据，避免测试用例之间互相影响
    """
    CART.clear()
    ORDERS.clear()

    return jsonify({
        "code": 200,
        "message": "reset success"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
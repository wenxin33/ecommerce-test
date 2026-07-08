class CartAPI:
    def __init__(self, client):
        self.client = client

    def add_to_cart(self, product_id=None, quantity=None):
        json_data = {}

        if product_id is not None:
            json_data["product_id"] = product_id

        if quantity is not None:
            json_data["quantity"] = quantity

        return self.client.post("/cart", json=json_data)

    def get_cart(self):
        return self.client.get("/cart")
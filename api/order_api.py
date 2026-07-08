class OrderAPI:
    def __init__(self, client):
        self.client = client

    def create_order(self):
        return self.client.post("/order")

    def get_order_detail(self, order_id):
        return self.client.get(f"/order/{order_id}")
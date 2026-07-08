class ProductAPI:
    def __init__(self, client):
        self.client = client

    def get_products(self):
        return self.client.get("/products")

    def get_product_detail(self, product_id):
        return self.client.get(f"/products/{product_id}")
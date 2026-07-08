# 把“HTTP请求”变成“业务动作”

class LoginAPI:
    def __init__(self, client):
        self.client = client

    def login(self, username, password):
        return self.client.post("/login", json={
            "username": username,
            "password": password
        })
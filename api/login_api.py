class LoginAPI:
    def __init__(self, client):
        self.client = client

    def login(self, username=None, password=None):
        json_data = {}

        if username is not None:
            json_data["username"] = username

        if password is not None:
            json_data["password"] = password

        return self.client.post("/login", json=json_data)
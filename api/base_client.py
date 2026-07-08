import requests

from utils.logger import get_logger


class BaseClient:
    def __init__(self, base_url="http://127.0.0.1:8000", token=None):
        self.base_url = base_url
        self.headers = {}
        self.logger = get_logger()

        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get(self, path, params=None):
        url = self.base_url + path

        self.logger.info(f"GET {url}")
        self.logger.info(f"PARAMS: {params}")
        self.logger.info(f"HEADERS: {self.headers}")

        response = requests.get(
            url,
            params=params,
            headers=self.headers,
            timeout=5
        )

        self.logger.info(f"STATUS_CODE: {response.status_code}")
        self.logger.info(f"RESPONSE: {response.text}")

        return response

    def post(self, path, json=None):
        url = self.base_url + path

        self.logger.info(f"POST {url}")
        self.logger.info(f"JSON: {json}")
        self.logger.info(f"HEADERS: {self.headers}")

        response = requests.post(
            url,
            json=json,
            headers=self.headers,
            timeout=5
        )

        self.logger.info(f"STATUS_CODE: {response.status_code}")
        self.logger.info(f"RESPONSE: {response.text}")

        return response

    def set_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"
        self.logger.info("Authorization token has been set.")
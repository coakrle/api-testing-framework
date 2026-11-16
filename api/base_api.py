
import requests
from utils.config import BASE_URL, API_KEY


class BaseAPI:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": API_KEY
        })
        self.timeout = 10

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout
        )

    def post(self, endpoint, data):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=self.timeout
        )

    def put(self, endpoint, data):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=self.timeout
        )

    def patch(self, endpoint, data):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=self.timeout
        )

    def delete(self, endpoint):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout
        )

    def close(self):
        self.session.close()

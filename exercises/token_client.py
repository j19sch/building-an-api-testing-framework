import requests
from . import api_client

class Token(api_client.ApiClient):
    def __init__(self):
        super().__init__()
        self.url = 'http://localhost:8000/token'

    def create_token(self, username):
        return self.post(f'{self.url}/{username}')

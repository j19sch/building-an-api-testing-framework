import requests
from . import api_client

class KnockKnock(api_client.ApiClient):
    def __init__(self):
        super().__init__()
        self.url = 'http://localhost:8000/knockknock'

    def knock(self):
        return self.get(self.url)

import requests

class Token:
    def __init__(self):
        self.url = 'http://localhost:8000/token'

    def create_token(self, username):
        return requests.post(f'{self.url}/{username}')

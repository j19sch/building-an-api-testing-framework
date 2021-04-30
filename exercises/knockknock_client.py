import requests

class KnockKnock:
    def __init__(self):
        self.url = 'http://localhost:8000/knockknock'

    def knock(self):
        return requests.get(self.url)

import falcon
import random
import string
from .data import CREDS


class Token(object):
    def __init__(self):
        self.creds = CREDS

    def on_post(self, req, resp, user):
        self.creds[user] = "".join(random.choice(string.ascii_letters) for _ in range(15))

        resp.media = {'token': self.creds[user]}
        resp.status = falcon.HTTP_201

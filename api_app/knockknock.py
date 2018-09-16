import falcon


class Collection(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_TEXT
        resp.body = "Who's there?"

        resp.status = falcon.HTTP_200

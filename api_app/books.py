import json
import falcon

from data import BOOKS


class Collection(object):
    def __init__(self):
        self.doc = BOOKS

    def on_get(self, req, resp):
        resp.body = json.dumps(self.doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    # def on_post(self, req, resp):
    #     self.doc['books'].append(req.book)
    #
    #     resp.body = json.dumps(self.doc, ensure_ascii=False)
    #     resp.status = falcon.HTTP_201


class Item(object):
    def __init__(self):
        self.doc = BOOKS

    def on_get(self, req, resp, book_id):
        requested_book = [book for book in self.doc if book['id'] == book_id][0]
        resp.body = json.dumps(requested_book, ensure_ascii=False)
        resp.status = falcon.HTTP_200

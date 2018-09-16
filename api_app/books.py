import uuid
import json
import falcon

from data import BOOKS


class Collection(object):
    def __init__(self):
        self.books = BOOKS

    def on_get(self, req, resp, book_id=None):
        if book_id:
            try:
                requested_book = [book for book in self.books if book['id'] == book_id][0]
            except IndexError:
                resp.status = falcon.HTTP_NOT_FOUND
            else:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(requested_book, ensure_ascii=False)
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(self.books, ensure_ascii=False)

    def on_post(self, req, resp):
        new_book = req.media
        new_book["id"] = str(uuid.uuid4())
        self.books.append(new_book)

        resp.body = json.dumps({"id": new_book["id"]}, ensure_ascii=False)
        resp.status = falcon.HTTP_201

    def on_delete(self, req, resp, book_id):
        self.books[:] = [book for book in self.books if book["id"] != book_id]
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp, book_id):
        updated_book = req.media
        updated_book['id'] = book_id

        self.books[:] = [updated_book if book['id'] == book_id else book for book in self.books]

        resp.body = json.dumps(updated_book, ensure_ascii=False)
        resp.status = falcon.HTTP_200

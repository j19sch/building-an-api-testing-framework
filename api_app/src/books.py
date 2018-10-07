import uuid
import falcon
from falcon.media.validators import jsonschema
from .schemas import book

from .data import BOOKS
from .hooks import validate_token, validate_uuid


class Books(object):
    def __init__(self):
        self.books = BOOKS

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = self.books

    @jsonschema.validate(book)
    def on_post(self, req, resp):
        new_book = req.media
        new_book["id"] = str(uuid.uuid4())
        self.books.append(new_book)

        resp.media = {"id": new_book["id"]}
        resp.status = falcon.HTTP_201


class Book(object):
    def __init__(self):
        self.books = BOOKS

    @falcon.before(validate_uuid)
    def on_get(self, req, resp, book_id):
        try:
            requested_book = [book for book in self.books if book['id'] == book_id][0]
        except IndexError:
            resp.status = falcon.HTTP_NOT_FOUND
        else:
            resp.status = falcon.HTTP_200
            resp.media = requested_book

    @falcon.before(validate_uuid)
    @falcon.before(validate_token)
    def on_delete(self, req, resp, book_id):
        if [book for book in self.books if book['id'] == book_id]:
            self.books[:] = [book for book in self.books if book["id"] != book_id]
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_NOT_FOUND

    @falcon.before(validate_uuid)
    @falcon.before(validate_token)
    @jsonschema.validate(book)
    def on_put(self, req, resp, book_id):
        updated_book = req.media
        updated_book['id'] = book_id

        if [book for book in self.books if book['id'] == book_id]:
            self.books[:] = [updated_book if book['id'] == book_id else book for book in self.books]
            resp.media = updated_book
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_NOT_FOUND

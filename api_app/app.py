import falcon

import books
import knockknock
import auth

api = application = falcon.API()


api.add_route('/knockknock', knockknock.Ping())

api.add_route('/books', books.Books())
api.add_route('/books/{book_id}', books.Books())

api.add_route('/token/{user}', auth.Auth())

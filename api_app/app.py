import falcon

import books
import knockknock

api = application = falcon.API()


api.add_route('/knockknock', knockknock.Collection())

api.add_route('/books', books.Collection())
api.add_route('/books/{book_id}', books.Collection())

import falcon

import books

api = application = falcon.API()

api.add_route('/books', books.Collection())
api.add_route('/books/{book_id}', books.Item())

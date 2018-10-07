import falcon

from api_app.src import knockknock, books, token

api = application = falcon.API()


api.add_route('/knockknock', knockknock.Ping())

api.add_route('/books', books.Books())
api.add_route('/books/{book_id}', books.Book())

api.add_route('/token/{user}', token.Token())

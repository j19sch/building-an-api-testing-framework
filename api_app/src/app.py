import falcon

from api_app.src import knockknock, books, token

app = falcon.App()


app.add_route('/knockknock', knockknock.Ping())

app.add_route('/books', books.Books())
app.add_route('/books/{book_id}', books.Book())

app.add_route('/token/{user}', token.Token())

import requests


class KnockKnock(object):
    def __init__(self):
        self.url = 'http://localhost:8000/knockknock'

    def get(self):
        return requests.get(self.url)


class Books(object):
    def __init__(self):
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return requests.get(self.url)

    def get_one(self, book_id):
        return requests.get(self.url + '/' + book_id)

    def post_book(self, new_book):
        return requests.post(self.url + '/books', json=new_book)


class Token(object):
    def __init__(self):
        self.url = self.endpoint = 'http://localhost:8000/token'

    def get_token(self, username):
        return requests.post(self.url + '/' + username)

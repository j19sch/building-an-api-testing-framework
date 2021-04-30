import requests

class Books:
    def __init__(self):
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return requests.get(self.url)

    def get_book(self, book_id):
        return requests.get(f'{self.url}/{book_id}')

    def add_book(self, new_book):
        return requests.post(self.url, json=new_book)

    def delete_book(self, book_id, user, token):
        return requests.delete(f'{self.url}/{book_id}', headers={'user': user, 'token': token})

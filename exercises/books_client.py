import requests
import logging
from . import api_client


class Books(api_client.ApiClient):
    def __init__(self):
        super().__init__()
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return self.get(self.url)

    def get_book(self, book_id):
        return self.get(f'{self.url}/{book_id}')

    def add_book(self, new_book):
        return self.post(self.url, json=new_book)

    def delete_book(self, book_id, user, token):
        return self.delete(f'{self.url}/{book_id}', headers={'user': user, 'token': token})

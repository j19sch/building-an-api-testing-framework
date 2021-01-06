import logging
import requests


class KnockKnock:
    def __init__(self):
        self.url = 'http://localhost:8000/knockknock'

    def knock(self):
        return requests.get(self.url)


class Books:
    def __init__(self):
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return requests.get(self.url)

    def get_one_book(self, book_id):
        return requests.get(f'{self.url}/{book_id}')

    def post_book(self, new_book):
        response = requests.post(self.url, json=new_book)

        logging.info(f"{response.request.method}: {response.request.url}")
        logging.info(f"headers: {response.request.headers}")
        logging.info(f"request body: {response.request.body}")

        logging.info(f"response status: {response.status_code}, elapsed: {response.elapsed.total_seconds()}s")
        logging.info(f"response body: {response.text}")

        return response

    def delete_book(self, book_id, user, token):
        return requests.delete(f'{self.url}/{book_id}', headers={'user': user, 'token': token})


class Token:
    def __init__(self):
        self.url = self.endpoint = 'http://localhost:8000/token'

    def create_token(self, username):
        return requests.post(f'{self.url}/{username}')

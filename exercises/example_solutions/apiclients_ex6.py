import logging
import requests


class ApiClient(requests.Session):
    def __init__(self):
        super().__init__()
        self.hooks['response'].append(self._log_details)

    @staticmethod
    def _log_details(response, *args, **kwargs):
        logging.info(f"{response.request.method}: {response.request.url}")
        logging.info(f"headers: {response.request.headers}")
        if response.request.body is not None:
            logging.info(f"request body: {response.request.body}")

        logging.info(f"response status: {response.status_code}, elapsed: {response.elapsed.total_seconds()}s")
        logging.info(f"headers: {response.headers}")
        if response.text != "":
            logging.info(f"response body: {response.text}")


class KnockKnock(ApiClient):
    def __init__(self):
        super().__init__()
        self.url = 'http://localhost:8000/knockknock'

    def knock(self):
        return self.get(self.url)


class Books(ApiClient):
    def __init__(self):
        super().__init__()
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return self.get(self.url)

    def get_one_book(self, book_id):
        return self.get(f'{self.url}/{book_id}')

    def post_book(self, new_book):
        return self.post(self.url, json=new_book)

    def delete_book(self, book_id, user, token):
        return self.delete(f'{self.url}/{book_id}', headers={'user': user, 'token': token})


class Token(ApiClient):
    def __init__(self):
        super().__init__()
        self.url = self.endpoint = 'http://localhost:8000/token'

    def create_token(self, username):
        return self.post(f'{self.url}/{username}')

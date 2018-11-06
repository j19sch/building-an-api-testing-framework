import datetime
import logging  # https://docs.python.org/2.7/library/logging.html and https://docs.python.org/3.7/library/logging.html
import pytest
import requests


class ApiClient(requests.Session):
    def __init__(self, api_name):
        super(ApiClient, self).__init__()
        self.hooks['response'].append(self._log_details)

        self.logger = logging.getLogger(api_name)
        self.logger.setLevel("INFO")

        if not self.logger.handlers:  # prevents multiple handlers resulting in duplicate log lines
            file_handler = logging.FileHandler('./%s.log' % datetime.datetime.now().strftime("%Y%m%dT%H%M%S"), mode='a')
            file_handler.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s %(levelname)s - %(name)s - %(message)s', "%H:%M:%S")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def _log_details(self, r, *args, **kwargs):
        self.logger.info("{}: {}".format(r.request.method, r.request.url))
        self.logger.info("headers: {}".format(r.request.headers))
        if r.request.body is not None:
            self.logger.info("request body: {}".format(r.request.body))

        self.logger.info("response status: {}, elapsed: {}s".format(r.status_code, r.elapsed.total_seconds()))
        self.logger.info("headers: {}".format(r.headers))
        if r.text != "":
            self.logger.info("response body: {}".format(r.text))


class BooksApi(ApiClient):
    def __init__(self):
        super(BooksApi, self).__init__(self.__class__.__name__)
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return self.get(self.url)

    def get_one_book(self, book_id):
        return self.get(self.url + '/' + book_id)

    def post_book(self, new_book):
        return self.post(self.url, json=new_book)

    def delete_book(self, book_id, user, token):
        return self.delete(self.url + '/' + book_id, headers={'user': user, 'token': token})


class TokenApi(ApiClient):
    def __init__(self):
        super(TokenApi, self).__init__(self.__class__.__name__)
        self.url = self.endpoint = 'http://localhost:8000/token'

    def get_token(self, username):
        return self.post(self.url + '/' + username)


@pytest.fixture
def books_api():
    return BooksApi()


@pytest.fixture
def creds():
    user = 'bob'
    token_api = TokenApi()
    response = token_api.get_token(user)
    token = response.json()['token']
    return user, token


@pytest.fixture
def new_book_id(books_api):
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = books_api.post_book(new_book)
    assert response.status_code == 201

    return response.json()['id']


def test_delete_book(books_api, creds, new_book_id):
    user, token = creds

    response = books_api.delete_book(new_book_id, user, token)
    assert response.status_code == 200

    response = books_api.get_one_book(new_book_id)
    assert response.status_code == 404

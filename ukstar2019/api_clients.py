import logging
import requests

BASE_URL = "http://localhost:8001"


class ApiClient(requests.Session):
    def __init__(self):
        super(ApiClient, self).__init__()
        self.hooks['response'].append(self._log_details)

    @staticmethod
    def _log_details(response, *args, **kwargs):
        logging.info("{}: {}".format(response.request.method, response.request.url))
        logging.info("headers: {}".format(response.request.headers))
        if response.request.body is not None:
            logging.info("request body: {}".format(response.request.body))

        logging.info("response status: {}, elapsed: {}s".format(response.status_code, response.elapsed.total_seconds()))
        logging.info("headers: {}".format(response.headers))
        if response.text != "":
            logging.info("response body: {}".format(response.text))


class KnockKnock(ApiClient):
    def __init__(self):
        super(KnockKnock, self).__init__()
        self.url = f"{BASE_URL}/knockknock"

    def knock(self):
        return self.get(self.url)


class Books(ApiClient):
    def __init__(self):
        super(Books, self).__init__()
        self.url = f"{BASE_URL}/books"

    def get_all_books(self):
        return self.get(self.url)

    def get_one_book(self, book_id):
        return self.get(self.url + '/' + book_id)

    def post_book(self, new_book):
        return self.post(self.url, json=new_book)

    def delete_book(self, book_id, user, token):
        return self.delete(self.url + '/' + book_id, headers={'user': user, 'token': token})

    def update_book(self, book_id, updated_book, user, token):
        return self.put(self.url + '/' + book_id, json=updated_book, headers={'user': user, 'token': token})


class Token(ApiClient):
    def __init__(self):
        super(Token, self).__init__()
        self.url = f"{BASE_URL}/token"

    def get_token(self, username):
        return self.post(self.url + '/' + username)

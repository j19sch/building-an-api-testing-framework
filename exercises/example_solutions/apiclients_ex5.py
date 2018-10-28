import logging
import requests


class ApiClient(requests.Session):
    def __init__(self):
        super(ApiClient, self).__init__()
        self.hooks['response'].append(self._log_details)

    @staticmethod
    def _log_details(r, *args, **kwargs):
        logging.info("{}: {}".format(r.request.method, r.request.url))
        logging.info("headers: {}".format(r.request.headers))
        if r.request.body is not None:
            logging.info("request body: {}".format(r.request.body))

        logging.info("response status: {}, elapsed: {}s".format(r.status_code, r.elapsed.total_seconds()))
        logging.info("headers: {}".format(r.headers))
        if r.text != "":
            logging.info("response body: {}".format(r.text))


class KnockKnock(ApiClient):
    def __init__(self):
        super(KnockKnock, self).__init__()
        self.url = 'http://localhost:8000/knockknock'

    def knock(self):
        return self.get(self.url)


class Books(ApiClient):
    def __init__(self):
        super(Books, self).__init__()
        self.url = 'http://localhost:8000/books'

    def get_all(self):
        return self.get(self.url)

    def get_one_book(self, book_id):
        return self.get(self.url + '/' + book_id)

    def post_book(self, new_book):
        return self.post(self.url, json=new_book)

    def delete_book(self, book_id, user, token):
        return self.delete(self.url + '/' + book_id, headers={'user': user, 'token': token})


class Token(ApiClient):
    def __init__(self):
        super(Token, self).__init__()
        self.url = self.endpoint = 'http://localhost:8000/token'

    def get_token(self, username):
        return self.post(self.url + '/' + username)

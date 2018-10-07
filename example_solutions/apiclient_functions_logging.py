import logging
import requests

_BASE_URL = 'http://localhost:8000'


# part of exercise 5
def _log_details(r, *args, **kwargs):
    logging.info("{}: {}".format(r.request.method, r.request.url))
    logging.info("headers: {}".format(r.request.headers))
    if r.request.body is not None:
        logging.info("request body: {}".format(r.request.body))

    logging.info("response status: {}, elapsed: {}s".format(r.status_code, r.elapsed.total_seconds()))
    logging.info("headers: {}".format(r.headers))
    if r.text != "":
        logging.info("response body: {}".format(r.text))


def knockknock():
    return requests.get(_BASE_URL + '/knockknock', hooks={'response': _log_details})


def get_all_books():
    return requests.get(_BASE_URL + '/books', hooks={'response': _log_details})


def get_one_book(book_id):
    return requests.get(_BASE_URL + '/books' + '/' + book_id, hooks={'response': _log_details})


def post_book(new_book):
    return requests.post(_BASE_URL + '/books', json=new_book, hooks={'response': _log_details})


def get_token(username):
    return requests.post(_BASE_URL + '/token' + '/' + username, hooks={'response': _log_details})


# part of exercise 4
def delete_book(book_id, user, token):
    return requests.delete(_BASE_URL + '/books' + '/' + book_id, headers={'user': user, 'token': token}, hooks={'response': _log_details})

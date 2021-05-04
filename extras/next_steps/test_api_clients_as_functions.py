import logging

import pytest
import requests

"""
Functions instead of class
for logging: HTTP action functions match signature with requests library functions
for api clients: one file per API importing the api functions

Sessions class
create class that inherits from session and sets these in its __init__()
stream=stream, verify=verify, proxies=proxies, cert=cert, timeout=timeout

Prepared requests
https://docs.python-requests.org/en/master/user/advanced/#prepared-requests

Disadvantage: requests.Session is faster when it maintains the sessions
https://docs.python-requests.org/en/master/user/advanced/#session-objects
The Session object allows you to persist certain parameters across requests. It also
persists cookies across all requests made from the Session instance, and will use
urllib3’s connection pooling. So if you’re making several requests to the same host,
the underlying TCP connection will be reused, which can result in a significant per-
formance increase (see HTTP persistent connection).
"""


def get(url, params=None, **kwargs):
    request = requests.Request('GET', url=url, params=params, **kwargs)
    prepared_request = request.prepare()

    logging.info(f"{prepared_request.method}: {prepared_request.url}")
    logging.info(prepared_request.body)

    with requests.Session() as session:
        response = session.send(prepared_request)

    logging.info(f"status {response.status_code}, reason: {response.reason}")
    logging.info(f"{response.text}")
    return response


def post(url, data=None, json=None, **kwargs):
    request = requests.Request('POST', url, data=data, json=json, **kwargs)
    prepared_request = request.prepare()

    logging.info(f"{prepared_request.method}: {prepared_request.url}")
    logging.info(prepared_request.body)

    with requests.Session() as session:
        response = session.send(prepared_request)

    logging.info(f"status {response.status_code}, reason: {response.reason}")
    logging.info(f"{response.text}")
    return response


def delete(url, **kwargs):
    request = requests.Request('DELETE', url, **kwargs)
    prepared_request = request.prepare()

    logging.info(f"{prepared_request.method}: {prepared_request.url}")
    logging.info(prepared_request.body)

    with requests.Session() as session:
        response = session.send(prepared_request)

    logging.info(f"status {response.status_code}, reason: {response.reason}")
    logging.info(f"{response.text}")
    return response


BASE_URL = "http://localhost:8000"


# Token API
TOKEN_API = f"{BASE_URL}/token"


def post_token(user):
    return post(f"{TOKEN_API}/{user}")


# Books API
BOOKS_API = f"{BASE_URL}/books"


def post_book(new_book):
    return post(BOOKS_API, json=new_book)


def get_one_book(book_id):
    return get(f'{BOOKS_API}/{book_id}')


def delete_book(book_id, user, token):
    return delete(f'{BOOKS_API}/{book_id}', headers={'user': user, 'token': token})


@pytest.fixture
def creds():
    user = 'bob'
    response = post_token(user)
    token = response.json()['token']
    return user, token


@pytest.fixture
def new_book_id():
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = post_book(new_book)
    assert response.status_code == 201

    return response.json()['id']


def test_delete_book(creds, new_book_id):
    user, token = creds

    response = delete_book(new_book_id, user, token)
    assert response.status_code == 200

    response = get_one_book(new_book_id)
    assert response.status_code == 404

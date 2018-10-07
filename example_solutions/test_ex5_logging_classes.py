import pytest

from . import apiclient_classes_logging


@pytest.fixture()
def creds():
    user = 'bob'
    token_api = apiclient_classes_logging.Token()
    response = token_api.get_token(user)
    token = response.json()['token']
    return user, token


@pytest.fixture()
def new_book_id():
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    books_api = apiclient_classes_logging.Books()
    response = books_api.post_book(new_book)
    assert response.status_code == 201

    return response.json()['id']


def test_delete_book(new_book_id, creds):
    user, token = creds
    books_api = apiclient_classes_logging.Books()

    response = books_api.delete_book(new_book_id, user, token)
    assert response.status_code == 200

    response = books_api.get_one_book(new_book_id)
    assert response.status_code == 404

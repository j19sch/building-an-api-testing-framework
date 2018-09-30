import pytest

from . import apiclient_functions


@pytest.fixture()
def creds():
    user = 'bob'
    response = apiclient_functions.get_token(user)
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

    response = apiclient_functions.post_book(new_book)
    assert response.status_code == 201

    return response.json()['id']


def test_delete_book(new_book_id, creds):
    user, token = creds

    response = apiclient_functions.delete_book(new_book_id, user, token)
    assert response.status_code == 200

    response = apiclient_functions.get_one_book(new_book_id)
    assert response.status_code == 404

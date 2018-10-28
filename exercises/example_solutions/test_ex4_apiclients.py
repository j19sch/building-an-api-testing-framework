import pytest

from . import apiclients_ex4


@pytest.fixture
def books_api():
    return apiclients_ex4.Books()


@pytest.fixture
def creds():
    user = 'bob'
    token_api = apiclients_ex4.Token()
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

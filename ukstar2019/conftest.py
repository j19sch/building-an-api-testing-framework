import pytest

from ukstar2019 import api_clients
from api_app.src.data import BOOKS


@pytest.fixture
def knockknock_api():
    return api_clients.KnockKnock()


@pytest.fixture
def books_api():
    return api_clients.Books()


@pytest.fixture
def token_api():
    return api_clients.Token()


@pytest.fixture(scope="session")
def initial_books():
    books = BOOKS.copy()
    return books


@pytest.fixture
def creds(token_api):
    user = 'bob'
    response = token_api.get_token(user)
    token = response.json()['token']
    return user, token


@pytest.fixture
def new_book(books_api):
    new_book = {
        "author": "Nicole Forsgren, Jez Humble, Gene Kim",
        "pages": 257,
        "publisher": "IT Revolution",
        "sub_title": "Building and scaling high performing technology organizations",
        "title": "Accelerate",
        "year": 2018
    }

    response = books_api.post_book(new_book)
    assert response.status_code == 201

    new_book['id'] = response.json()['id']

    return new_book

import pytest
import requests


# The fixture below will create a new book, then yield the new_book dictionary to the test.
# Once the test has run, the remainder of the function is executed, removing the book again.
# This will happen regardless of the outcome of the test itself (pass, fail, error).
#
# Docs: https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code


@pytest.fixture
def new_book():
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = requests.post('http://localhost:8000/books', json=new_book)
    assert response.status_code == 201

    new_book['id'] = response.json()['id']

    yield new_book

    user = 'bob'
    response = requests.post(f'http://localhost:8000/token/{user}')
    token = response.json()['token']
    response = requests.delete(f'http://localhost:8000/books/{new_book["id"]}',
                               headers={'user': user, 'token': token})
    assert response.status_code == 200


def test_get_one_book(new_book):
    response = requests.get(f'http://localhost:8000/books/{new_book["id"]}')
    assert response.status_code == 200
    assert response.json() == new_book

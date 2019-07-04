import pytest
import requests


@pytest.fixture(scope="session")
def creds():
    user = 'bob'
    response = requests.post('http://localhost:8000/token/' + user)
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

    response = requests.post('http://localhost:8000/books', json=new_book)
    assert response.status_code == 201

    return response.json()['id']


def test_delete_book(new_book_id, creds):
    user, token = creds

    response = requests.delete('http://localhost:8000/books/' + new_book_id, headers={'user': user, 'token': token})
    assert response.status_code == 200

    response = requests.get('http://localhost:8000/books/' + new_book_id)
    assert response.status_code == 404

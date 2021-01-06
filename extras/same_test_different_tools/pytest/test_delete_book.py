import pytest
import requests


@pytest.fixture()
def books():
    books = requests.get('http://localhost:8000/books').json()
    return books


@pytest.fixture()
def creds():
    user = 'user'
    token = requests.post('http://localhost:8000/token/user').json()['token']
    return user, token


def test_delete_book(books, creds):
    book_to_delete = books[0]
    user, token = creds

    response = requests.delete(f'http://localhost:8000/books/{book_to_delete["id"]}',
                               headers={'user': user, 'token': token})
    assert response.status_code == 200

    response = requests.get(f'http://localhost:8000/books/{book_to_delete["id"]}')
    assert response.status_code == 404

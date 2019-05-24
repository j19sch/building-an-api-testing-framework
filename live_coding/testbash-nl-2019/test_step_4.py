import requests
import pytest

URL = 'http://localhost:8000'


class BooksApi():
	def __init__(self):
		self.url = f'{URL}/books'

	def add_new_book(self, new_book):
		return requests.post(self.url, json=new_book)

@pytest.fixture
def books_api():
	return BooksApi()

@pytest.fixture
def new_book_id(books_api):
	new_book = {
    "author": "Ray Monk", 
    "pages": 110, 
    "publisher": "Granta Books, London", 
    "sub_title": None, 
    "title": "How to read Wittgenstein", 
    "year": 2005
	}

	response = books_api.add_new_book(new_book)
	book_id = response.json()['id']

	return book_id

@pytest.fixture(scope='session')
def user_and_token():
	user = 'testbash'
	response = requests.post(f'{URL}/token/{user}')
	token = response.json()['token']

	return user, token	


def test_delete_book(new_book_id, user_and_token):
	user, token = user_and_token

	response = requests.delete(f'{URL}/books/{new_book_id}',
		headers={'user': user, 'token': token})

	assert response.status_code == 200
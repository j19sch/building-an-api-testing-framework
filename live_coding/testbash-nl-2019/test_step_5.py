import requests
import pytest
import logging

URL = 'http://localhost:8000'


class BooksApi(requests.Session):
	def __init__(self):
		super().__init__()
		self.url = f'{URL}/books'
		self.hooks['response'].append(self._log_stuff)

	def add_new_book(self, new_book):
		return self.post(self.url, json=new_book)

	@staticmethod  # Why it went wrong at TestBash
	def _log_stuff(response, *args, **kwargs):
		logging.info("oops sorry")
		logging.info(response.request.url)
		logging.info(response.request.method)
		logging.info(response.request.body)
		logging.info(response.status_code)
		logging.info(response.text)

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
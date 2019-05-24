# step 2 - pytest

import requests
from pprint import pprint

URL = 'http://localhost:8000'


def test_knockknock():
	response = requests.get(f'{URL}/knockknock')
	print(response.status_code)
	print(response.text)

	assert response.status_code == 201

def test_get_all_books():
	response = requests.get(f'{URL}/books')
	print(response.status_code)
	pprint(response.json())
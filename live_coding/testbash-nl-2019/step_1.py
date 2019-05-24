# step 1

import requests
from pprint import pprint

URL = 'http://localhost:8000'


response = requests.get(f'{URL}/knockknock')
print(response.status_code)
print(response.text)

assert response.status_code == 201

response = requests.get(f'{URL}/books')
print(response.status_code)
pprint(response.json())
import requests
from pprint import pformat

response = requests.get('http://localhost:8000/books')
print("\n")
print(response.status_code)
print(pformat(response.headers))
print(pformat(response.text))
print(pformat(response.json()))

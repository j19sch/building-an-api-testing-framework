import requests

response = requests.get('http://localhost:8000/images')
print(response.__dict__)
print("\n")
print(response.status_code)
print(response.headers)
print(response.text)

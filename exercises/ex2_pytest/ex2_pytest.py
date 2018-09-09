import requests


def test_get_all_books_success():
    response = requests.get('http://localhost:8000/books')

    assert response.status_code == 200
    assert response.json()[0]["id"] == "9b30d321-d242-444f-b2db-884d04a4d806"


def test_get_all_books_fails():
    response = requests.get('http://localhost:8000/books')

    assert response.status_code == 200
    assert response.json()[0]["id"] == "9b30d321-d242-444f-b2db-not-a-uuid"

import pytest  # https://docs.pytest.org/en/latest/parametrize.html
import requests


@pytest.mark.parametrize("invalid_book_id", [
    "1",
    "aaaa",
    "11d399cb-5a44-430c-bb9d-51fa3dab986",  # last character missing
    "h1d399cb-5a44-430c-bb9d-51fa3dab9864"  # h at start makes uuid invalid
])
def test_get_invalid_book_id(invalid_book_id):
    response = requests.get('http://localhost:8000/books/' + invalid_book_id)
    assert response.status_code == 400
    assert response.json()['title'] == '400 Bad Request'
    assert response.json()['description'] == 'Not a valid uuid.'

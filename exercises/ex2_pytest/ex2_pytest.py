import requests


def test_get():
    response = requests.get('http://localhost:8000/images')

    assert response.status_code == 200
    assert response.json()["images"][0]["href"] == "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.pngz"

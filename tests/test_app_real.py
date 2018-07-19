import requests


def test_list_images():
    response = requests.get("http://localhost:8000/images")

    print response.text

    assert response.status_code == 200
    assert response.text == '{"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}]}'



def test_post_image():
    response = requests.post("http://localhost:8000/images", json={"foo": "bar"})

    print response.text

    assert response.status_code == 201
    assert response.text == '{"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}, {"foo": "bar"}]}'

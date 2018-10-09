import requests


def test_knockknock():
    response = requests.get('http://localhost:8000/knockknock')
    assert response.status_code == 200
    assert response.text == "Who's there?"


def test_get_all_books():
    response = requests.get('http://localhost:8000/books')
    assert response.status_code == 200
    books = response.json()
    assert books is not None
    assert len(books) == 5


def test_get_one_book():
    response = requests.get('http://localhost:8000/books/8b91b84b-04e4-4496-9635-66468c2f3e41')
    assert response.status_code == 200
    assert response.json() == {
        'id': '8b91b84b-04e4-4496-9635-66468c2f3e41',
        'title': 'Against Method',
        'sub_title': None,
        'author': 'Paul Feyerabend',
        'publisher': 'Verso',
        'year': 2010,
        'pages': 296
    }


def test_post_new_book():
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = requests.post('http://localhost:8000/books', json=new_book)
    assert response.status_code == 201
    assert response.json()['id'] is not None


def test_get_token_for_user():
    response = requests.post('http://localhost:8000/token/alice')
    print(response.status_code, response.json())
    assert response.status_code == 201
    assert response.json()['token'] is not None

import requests
import pytest

class TestKnockknockApi:
    @pytest.fixture
    def fixture(self):
        return requests.get('http://localhost:8000/knockknock')

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_response_is_correct(self, fixture):
        assert fixture.text == 'Who\'s there?'

class TestBooksApi:
    @pytest.fixture
    def fixture(self):
        return requests.get('http://localhost:8000/books')

    @pytest.fixture
    def post_fixture(self):
        payload = {
            'title': 'New book',
            'sub_title': 'New book sub title',
            'author': 'Dmytro Titenko',
            'publisher': 'Mendix',
            'year': 2021,
            'pages': 53
        }
        response = requests.post('http://localhost:8000/books', json=payload)
        response_body = response.json()
        
        assert response_body is not None
        assert response_body["id"] is not None

        return (response, response_body)

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_books_contains_the_book(self, fixture):
        response_body = fixture.json()
        assert response_body[0]['id'] == '9b30d321-d242-444f-b2db-884d04a4d806'

    def test_book_store_request_is_successful(self, post_fixture):
        response, _ = post_fixture
        assert response.status_code == 201

    def test_book_is_stored(self, post_fixture):
        _, response_body = post_fixture

        respponse = requests.get(f'http://localhost:8000/books/{response_body["id"]}')
        response_body = respponse.json()
        assert response_body is not None
        assert response_body["title"] == 'New book'

class TestBookApi:
    @pytest.fixture
    def fixture(self):
        return requests.get('http://localhost:8000/books/9b30d321-d242-444f-b2db-884d04a4d806')

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_book_has_correct_title(self, fixture):
        response_body = fixture.json()
        assert response_body['title'] == 'Perfect Software And Other Illusions About Testing'

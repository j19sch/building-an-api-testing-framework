import requests
import pytest

class TestBookApi:
    @pytest.fixture
    def fixture(self):
        return requests.get('http://localhost:8000/books/9b30d321-d242-444f-b2db-884d04a4d806')

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_book_has_correct_title(self, fixture):
        response_body = fixture.json()
        assert response_body['title'] == 'Perfect Software And Other Illusions About Testing'

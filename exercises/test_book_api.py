import pytest
from . import books_client

class TestBookApi:
    @pytest.fixture(scope="class")
    def fixture(self):
        client = books_client.Books()
        return client.get_book('9b30d321-d242-444f-b2db-884d04a4d806')

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_book_has_correct_title(self, fixture):
        response_body = fixture.json()
        assert response_body['title'] == 'Perfect Software And Other Illusions About Testing'

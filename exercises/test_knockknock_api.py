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

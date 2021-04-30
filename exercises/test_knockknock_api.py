import pytest
from . import knockknock_client

class TestKnockknockApi:
    @pytest.fixture(scope="class")
    def fixture(self):
        client = knockknock_client.KnockKnock()
        return client.knock()

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_response_is_correct(self, fixture):
        assert fixture.text == 'Who\'s there?'

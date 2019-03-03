def test_knockknock(knockknock_api):
    response = knockknock_api.knock()

    assert response.status_code == 200
    assert response.text == "Who's there?"

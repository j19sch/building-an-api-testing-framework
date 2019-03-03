def test_post_auth(token_api):
    response = token_api.get_token("user01")

    assert response.status_code == 201
    assert 'token' in response.json().keys()

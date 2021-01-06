import pytest  #
import requests


# The @pytest.mark.parametrize decorator allows you to run the same test with different data.
# The example below illustrates the simples usage: different inputs expected to result in the same output.
# Since the decorator accepts multiple arguments, you can also for instance provide pairs of expected input
# and expected output. This allows you to test these inputs and outputs without having to duplicate code.
# Finally, by stacking parametrize decorators you can test all combinations of the arguments in the separate decorators.
#
# Docs: https://docs.pytest.org/en/latest/parametrize.html


@pytest.mark.parametrize("invalid_book_id", [
    "1",
    "aaaa",
    "11d399cb-5a44-430c-bb9d-51fa3dab986",  # last character missing
    "h1d399cb-5a44-430c-bb9d-51fa3dab9864"  # h at start makes uuid invalid
])
def test_get_invalid_book_id(invalid_book_id):
    response = requests.get(f'http://localhost:8000/books/{invalid_book_id}')
    assert response.status_code == 400
    assert response.json()['title'] == '400 Bad Request'
    assert response.json()['description'] == 'Not a valid uuid.'

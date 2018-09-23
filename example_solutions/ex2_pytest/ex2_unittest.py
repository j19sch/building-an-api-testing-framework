import requests
import unittest


class TestImagesApi(unittest.TestCase):

    def test_get_all_books_success(self):
        response = requests.get('http://localhost:8000/books')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["id"], "9b30d321-d242-444f-b2db-884d04a4d806")

    def test_get_all_books_fail(self):
        response = requests.get('http://localhost:8000/books')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["id"], "9b30d321-d242-444f-b2db-not-a-uuid")


if __name__ == '__main__':
    unittest.main()

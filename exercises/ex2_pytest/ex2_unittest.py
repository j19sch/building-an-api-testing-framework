import requests
import unittest


class TestImagesApi(unittest.TestCase):

    def test_get_1(self):
        response = requests.get('http://localhost:8000/images')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["images"][0]["href"], "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.pngz")


if __name__ == '__main__':
    unittest.main()

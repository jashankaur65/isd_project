import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("Susan", "Clark", "susanclark@pixell.com", 1010)

    def test_email_valid(self):
        self.assertEqual(self.client.get_email(), "susanclark@pixell.com")

    def test_email_invalid(self):
        with self.assertRaises(ValueError):
            Client("John", "Doe", "invalidemail", 1001)

    def test_str(self):
        expected = "Clark, Susan [1010] - susanclark@pixell.com"
        self.assertEqual(str(self.client), expected)


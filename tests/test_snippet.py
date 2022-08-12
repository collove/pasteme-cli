import unittest

from pasteme_cli.constants import PASTEME_API_URL
from pasteme_cli.sdk.pasteme import Snippet


class SnippetTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sample = {
            'title': 'Paste Title',
            'body': 'print("Hello")',
            'language': 'bash',
            'theme': 'default',
            'expiry_time': '7',
        }

    # TODO: Using mocks
    def test_push_snippet(self):
        response = Snippet(**self.sample).push(PASTEME_API_URL)
        self.assertEqual(response.status_code, 201)
        self.assertIn('url', response.json().keys())


if __name__ == '__main__':
    unittest.main()

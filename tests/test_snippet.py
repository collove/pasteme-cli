import unittest

from src.pasteme_cli.constants import PASTEME_SERVICE_URL
from src.pasteme_cli.sdk.pasteme import PasteMe


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
        resp = PasteMe().create(**self.sample)
        self.assertIn(PASTEME_SERVICE_URL, resp.url)


if __name__ == '__main__':
    unittest.main()

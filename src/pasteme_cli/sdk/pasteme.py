import json

import requests
from pygments import formatters
from pygments import highlight
from pygments import lexers

JSON_TEMPLATE = '''-> {}
{}'''

class Snippet:

    def __init__(self, title, body, language, theme) -> None:
        self.snippet = {
            'title': title,
            'body': body,
            'language': language,
            'theme': theme,
        }

    def push(self, url, is_verbose=False) -> requests.Response:
        response = requests.post(
            url=url,
            data=self.snippet
        )
        
        if is_verbose:
            response_json = response.json()
            sent_data = highlight(
                json.dumps(self.snippet, indent=3),
                lexers.JsonLexer(),
                formatters.TerminalFormatter()
            )
            response_data = highlight(
                json.dumps(response_json, indent=3),
                lexers.JsonLexer(),
                formatters.TerminalFormatter()
            )
            print(JSON_TEMPLATE.format('Posted Data', sent_data))
            print(JSON_TEMPLATE.format('Returned Payload', response_data))
        
        return response
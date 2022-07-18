import json

import requests
from pygments import formatters
from pygments import highlight
from pygments import lexers

JSON_TEMPLATE = '''-> {}
{}'''

class Snippet:

    def __init__(self, title, body, language) -> None:
        self.snippet = {
            'title': title,
            'body': body,
            'language': language,
        }
    
    def push(self, url, is_verbose=False) -> requests.Response:
        response = requests.post(
            url=url,
            data=self.snippet
        ).json()
        
        if is_verbose:
            sent_data = highlight(
                json.dumps(self.snippet, indent=3),
                lexers.JsonLexer(),
                formatters.TerminalFormatter()
            )
            response_data = highlight(
                json.dumps(response, indent=3),
                lexers.JsonLexer(),
                formatters.TerminalFormatter()
            )
            print(JSON_TEMPLATE.format('Posted Data', sent_data))
            print(JSON_TEMPLATE.format('Returned Payload', response_data))
        
        return response
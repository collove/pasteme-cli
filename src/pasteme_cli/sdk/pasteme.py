import json
from typing import ClassVar
from urllib.parse import urljoin

import requests
from pygments import formatters, highlight, lexers

from ..constants import PASTEME_SERVICE_URL
from .types import APIResponse

JSON_TEMPLATE = '''-> {}
{}'''


class PasteMe:
    BASE_URL: ClassVar[str] = PASTEME_SERVICE_URL
    API_URL: ClassVar[str] = urljoin(BASE_URL, "/api/v1/paste/")

    def __init__(self, verbose: bool = False) -> None:
        self.verbose = verbose

    def create(self, **context) -> APIResponse:
        response = requests.post(self.API_URL, data=context)

        if self.verbose:
            response_json = response.json()
            sent_data = highlight(
                json.dumps(context, indent=3),
                lexers.JsonLexer(),
                formatters.TerminalFormatter(),
            )
            response_data = highlight(
                json.dumps(response_json, indent=3),
                lexers.JsonLexer(),
                formatters.TerminalFormatter(),
            )
            print(JSON_TEMPLATE.format('Posted Data', sent_data))
            print(JSON_TEMPLATE.format('Returned Payload', response_data))

        return APIResponse(**response.json())

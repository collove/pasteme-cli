"""Types representing API responses from PasteMe."""
from dataclasses import dataclass


@dataclass
class APIResponse:
    id: str
    title: str
    body: str
    language: str
    theme: str
    expires_in: str
    url: str

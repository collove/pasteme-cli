"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mpasteme_cli` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``pasteme_cli.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``pasteme_cli.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import json
import sys

import requests
from requests.exceptions import ConnectionError

from .constants import CONNECTION_ISSUE_HINT
from .constants import JSON_TEMPLATE
from .constants import LANGUAGES
from .constants import LANGUAGES_HINT
from .constants import PASTEME_API_URL
from .constants import PASTEME_SERVICE_URL

parser = argparse.ArgumentParser(description=f'A CLI pastebin tool interacting with PasteMe ({PASTEME_SERVICE_URL}) RESTful service.')
parser.add_argument(
	'-t', '--title',
	metavar='',
	default='Untitled',
	type=str,
	help='title/description of snippet',
)
parser.add_argument(
	'-l', '--language',
	metavar='',
	default='plaintext',
	type=str,
	help=LANGUAGES_HINT,
)
parser.add_argument(
    "-v", "--verbose",
	action = "store_true",
    help="verbosity for post data and response",
)
parser.add_argument(
	'body',
	metavar='code',
	type=str,
	help='snippet body (code)',
)

def main(args=None):
	args = parser.parse_args(args=args)
 
	if language_is_valid(args.language):
		context = {
			'title': args.title,
			'body': args.body,
			'language': args.language,
		}
	else:
		sys.exit(f'Language {args.language} is not valid! Check out "pasteme --help" for supported languages.')

	try:
		response = requests.post(
			url=PASTEME_API_URL,
			data=context
		).json()
  
		if args.verbose:
			print(
       			JSON_TEMPLATE.format(
              		'REQUEST',
              		json.dumps(context, indent=3)
                )
            )
			print(
       			JSON_TEMPLATE.format(
              		'RESPONSE',
              		json.dumps(response, indent=3)
                )
            )

		sys.exit(f'PASTE --> {response["url"]}')
	except ConnectionError:
		sys.exit(CONNECTION_ISSUE_HINT)

	# TODO: finding a way reading the code/file from the user (maybe file only)
	# like: pasteme -f file.py -L 120:132


def language_is_valid(lang) -> bool:
    return lang in LANGUAGES.keys()
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
import sys

from requests.exceptions import ConnectionError

from pasteme_cli.sdk import Snippet

from .constants import CONNECTION_ISSUE_HINT
from .constants import EPILOG_DESCRIPTION
from .constants import LANGUAGES
from .constants import LANGUAGES_HINT
from .constants import PASTEME_API_URL
from .constants import PASTEME_SERVICE_URL
from .constants import THEMES
from .constants import THEMES_HINT

parser = argparse.ArgumentParser(
    description=f'A CLI pastebin tool interacting with PasteMe ({PASTEME_SERVICE_URL}) RESTful APIs.',
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
	'-t', '--title',
	metavar='',
	type=str,
	help='title/description of snippet',
)
parser.add_argument(
	'-l', '--language',
	metavar='',
	default='plaintext',
	type=str,
	choices=LANGUAGES.keys(),
	help=LANGUAGES_HINT,
)
parser.add_argument(
	'-T', '--theme',
	metavar='',
	default='default',
	type=str,
	choices=THEMES.keys(),
	help=THEMES_HINT,
)
parser.add_argument(
    "-v", "--verbose",
	action = "store_true",
    help="verbosity for post data and response",
)
parser.add_argument(
	'-s', '--start',
	metavar='',
	type=int,
	default=1,
	help='select lines from (default: first line of the file)',
)
parser.add_argument(
	'-e', '--end',
	metavar='',
	type=int,
	help='select lines till (default: end of the file)',
)
parser.add_argument(
	'file',
	type=open,
	help='script file',
)

def main(args=None):
	args = parser.parse_args(args=args)

	with args.file as source_code:
		code_lines = source_code.readlines()

	args.end = args.end if args.end else len(code_lines)

	code_lines = code_lines[int(args.start)-1:int(args.end)]
 
	if not code_lines:
		sys.exit(f'Make sure ({args.start}-{args.end}) range is available in your source code file.')

	context = {
		'title': args.title,
		'body': ''.join(code_lines),
		'language': args.language,
		'theme': args.theme,
	}
 
	try:
		snippet = Snippet(**context)
		context = snippet.push(PASTEME_API_URL, args.verbose).json()
		print(f'PASTE --> {context["url"]}')
		sys.exit()
	except ConnectionError:
		sys.exit(CONNECTION_ISSUE_HINT)

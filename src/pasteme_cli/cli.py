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
import fileinput

import requests

from .constants import LANGUAGES, PASTEME_SERVICE_URL

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
	help='language of snippet/file',
)


def main(args=None):
	args = parser.parse_args(args=args)

	# TODO: writing the main functionality of POST
	# and GET requests.

	# TODO: also finding a better solution for reading
	# from the standard input channel.
	# sys.exit()

	pass
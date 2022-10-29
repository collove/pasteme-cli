``pasteme-cli`` Python Package
------------------------------

`PasteMe <https://github.com/collove/pasteme>`__ is a RESTful pastebin
service. Install this CLI tool and paste right from your command-line
interface.

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pasteme-cli/badge/?style=flat
    :target: https://pasteme-cli.readthedocs.io/
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/pasteme-cli.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pasteme-cli

.. |wheel| image:: https://img.shields.io/pypi/wheel/pasteme-cli.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pasteme-cli

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pasteme-cli.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pasteme-cli

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pasteme-cli.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pasteme-cli

.. |commits-since| image:: https://img.shields.io/github/commits-since/collove/pasteme-cli/v1.0.6.svg
    :alt: Commits since latest release
    :target: https://github.com/collove/pasteme-cli/compare/v1.0.6...main

Setup & Installation
~~~~~~~~~~~~~~~~~~~~

Since PasteMe provides API endpoints, you can install the following
Python package and paste your source codes and code snippets using your
CLIs or Terminals.

.. code:: sh

   $ pip install pasteme-cli

Usage
~~~~~

.. code:: sh

   $ pasteme [OPTIONS] file.py
   PASTE -> <URL>

To paste with the following attributes, run the command with the specified options and values.

.. code:: sh

   title       ->  "Here is the Title" (default: Untitled)
   line_start  ->  20 (default: First line)
   line_end    ->  35 (defalut: Last line)
   language    ->  C++ (default: PlainText)
   expires at  ->  One month (default: One week)

.. code:: sh

   $ pasteme --start 20 --end 35 --title "Here is the Title" --language cpp -x 1m program.cpp

You will have your 15 lines of code highlighted in C++ ready to share. Also visit the manual by typing ``$ pasteme --help`` and you have more
hints on the options and arguments.

License
~~~~~~~

PasteMe is being licensed under the `MIT
License <https://github.com/collove/pasteme/blob/main/LICENSE>`__.

Special Thanks to
~~~~~~~~~~~~~~~~~

-  `Hashnode <https://hashnode.com/>`__
-  `PlanetScale <https://planetscale.com/>`__

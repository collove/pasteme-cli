``pasteme-cli`` Python Package
------------------------------

`PasteMe <https://github.com/collove/pasteme>`__ is a RESTful pastebin
service. Install this CLI tool and paste right from your command-line
interface.

Setup & Installation
~~~~~~~~~~~~~~~~~~~~

Since PasteMe provides API endpoints, you can install the following
Python package and paste your source codes and code snippets using your
CLIs or Terminals.

.. code:: shell

   $ pip install pasteme-cli

Usage
~~~~~

.. code:: shell

   $ pasteme [OPTIONS] file.py
   PASTE -> <URL>

To paste with the following attributes, run the command with the specified options and values.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   title="Here is the Title"
   paste_from=20
   paste_till=35
   language=C++

.. code:: shell

   $ pasteme --start 20 --end 35 --title "Here is the Title" --language cpp program.cpp

Also visit the manual by typing ``$ pasteme --help`` and you have more
hints on the options and arguments.

License
~~~~~~~

PasteMe is being licensed under the `MIT
License <https://github.com/collove/pasteme/blob/main/LICENSE>`__.

Special Thanks to
~~~~~~~~~~~~~~~~~

-  `Hashnode <https://hashnode.com/>`__
-  `PlanetScale <https://planetscale.com/>`__

========
Overview
========

.. start-badges

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/collove/pasteme-cli/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/collove/pasteme-cli/compare/v0.0.2...main



.. end-badges

A CLI pastebin tool.

* Free software: MIT license

Installation
============

::

    pip install pasteme-cli

You can also install the in-development version with::

    pip install https://github.com/collove/pasteme-cli/archive/main.zip


Documentation
=============


https://pasteme-cli.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

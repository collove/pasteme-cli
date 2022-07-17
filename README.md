## `pasteme-cli` Python Package
[PasteMe](https://github.com/collove/pasteme) is a RESTful pastebin service. Install this CLI tool and paste right from your command-line interface.

### Setup & Installation
Since PasteMe provides API endpoints, you can install the following Python package and paste your source codes and code snippets using your CLIs or Terminals.

```shell
$ pip install pasteme-cli
```

### Usage

```shell
$ pasteme [OPTIONS] file.py
PASTE -> <URL>
```

#### To paste with the following attributes, run the command with the specified options and values.

```shell
title="Here is the Title"
paste_from=20
paste_till=35
language=C++
```

```shell
$ pasteme --start 20 --end 35 --title "Here is the Title" --language cpp program.cpp
```

Also visit the manual by typing `$ pasteme --help` and you have more hints on the options and arguments.

### License
PasteMe is being licensed under the [MIT License](https://github.com/collove/pasteme/blob/main/LICENSE).

### Special Thanks to
- [Hashnode](https://hashnode.com/)
- [PlanetScale](https://planetscale.com/)
<!--
  ~ Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>, nfitzen
  ~ 
  ~ SPDX-License-Identifier: MIT
  -->

# python-anilist

[![License](https://img.shields.io/github/license/AmanoTeam/aiodown)](https://github.com/AmanoTeam/python-anilist/raw/main/LICENSE)
![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)
![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Contributors](https://img.shields.io/github/contributors/AmanoTeam/python-anilist.svg)](https://github.com/AmanoTeam/python-anilist/graphs/contributors)
[![PyPi](https://badge.fury.io/py/python-anilist.svg)](https://pypi.org/project/python-anilist/)

> A simple wrapper with full support for `asyncio` made in `Python 3` for [Anilist](//anilist.co) using [httpx](//github.com/encode/httpx).

## Requirements

- Python 3.7 or higher.
- httpx 0.14 or higher.

## Installation

**NOTE:** If `python3` is "not a recognized command" try using `python` instead.

For the latest stable version:
```sh
python3 -m pip install python-anilist
```

For the latest development version:
```sh
python3 -m pip install git+https://github.com/AmanoTeam/python-anilist.git#egg=python-anilist
```

## Basic starting guide

First, import the module
```py
import anilist
```

Next, define the client to interact with the API

```py
client = anilist.Client()
```

You can search for the name of something on the site using:
- `client.search_user(name, limit=10)`
- `client.search_anime(name, limit=10)`
- `client.search_manga(name, limit=10)`
- `client.search_character(name, limit=10)`
- `client.search_staff(name, limit=10)`

If you know the ID of something, then use the get() commands instead:
- `client.get_user(ID)`
- `client.get_anime(ID)`
etc.

Example code usage:

```py
from pythonanilist import anilist

client = anilist.Client()

madoka_list = client.search_anime("madoka", limit=10)  # returns list of up to 10 Anime object results
madoka = madoka_list[0][0][0]  # assume you want the first search result
print(madoka.title, madoka.id)

>>> {'romaji': 'Mahou Shoujo Madoka☆Magica', 'english': 'Puella Magi Madoka Magica', 'native': '魔法少女まどか☆マギカ'} 9756
```
## What's left to do?

- Write the API Documentation.
- Show some examples.

## Credits

* [AnilistPy](//github.com/anilistpy/anilistpy): for inspiration.

## License

Copyright © 2021-2022 [AmanoTeam](https://github.com/AmanoTeam)
and the python-anilist contributors

Licensed under the [Expat/MIT license](LICENSE).
This project is also [REUSE compliant](https://reuse.software/).
See individual files for more copyright information.

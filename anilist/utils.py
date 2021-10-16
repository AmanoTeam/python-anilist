#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Amano Team <https://amanoteam.com/> and the python-anilist contributors

from .queries import *

API_URL = "https://graphql.anilist.co"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

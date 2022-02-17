#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/> and the python-anilist contributors

from .queries import (
    ANIME_SEARCH_QUERY,
    MANGA_SEARCH_QUERY,
    CHARACTER_SEARCH_QUERY,
    STAFF_SEARCH_QUERY,
    USER_SEARCH_QUERY,
    ANIME_GET_QUERY,
    MANGA_GET_QUERY,
    CHARACTER_GET_QUERY,
    STAFF_GET_QUERY,
    USER_GET_QUERY,
    LIST_GET_QUERY,
    LIST_ITEM_GET_QUERY,
    LIST_GET_QUERY_ANIME,
    LIST_GET_QUERY_MANGA,
    LIST_ACTIVITY_QUERY,
    TEXT_ACTIVITY_QUERY,
    MESSAGE_ACTIVITY_QUERY,
    MESSAGE_ACTIVITY_QUERY_SENT,
    MESSAGE_ACTIVITY_SENT_QUERY,
)

API_URL = "https://graphql.anilist.co"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
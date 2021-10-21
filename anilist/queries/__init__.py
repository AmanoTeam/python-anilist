#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Amano Team <https://amanoteam.com/> and the python-anilist contributors

from importlib.resources import read_text
from ._query_files import activity, get, search

__all__ = (
    "ANIME_SEARCH_QUERY",
    "MANGA_SEARCH_QUERY",
    "CHARACTER_SEARCH_QUERY",
    "STAFF_SEARCH_QUERY",
    "USER_SEARCH_QUERY",
    "ANIME_GET_QUERY",
    "MANGA_GET_QUERY",
    "CHARACTER_GET_QUERY",
    "STAFF_GET_QUERY",
    "USER_GET_QUERY",
    "LIST_GET_QUERY",
    "LIST_ITEM_GET_QUERY",
    "LIST_ACTIVITY_QUERY",
    "TEXT_ACTIVITY_QUERY",
    "MESSAGE_ACTIVITY_QUERY",
    "MESSAGE_ACTIVITY_QUERY_SENT",
    "MESSAGE_ACTIVITY_SENT_QUERY",
)

ANIME_SEARCH_QUERY = read_text(search, "anime_search.graphql")
MANGA_SEARCH_QUERY = read_text(search, "manga_search.graphql")
CHARACTER_SEARCH_QUERY = read_text(search, "character_search.graphql")
STAFF_SEARCH_QUERY = read_text(search, "staff_search.graphql")
USER_SEARCH_QUERY = read_text(search, "user_search.graphql")

ANIME_GET_QUERY = read_text(get, "anime_get.graphql")
MANGA_GET_QUERY = read_text(get, "manga_get.graphql")
CHARACTER_GET_QUERY = read_text(get, "character_get.graphql")
STAFF_GET_QUERY = read_text(get, "staff_get.graphql")
USER_GET_QUERY = read_text(get, "user_get.graphql")
LIST_GET_QUERY = read_text(get, "list_get.graphql")
LIST_ITEM_GET_QUERY = read_text(get, "list_item_get.graphql")

# I wonder if the activity queries should be lumped under "get" instead.
# They function pretty much exactly the same. - nfitzen

LIST_ACTIVITY_QUERY = read_text(activity, "list_activity.graphql")
TEXT_ACTIVITY_QUERY = read_text(activity, "text_activity.graphql")
MESSAGE_ACTIVITY_QUERY = read_text(activity, "message_activity.graphql")
MESSAGE_ACTIVITY_QUERY_SENT = read_text(activity, "message_activity_sent.graphql")
MESSAGE_ACTIVITY_SENT_QUERY = MESSAGE_ACTIVITY_QUERY_SENT

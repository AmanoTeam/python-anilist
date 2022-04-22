#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .activity import ListActivity, ListActivityStatus, TextActivity
from .anime import Anime
from .character import Character
from .cover import Cover
from .date import Date
from .favourites import FavouritesUnion
from .image import Image
from .manga import Manga
from .medialist import MediaList
from .name import Name
from .next_airing import NextAiring
from .page import PageInfo
from .score import Score
from .season import Season
from .staff import Staff, Studio
from .statistics import Ranking, Statistic, StatisticsUnion
from .title import Title
from .trailer import Trailer
from .user import User

__all__ = [
    "Anime",
    "Character",
    "Cover",
    "Date",
    "FavouritesUnion",
    "Image",
    "ListActivity",
    "ListActivityStatus",
    "Name",
    "NextAiring",
    "Manga",
    "PageInfo",
    "MediaList",
    "Ranking",
    "TextActivity",
    "Title",
    "Trailer",
    "Score",
    "Season",
    "Staff",
    "Statistic",
    "StatisticsUnion",
    "Studio",
    "User",
]

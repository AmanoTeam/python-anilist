#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .anime import Anime
from .character import Character
from .cover import Cover
from .date import Date
from .image import Image
from .name import Name
from .next_airing import NextAiring
from .manga import Manga
from .title import Title
from .trailer import Trailer
from .score import Score
from .season import Season
from .staff import Staff, Studio
from .favourites import FavouritesUnion
from .statistics import Statistic, StatisticsUnion, Ranking
from .user import User
from .activity import ListActivity, ListActivityStatus, TextActivity
from .medialist import MediaList

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

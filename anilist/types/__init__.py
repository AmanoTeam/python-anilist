# MIT License
#
# Copyright (c) 2021 Amano Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

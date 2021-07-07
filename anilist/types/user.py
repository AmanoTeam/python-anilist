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

from .name import Name
from .image import Image
from .date import Date
from .favourites import FavouritesUnion
from .statistics import StatisticsUnion
from typing import Callable, Dict


class User:
    def __init__(
        self,
        *,
        id: int,
        name: str,
        created_at: int,
        updated_at: int,
        about: str = None,
        image: Dict = None,
        favourites: FavouritesUnion = None,
        statistics: StatisticsUnion = None,
        url: str = None,
        donator_tier: int = None,
        donator_badge: str = None,
    ):
        self.id = id
        self.name = name
        self.created_at = Date.from_timestamp(created_at)
        self.updated_at = Date.from_timestamp(updated_at)
        if about:
            self.about = about
        if image:
            self.image = Image(medium=image["medium"], large=image["large"])
        if favourites:
            self.favourites = favourites
        if statistics:
            self.statistics = statistics
        if url:
            self.url = url
        if donator_tier:
            self.donator_tier = donator_tier
        if donator_badge:
            self.donator_badge = donator_badge

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

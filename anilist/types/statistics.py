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

from .score import Score
from typing import Dict, Callable, List


class Ranking:
    def __init__(
        self,
        *,
        type: str,
        format: str,
        rank: int,
        all_time: bool = False,
        year: int = None,
        season: str = None,
    ) -> None:
        self.type = type
        self.format = format
        self.rank = rank
        self.all_time = all_time
        if year:
            self.year = year
        if season:
            self.season = season

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())


class Statistic:
    def __init__(
        self,
        *,
        count: int,
        mean_score: int,
        minutes_watched: int,
        episodes_watched: int,
        chapters_read: int,
        volumes_read: int,
        statuses: List[Dict[str, int]] = None,
        genres: List[Dict[str, int]] = None,
        tags: List[Dict[str, int]] = None,
    ) -> None:
        self.count = count
        self.mean_score = mean_score
        self.minutes_watched = minutes_watched
        self.episodes_watched = episodes_watched
        self.chapters_read = chapters_read
        self.volumes_read = volumes_read
        if statuses:
            self.statuses = statuses
        if genres:
            self.genres = genres
        if tags:
            self.tags = tags

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())


class StatisticsUnion:
    def __init__(self, *, anime: Statistic, manga: Statistic) -> None:
        self.anime = anime
        self.manga = manga

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())
#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .score import Score
from typing import Dict, Callable, List


class Ranking:
    """Ranking of a media object."""

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
    """Statistic object of a user."""

    def __init__(
        self,
        *,
        count: int,
        mean_score: int,
        minutes_watched: int = None,
        episodes_watched: int = None,
        chapters_read: int = None,
        volumes_read: int = None,
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
    """Union containing anime and manga statistics of a user."""

    def __init__(self, *, anime: Statistic, manga: Statistic) -> None:
        self.anime = anime
        self.manga = manga

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

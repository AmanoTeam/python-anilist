#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict, List

from .object import Object
from .score import Score


class Ranking(Object):
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


class Statistic(Object):
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
        statuses: list[list[dict[str, int], dict[str, int]]] = None,
        genres: list[list[dict[str, int], dict[str, int]]] = None,
        tags: list[list[dict[str, int], dict[str, int]]] = None,
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


class StatisticsUnion(Object):
    """Union containing anime and manga statistics of a user."""

    def __init__(self, *, anime: Statistic, manga: Statistic) -> None:
        self.anime = anime
        self.manga = manga

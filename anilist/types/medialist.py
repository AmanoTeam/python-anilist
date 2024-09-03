#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict, Union

from .anime import Anime
from .date import Date
from .manga import Manga
from .object import Hashable


class MediaList(Hashable):
    """List item containing state of a entry in a user's list."""

    def __init__(
        self,
        *,
        id: int,
        status: str = None,
        score: float = None,
        progress: int = None,
        repeat: int = None,
        priority: int = None,
        start_date: Dict = None,
        complete_date: Dict = None,
        update_date: int = None,
        create_date: int = None,
        media: Union[Anime, Manga] = None,
    ) -> None:
        self.id = id
        if status:
            self.status = status
        if score:
            self.score = score
        if progress:
            self.progress = progress
        if repeat:
            self.repeat = repeat
        if priority:
            self.priority = priority
        if start_date:
            self.start_date = Date(
                year=start_date["year"],
                month=start_date["month"],
                day=start_date["day"],
            )
        if complete_date:
            self.complete_date = Date(
                year=complete_date["year"],
                month=complete_date["month"],
                day=complete_date["day"],
            )
        if update_date:
            self.update_date = Date.from_timestamp(update_date)
        if create_date:
            self.create_date = Date.from_timestamp(create_date)
        if media:
            self.media = media

#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .date import Date
from typing import Callable, Dict


class NextAiring:
    """Status of an airing anime."""

    def __init__(
        self,
        *,
        time_until: int = None,
        at: int = None,
        episode: int = None,
    ):
        if time_until:
            self.time_until = time_until
        if at:
            self.at = Date.from_timestamp(at)
        if episode:
            self.episode = episode

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

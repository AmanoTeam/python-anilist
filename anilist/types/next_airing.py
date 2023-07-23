#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .date import Date
from .object import Object


class NextAiring(Object):
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

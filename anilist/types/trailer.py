#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Hashable


class Trailer(Hashable):
    """Contains data for anime trailers."""

    def __init__(
        self,
        *,
        id: int = None,
        thumbnail: str = None,
        site: str = None,
    ):
        if id:
            self.id = id
        if thumbnail:
            self.thumbnail = thumbnail
        if site:
            self.site = site
            if site == "youtube":
                self.url = f"https://youtu.be/{id}"

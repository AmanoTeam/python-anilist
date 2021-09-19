#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .name import Name
from .image import Image
from .date import Date
from .favourites import FavouritesUnion
from .statistics import StatisticsUnion
from typing import Callable, Dict, Tuple


def get_profile_color(color: str) -> Tuple[int, int, int]:
    """Returns RGB value from color name.

    Args:
        color (str): Color name or hex code.

    Returns:
        Tuple[int, int, int]: RGB value for the color.
    """
    if color == "blue":
        return 61, 180, 242
    elif color == "purple":
        return 192, 99, 255
    elif color == "green":
        return 76, 202, 81
    elif color == "orange":
        return 239, 136, 26
    elif color == "red":
        return 255, 51, 51
    elif color == "pink":
        return 252, 157, 214
    elif color == "gray":
        return 103, 123, 148
    elif "#" in color:
        color = color.replace("#", "")
        return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))
    else:
        return 255, 255, 255


class User:
    """User object."""

    def __init__(
        self,
        *,
        id: int,
        name: str,
        created_at: int = None,
        updated_at: int = None,
        about: str = None,
        image: Dict = None,
        favourites: FavouritesUnion = None,
        statistics: StatisticsUnion = None,
        url: str = None,
        donator_tier: int = None,
        donator_badge: str = None,
        profile_color: str = None,
    ):
        self.id = id
        self.name = name
        if created_at:
            self.created_at = Date.from_timestamp(created_at)
        if updated_at:
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
        if profile_color:
            self.profile_color = get_profile_color(profile_color)

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .name import Name
from .image import Image
from .date import Date
from typing import Callable, Dict


class Character:
    """Character object."""

    def __init__(
        self,
        *,
        id: int,
        name: Dict,
        role: str = None,
        image: Dict = None,
        url: str = None,
        favorites: int = None,
        description: str = None,
        media: Dict = None,
        birth_date: Dict = None,
        age: int = None,
        is_favorite: bool = None,
        gender: str = None,
    ):
        self.id = id
        self.name = Name(
            first=name["first"],
            full=name["full"],
            native=name["native"],
            last=name["last"],
        )
        if role:
            self.role = role
        if image:
            self.image = Image(medium=image["medium"], large=image["large"])
        if url:
            self.url = url
        if favorites:
            self.favorites = favorites
        if description:
            self.description = description
        if media:
            self.media = [item["node"] for item in media["edges"]]
        if birth_date:
            self.birth_date = Date(
                year=birth_date["year"],
                month=birth_date["month"],
                day=birth_date["day"],
            )
        if age:
            self.age = age
        if gender:
            self.gender = gender
        if is_favorite is not None:
            self.is_favorite = is_favorite

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

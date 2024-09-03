#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict, List

from .anime import Anime
from .character import Character
from .manga import Manga
from .object import Object
from .staff import Staff, Studio


class FavouritesUnion(Object):
    """Favourites union containing all
    anime, manga, character, staff and studio
    favourites of a user."""

    def __init__(
            self,
            *,
            anime: List[Anime] = None,
            manga: List[Manga] = None,
            characters: List[Character] = None,
            staff: List[Staff] = None,
            studios: List[Studio] = None,
    ) -> None:
        if not anime:
            anime = []
        if not manga:
            manga = []
        if not characters:
            characters = []
        if not staff:
            staff = []
        if not studios:
            studios = []

        self.anime = anime
        self.manga = manga
        self.characters = characters
        self.staff = staff
        self.studios = studios

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            if ((self.anime, self.manga, self.characters, self.staff, self.studios) ==
                    (other.anime, other.manga, other.characters, other.staff, other.studios)):
                return True

#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Object


class Title(Object):
    """Title object."""

    def __init__(
        self,
        *,
        romaji: str,
        english: str,
        native: str,
    ):
        if romaji:
            self.romaji = romaji
        if english:
            self.english = english
        if native:
            self.native = native

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return str(self) == str(other)

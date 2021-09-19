#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Title:
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

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

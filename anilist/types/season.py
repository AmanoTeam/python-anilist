#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Object


class Season(Object):
    """Season object that represents a season."""

    def __init__(
        self,
        *,
        name: str = None,
        year: int = None,
        number: int = None,
    ):
        if name:
            self.name = name
        if year:
            self.year = year
        if number:
            self.number = number

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            if (self.name, self.year, self.number) == (other.name, other.year, other.number):
                return True
            
    def __hash__(self) -> int:
        return hash((self.name, self.year, self.number))

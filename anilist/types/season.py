#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Season:
    """Season object that represents a seson."""

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

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Date:
    def __init__(
        self,
        *,
        year: int = None,
        month: int = None,
        day: int = None,
    ):
        if year:
            self.year = year
        if month:
            self.month = month
        if day:
            self.day = day

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

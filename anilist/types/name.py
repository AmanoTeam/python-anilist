#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Name:
    """Name object."""

    def __init__(
        self,
        *,
        first: str,
        full: str,
        native: str,
        last: str,
        alternative: str = None,
    ):
        if first:
            self.first = first
        if full:
            self.full = full
        if native:
            self.native = native
        if last:
            self.last = last
        if alternative:
            self.alternative = alternative

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

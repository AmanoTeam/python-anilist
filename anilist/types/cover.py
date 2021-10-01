#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Cover:
    """Cover object. Contains URL's for each size."""

    def __init__(
        self,
        *,
        medium: str = None,
        large: str = None,
        extra_large: str = None,
    ):
        if medium:
            self.medium = medium
        if large:
            self.large = large
        if extra_large:
            self.extra_large = extra_large

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

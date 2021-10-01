#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Image:
    """Image object."""

    def __init__(
        self,
        *,
        medium: str = None,
        large: str = None,
    ):
        if medium:
            self.medium = medium
        if large:
            self.large = large

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

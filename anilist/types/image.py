#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Object


class Image(Object):
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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.raw() == other.raw()

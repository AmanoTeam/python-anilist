#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Object


class Cover(Object):
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

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__repr__() == other.__repr__()

#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict

from .object import Object


class Score(Object):
    """Mean and average score union."""

    def __init__(
        self,
        *,
        mean: int = None,
        average: int = None,
    ):
        if mean:
            self.mean = mean
        if average:
            self.average = average

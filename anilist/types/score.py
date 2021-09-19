#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class Score:
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

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

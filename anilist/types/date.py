#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from datetime import datetime, date
from typing import Callable, Dict


class Date:
    """Date object containing year, month and day."""

    def __init__(
        self,
        *,
        year: int = None,
        month: int = None,
        day: int = None,
        timestamp: int = None
    ):
        if year:
            self.year = year
        if month:
            self.month = month
        if day:
            self.day = day
        if timestamp:
            self.timestamp = timestamp

    @staticmethod
    def from_timestamp(timestamp: int) -> "Date":
        """Creates a Date object from a timestamp.

        Args:
            timestamp (int): Timestamp.

        Returns:
            Date: Date object.
        """
        time = datetime.fromtimestamp(timestamp)
        return Date(year=time.year, month=time.month, day=time.day, timestamp=timestamp)

    def get_timestamp(self) -> int:
        """Formats and returns timestamp.

        Returns:
            int: Formatted timestamp.
        """
        if hasattr(self, "timestamp"):
            return self.timestamp

        if (
            not hasattr(self, "year")
            and not hasattr(self, "month")
            and not hasattr(self, "day")
        ):
            return -1

        dt = datetime(
            self.year if hasattr(self, "year") else date.today().year + 1,
            self.month if hasattr(self, "month") else 1,
            self.day if hasattr(self, "day") else 1,
        )

        return round(dt.timestamp())

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

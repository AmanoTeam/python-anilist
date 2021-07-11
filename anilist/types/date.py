# MIT License
#
# Copyright (c) 2021 Amano Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from datetime import datetime, date
from typing import Callable, Dict


class Date:
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
        time = datetime.fromtimestamp(timestamp)
        return Date(year=time.year, month=time.month, day=time.day, timestamp=timestamp)

    def get_timestamp(self) -> int:
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

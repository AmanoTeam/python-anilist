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

from .date import Date
from typing import Dict, Callable


class MediaList:
    def __init__(
        self,
        *,
        id: int,
        status: str,
        score: float,
        progress: int,
        repeat: int,
        priority: int,
        start_date: Dict,
        complete_date: Dict,
        update_date: int,
        create_date: int
    ) -> None:
        self.id = id
        self.status = status
        self.score = score
        self.progress = progress
        self.repeat = repeat
        self.priority = priority
        self.start_date = Date(
            year=start_date["year"],
            month=start_date["month"],
            day=start_date["day"],
        )
        self.complete_date = Date(
            year=complete_date["year"],
            month=complete_date["month"],
            day=complete_date["day"],
        )
        self.update_date = Date.from_timestamp(update_date)
        self.create_date = Date.from_timestamp(create_date)

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())
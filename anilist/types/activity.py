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

from .anime import Anime
from .manga import Manga
from .date import Date

from typing import List, Union, Dict, Callable, Optional


class ListActivityStatus:

    MAP = {
        "PLANS TO WATCH": 0,
        "WATCHED EPISODE": 1,
        "REWATCHED EPISODE": 2,
        "PAUSED WATCHING": 3,
        "PLANS TO READ": 0,
        "READ CHAPTER": 1,
        "REREAD CHAPTER": 2,
        "PAUSED READING": 3,
        "DROPPED": 4,
        "COMPLETED": 5,
    }

    def __init__(self, *, status: str, progress: str = None) -> None:

        if status.upper() not in self.MAP:
            raise TypeError("invalid status")

        self.string = status.upper()
        self.type = self.MAP[status.upper()]
        self.progress = Optional[Union[List[int], int]]

        if self.MAP[self.string] in [1, 2]:

            if "-" in progress:
                progress: list = progress.replace(" ", "").split("-")
                self.progress = [int(i) for i in progress]
            else:
                self.progress = int(progress)
        else:
            self.progress = None

    def __repr__(self) -> Callable:
        return "<ListActivityStatus: {}:{}>".format(self.string, str(self.type))

    def __eq__(self, o: "ListActivityStatus") -> bool:
        return "<ListActivityStatus: {}:{}>".format(self.string, str(self.type)) == str(
            o
        )

    def __str__(self) -> str:

        progress_str = ""
        if not self.progress:
            pass
        elif isinstance(self.progress, List):
            progress_str = " " + " - ".join(str(i) for i in self.progress)
        elif isinstance(self.progress, int):
            progress_str = " " + str(self.progress)

        return "{}{}".format(
            self.string.title(),
            progress_str,
        )


class ListActivity:
    def __init__(
        self,
        *,
        id: int,
        date: int,
        status: str = None,
        progress: str = None,
        url: str = None,
        media: Union[Anime, Manga] = None,
    ) -> None:
        self.id = id
        self.date = Date.from_timestamp(date)
        if status or progress:
            self.status = ListActivityStatus(status=status, progress=progress)
        if url:
            self.url = url
        if media:
            self.media = media

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())


class TextActivity:
    def __init__(
        self,
        *,
        id: int,
        reply_count: int,
        date: int,
        text: str = None,
        url: str = None,
    ) -> None:
        self.id = id
        self.reply_count = reply_count
        self.date = Date.from_timestamp(date)
        if text:
            self.text = text
        if url:
            self.url = url

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())
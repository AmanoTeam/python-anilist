#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from .user import User
from .anime import Anime
from .manga import Manga
from .date import Date

from typing import List, Union, Dict, Callable, Optional


class ListActivityStatus:
    """Status object for list activities.

    Args:
        status (str): Status string.
        progress (str): Progress string. Defaults to None.

    Attributes:
        MAP (Dict[str, int]): Map of text statuses that represent status codes.
        string (str): Formatted status string.
        type (int): Status code.
        progress (Union[List[int], int], optional): Activity progress.
    """

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
    """List activity object.

    Args:
        id (int): Activity id.
        date (int): Activity timestamp.
        status (str, optional): Activity status text. Defaults to None.
        progress (str, optional): Activity progress. Defaults to None.
        url (str, optional): Activity URL. Defaults to None.
        media (Union[Anime, Manga], optional): Activity media. Defaults to None.

    Attributes:
        id (int): Activity id.
        date (Date): Activity date.
        status (ListActivityStatus, optional): Activity status text.
        url (str, optional): Activity URL.
        media (Union[Anime, Manga], optional): Activity media.
    """

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
    """Text activity object.

    Args:
        id (int): Activity id.
        reply_count (int): Total reply count.
        date (int): Activity timestamp.
        user (User): Activity author.
        text (str, optional): Activity content. Defaults to None.
        text_html (str, optional): Activity content in HTML. Defaults to None.
        url (str, optional): Activity URL. Defaults to None.
        recipient (User, optional): Activity recipient. Defaults to None.

    Attributes:
        id (int): Activity id.
        reply_count (int): Total reply count.
        date (Date): Activity date.
        user (User): Activity author.
        text (str, optional): Activity content.
        text_html (str, optional): Activity content in HTML.
        url (str, optional): Activity URL.
        recipient (User, optional): Activity recipient.
    """

    def __init__(
        self,
        *,
        id: int,
        reply_count: int,
        date: int,
        user: User,
        text: str = None,
        text_html: str = None,
        url: str = None,
        recipient: User = None,
    ) -> None:
        self.id = id
        self.reply_count = reply_count
        self.date = Date.from_timestamp(date)
        self.user = user
        if text:
            self.text = text
        if text_html:
            self.text_html = text
        if url:
            self.url = url
        if recipient:
            self.recipient = recipient

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

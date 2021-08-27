#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

class Trailer:
    def __init__(
        self,
        *,
        id: int = None,
        thumbnail: str = None,
        site: str = None,
    ):
        if id:
            self.id = id
        if thumbnail:
            self.thumbnail = thumbnail
        if site:
            self.site = site
            if site == "youtube":
                self.url = f"https://youtu.be/{id}"

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

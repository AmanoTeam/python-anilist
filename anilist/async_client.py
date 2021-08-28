#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

import httpx

from anilist.types import Anime, Character, Manga
from typing import Optional
from anilist.utils import (
    ANIME_GET_QUERY,
    ANIME_SEARCH_QUERY,
    API_URL,
    CHARACTER_GET_QUERY,
    CHARACTER_SEARCH_QUERY,
    HEADERS,
    MANGA_GET_QUERY,
    MANGA_SEARCH_QUERY,
)


class Client:
    def __init__(self):
        self.httpx = None

    async def __aenter__(self):
        self.httpx = httpx.AsyncClient(http2=True)
        return self

    async def __aexit__(self, *args):
        await self.httpx.aclose()
        self.httpx = None
        return None

    async def search(self, query: str, content_type: str = "anime", limit: int = 10):
        if isinstance(content_type, str):
            content_type = content_type.lower()
        else:
            raise TypeError(
                f"content_type argument must be a string, not '{content_type.__class__.__name__}'"
            )
        if not isinstance(query, str):
            raise TypeError(
                f"query argument must be a string, not '{query.__class__.__name__}'"
            )
        if isinstance(limit, str) and limit.isdecimal():
            limit = int(limit)
        elif not isinstance(limit, int):
            raise TypeError(
                f"limit argument must be a string, not '{limit.__class__.__name__}'"
            )
        if content_type == "anime":
            return await self.search_anime(query=query, limit=limit, avg_score=avg_score)
        elif content_type in ["char", "character"]:
            return await self.search_character(query=query, limit=limit)
        elif content_type == "manga":
            return await self.search_manga(query=query, limit=limit)
        else:
            raise TypeError("There is no such content type.")

    async def get(self, id: int, content_type: str = "anime"):
        if isinstance(content_type, str):
            content_type = content_type.lower()
        else:
            raise TypeError(
                f"content_type argument must be a string, not '{content_type.__class__.__name__}'"
            )
        if isinstance(id, str) and id.isdecimal():
            id = int(id)
        elif not isinstance(id, int):
            raise TypeError(
                f"id argument must be a string, not '{id.__class__.__name__}'"
            )
        if content_type == "anime":
            return await self.get_anime(id=id)
        elif content_type in ["char", "character"]:
            return await self.get_character(id=id)
        elif content_type == "manga":
            return await self.get_manga(id=id)
        else:
            raise TypeError("There is no such content type.")

    async def search_anime(self, query: str, limit: int, avg_score: int) -> Optional[Anime]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=ANIME_SEARCH_QUERY,
                variables=dict(
                    search=query,
                    score=avg_score,
                    per_page=limit,
                    MediaType="ANIME",
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        if data["data"]:
            try:
                items = data["data"]["Page"]["media"]
                results = [
                    Anime(id=item["id"], title=item["title"], url=item["siteUrl"])
                    for item in items
                ]
                return results
            except:
                pass
        return None

    async def search_character(self, query: str, limit: int) -> Optional[Character]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=CHARACTER_SEARCH_QUERY,
                variables=dict(
                    search=query,
                    per_page=limit,
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        if data["data"]:
            try:
                items = data["data"]["Page"]["characters"]
                results = [
                    Character(id=item["id"], name=item["name"]) for item in items
                ]
                return results
            except:
                pass
        return None

    async def search_manga(self, query: str, limit: int) -> Optional[Manga]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=MANGA_SEARCH_QUERY,
                variables=dict(
                    search=query,
                    per_page=limit,
                    MediaType="MANGA",
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        if data["data"]:
            try:
                items = data["data"]["Page"]["media"]
                results = [
                    Manga(id=item["id"], title=item["title"], url=item["siteUrl"])
                    for item in items
                ]
                return results
            except:
                pass
        return None

    async def get_anime(self, id: int) -> Optional[Anime]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=ANIME_GET_QUERY,
                variables=dict(
                    id=id,
                    MediaType="ANIME",
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        if data["data"]:
            try:
                item = data["data"]["Page"]["media"][0]
                return Anime(
                    id=item["id"],
                    title=item["title"],
                    url=item["siteUrl"],
                    episodes=item["episodes"],
                    description=item["description"],
                    format=item["format"],
                    status=item["status"],
                    duration=item["duration"],
                    genres=item["genres"],
                    tags=item["tags"],
                    studios=item["studios"],
                    start_date=item["startDate"],
                    end_date=item["endDate"],
                    season=dict(
                        name=item["season"],
                        year=item["seasonYear"],
                        number=item["seasonInt"],
                    ),
                    country=item["countryOfOrigin"],
                    cover=item["coverImage"],
                    banner=item["bannerImage"],
                    source=item["source"],
                    hashtag=item["hashtag"],
                    synonyms=item["synonyms"],
                    score=dict(
                        mean=item["meanScore"],
                        average=item["averageScore"],
                    ),
                    next_airing=item["nextAiringEpisode"],
                    trailer=item["trailer"],
                    staff=item["staff"],
                    characters=item["characters"],
                )
            except:
                pass
        return None

    async def get_character(self, id: int) -> Optional[Character]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=CHARACTER_GET_QUERY,
                variables=dict(
                    id=id,
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        if data["data"]:
            try:
                item = data["data"]["Character"]
                return Character(
                    id=item["id"],
                    name=item["name"],
                    image=item["image"],
                    url=item["siteUrl"],
                    favorites=item["favourites"],
                    description=item["description"],
                    media=item["media"],
                    is_favorite=item["isFavourite"],
                )
            except:
                pass
        return None

    async def get_manga(self, id: int) -> Optional[Manga]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=MANGA_GET_QUERY,
                variables=dict(
                    id=id,
                    MediaType="MANGA",
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        if data["data"]:
            try:
                item = data["data"]["Page"]["media"][0]
                return Manga(
                    id=item["id"],
                    title=item["title"],
                    url=item["siteUrl"],
                    chapters=item["chapters"],
                    description=item["description"],
                    status=item["status"],
                    genres=item["genres"],
                    tags=item["tags"],
                    studios=item["studios"],
                    start_date=item["startDate"],
                    end_date=item["endDate"],
                    season=dict(
                        name=item["season"],
                        year=item["seasonYear"],
                        number=item["seasonInt"],
                    ),
                    country=item["countryOfOrigin"],
                    cover=item["coverImage"],
                    banner=item["bannerImage"],
                    source=item["source"],
                    hashtag=item["hashtag"],
                    synonyms=item["synonyms"],
                    score=dict(
                        mean=item["meanScore"],
                        average=item["averageScore"],
                    ),
                    next_airing=item["nextAiringEpisode"],
                    trailer=item["trailer"],
                    staff=item["staff"],
                    characters=item["characters"],
                    volumes=item["volumes"],
                )
            except:
                pass
        return None

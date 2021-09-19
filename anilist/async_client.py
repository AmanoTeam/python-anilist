#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

import httpx

from anilist.types import (
    Anime,
    Character,
    Manga,
    User,
    FavouritesUnion,
    Staff,
    Studio,
    StatisticsUnion,
    Statistic,
    ListActivity,
    TextActivity,
    MediaList,
    Ranking,
)
from typing import Optional, Union, List, Tuple
from anilist.utils import (
    API_URL,
    HEADERS,
    ANIME_GET_QUERY,
    ANIME_SEARCH_QUERY,
    MANGA_GET_QUERY,
    MANGA_SEARCH_QUERY,
    CHARACTER_GET_QUERY,
    CHARACTER_SEARCH_QUERY,
    STAFF_GET_QUERY,
    STAFF_SEARCH_QUERY,
    USER_GET_QUERY,
    USER_SEARCH_QUERY,
    LIST_GET_QUERY,
    LIST_ITEM_GET_QUERY,
    LIST_ACTIVITY_QUERY,
    TEXT_ACTIVITY_QUERY,
    MESSAGE_ACTIVITY_QUERY,
    MESSAGE_ACTIVITY_QUERY_SENT,
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

    async def search(
        self, query: str, content_type: str = "anime", page: int = 1, limit: int = 10
    ):
        """Used to search specified content type with the given query.

        Args:
            query (str): Search query.
            content_type (str, optional): anime, manga, character, staff or user. Defaults to "anime".
            page (int, optional): Current page. Defaults to 1.
            limit (int, optional): Maximum items per page. Defaults to 10.

        Raises:
            TypeError: If content type is not a string.
            TypeError: If query type is not a string.
            TypeError: If limit argument is not an int.
            TypeError: If the content type is invalid.

        Returns:
            Union[Anime, Manga, Character, Staff, User], optional: Search results.
        """
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
                f"limit argument must be an int, not '{limit.__class__.__name__}'"
            )
        if content_type == "anime":
            return await self.search_anime(query=query, page=page, limit=limit)
        elif content_type == "manga":
            return await self.search_manga(query=query, page=page, limit=limit)
        elif content_type in ["char", "character"]:
            return await self.search_character(query=query, page=page, limit=limit)
        elif content_type == "staff":
            return await self.search_staff(query=query, page=page, limit=limit)
        elif content_type == "user":
            return await self.search_user(query=query, page=page, limit=limit)
        else:
            raise TypeError("There is no such content type.")

    async def get(
        self,
        id: Union[int, str],
        content_type: str = "anime",
        page: int = 1,
        limit: int = 25,
    ):
        """Gets specified item from given id.

        Args:
            id (Union[int, str]): Item id.
            content_type (str, optional): anime, manga, character, staff, list or user. Defaults to "anime".
            page (int, optional): Current page. Defaults to 1. Only used for lists.
            limit (int, optional): Maximum items per page. Defaults to 25. Only used for lists.

        Raises:
            TypeError: If content type is not a string.
            TypeError: If the list author is not found.
            TypeError: If id is not an int or a valid user.
            TypeError: If id is not a string for a user.
            TypeError: If the content type is invalid.

        Returns:
            Union[Anime, Manga, Character, Staff, List[MediaList], User], optional: Returned items.
        """
        if isinstance(content_type, str):
            content_type = content_type.lower()
        else:
            raise TypeError(
                f"content_type argument must be a string, not '{content_type.__class__.__name__}'"
            )
        if isinstance(id, str) and id.isdecimal():
            id = int(id)
        elif not isinstance(id, int):
            if content_type == "user":
                user = await self.get_user(name=id)
                return user
            elif content_type == "list":
                try:
                    user = await self.get_user(name=id)
                    id = user.id
                except Exception:
                    raise TypeError(f"user not found")
            else:
                raise TypeError(
                    f"id argument must be a string, not '{id.__class__.__name__}'"
                )
        if content_type == "anime":
            return await self.get_anime(id=id)
        elif content_type == "manga":
            return await self.get_manga(id=id)
        elif content_type in ["char", "character"]:
            return await self.get_character(id=id)
        elif content_type == "staff":
            return await self.get_staff(id=id)
        elif content_type == "list":
            return await self.get_list(user_id=id, limit=limit, page=page)
        elif content_type == "user":
            raise TypeError("id argument must be a string for the user object.")
        else:
            raise TypeError("There is no such content type.")

    async def search_anime(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[Anime]:
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
                    page=page,
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
            except Exception:
                pass
        return None

    async def search_manga(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[Manga]:
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
                    page=page,
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
            except Exception:
                pass
        return None

    async def search_character(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[Character]:
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
                    page=page,
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
            except Exception:
                pass
        return None

    async def search_staff(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[Staff]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=STAFF_SEARCH_QUERY,
                variables=dict(
                    search=query,
                    page=page,
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
                items = data["data"]["Page"]["staff"]
                results = [Staff(id=item["id"], name=item["name"]) for item in items]
                return results
            except Exception:
                pass
        return None

    async def search_user(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[User]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=USER_SEARCH_QUERY,
                variables=dict(
                    search=query,
                    page=page,
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
                items = data["data"]["Page"]["users"]
                results = [
                    User(id=item["id"], name=item["name"], image=item["avatar"])
                    for item in items
                ]
                return results
            except Exception:
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
                    is_adult=item["isAdult"],
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
                    popularity=item["popularity"],
                    rankings=[
                        Ranking(
                            type=i["type"],
                            all_time=i["allTime"],
                            format=i["format"],
                            rank=i["rank"],
                            year=i["year"],
                            season=i["season"],
                        )
                        for i in item["rankings"]
                    ],
                )
            except Exception:
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
                    is_adult=item["isAdult"],
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
                    popularity=item["popularity"],
                    rankings=[
                        Ranking(
                            type=i["type"],
                            all_time=i["allTime"],
                            format=i["format"],
                            rank=i["rank"],
                            year=i["year"],
                            season=i["season"],
                        )
                        for i in item["rankings"]
                    ],
                )
            except Exception:
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
            except Exception:
                pass
        return None

    async def get_staff(self, id: int) -> Optional[Staff]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=STAFF_GET_QUERY,
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
                item = data["data"]["Staff"]
                return Staff(
                    id=item["id"],
                    name=item["name"],
                    language=item["languageV2"],
                    image=item["image"],
                    description=item["description"],
                    gender=item["gender"],
                    birth_date=item["dateOfBirth"],
                    death_date=item["dateOfDeath"],
                    url=item["siteUrl"],
                    favorites=item["favourites"],
                    occupations=item["primaryOccupations"],
                    age=item["age"],
                    years_active=item["yearsActive"],
                    home_town=item["homeTown"],
                )
            except Exception:
                pass
        return None

    async def get_user(self, name: str) -> Optional[User]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=USER_GET_QUERY,
                variables=dict(
                    name=name,
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
                item = data["data"]["User"]

                favourites = FavouritesUnion(
                    anime=[
                        Anime(
                            id=i["id"],
                            title=i["title"],
                            url=i["siteUrl"],
                            genres=i["genres"],
                            is_adult=i["isAdult"],
                            cover=i["coverImage"],
                            banner=i["bannerImage"],
                            source=i["source"],
                            hashtag=i["hashtag"],
                            synonyms=i["synonyms"],
                            score=dict(
                                mean=i["meanScore"],
                                average=i["averageScore"],
                            ),
                        )
                        for i in item["favourites"]["anime"]["nodes"]
                    ],
                    manga=[
                        Manga(
                            id=i["id"],
                            title=i["title"],
                            url=i["siteUrl"],
                            genres=i["genres"],
                            is_adult=i["isAdult"],
                            cover=i["coverImage"],
                            banner=i["bannerImage"],
                            source=i["source"],
                            hashtag=i["hashtag"],
                            synonyms=i["synonyms"],
                            score=dict(
                                mean=i["meanScore"],
                                average=i["averageScore"],
                            ),
                        )
                        for i in item["favourites"]["manga"]["nodes"]
                    ],
                    characters=[
                        Character(
                            id=i["id"],
                            name=i["name"],
                            image=i["image"],
                            description=i["description"],
                            gender=i["gender"],
                            birth_date=i["dateOfBirth"],
                            url=i["siteUrl"],
                            favorites=i["favourites"],
                            age=i["age"],
                        )
                        for i in item["favourites"]["characters"]["nodes"]
                    ],
                    staff=[
                        Staff(
                            id=i["id"],
                            name=i["name"],
                            language=i["languageV2"],
                            image=i["image"],
                            description=i["description"],
                            gender=i["gender"],
                            birth_date=i["dateOfBirth"],
                            death_date=i["dateOfDeath"],
                            url=i["siteUrl"],
                            favorites=i["favourites"],
                            occupations=i["primaryOccupations"],
                            age=i["age"],
                            years_active=i["yearsActive"],
                            home_town=i["homeTown"],
                        )
                        for i in item["favourites"]["staff"]["nodes"]
                    ],
                    studios=[
                        Studio(
                            id=i["id"],
                            name=i["name"],
                            is_animation_studio=i["isAnimationStudio"],
                            url=i["siteUrl"],
                            favourites=i["favourites"],
                        )
                        for i in item["favourites"]["studios"]["nodes"]
                    ],
                )

                stat_anime = item["statistics"]["anime"]
                stat_manga = item["statistics"]["manga"]

                statistics = StatisticsUnion(
                    anime=Statistic(
                        count=stat_anime["count"],
                        mean_score=stat_anime["meanScore"],
                        minutes_watched=stat_anime["minutesWatched"],
                        episodes_watched=stat_anime["episodesWatched"],
                        statuses=[
                            [stat["status"], stat["count"]]
                            for stat in stat_anime["statuses"]
                        ],
                        genres=[
                            [genre["genre"], genre["count"]]
                            for genre in stat_anime["genres"]
                        ],
                        tags=[
                            [tag["tag"]["name"], tag["count"]]
                            for tag in stat_anime["tags"]
                        ],
                    ),
                    manga=Statistic(
                        count=stat_manga["count"],
                        mean_score=stat_manga["meanScore"],
                        chapters_read=stat_manga["chaptersRead"],
                        volumes_read=stat_manga["volumesRead"],
                        statuses=[
                            [stat["status"], stat["count"]]
                            for stat in stat_manga["statuses"]
                        ],
                        genres=[
                            [genre["genre"], genre["count"]]
                            for genre in stat_manga["genres"]
                        ],
                        tags=[
                            [tag["tag"]["name"], tag["count"]]
                            for tag in stat_manga["tags"]
                        ],
                    ),
                )

                return User(
                    id=item["id"],
                    name=item["name"],
                    created_at=item["createdAt"],
                    updated_at=item["updatedAt"],
                    image=item["avatar"],
                    url=item["siteUrl"],
                    about=item["about"],
                    donator_tier=item["donatorTier"],
                    donator_badge=item["donatorBadge"],
                    profile_color=item["options"]["profileColor"],
                    favourites=favourites,
                    statistics=statistics,
                )
            except Exception:
                pass
        return None

    async def get_list(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[Tuple[List[MediaList], List[MediaList]]]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=LIST_GET_QUERY,
                variables=dict(
                    user_id=user_id,
                    page=page,
                    per_page=limit,
                ),
            ),
            headers=HEADERS,
        )
        data = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None

        anime_list = []
        manga_list = []
        if data["data"]:
            try:
                item = data["data"]["anime"]["mediaList"]

                for item in data["data"]["anime"]["mediaList"]:
                    media = item["media"]

                    anime = Anime(
                        id=media["id"],
                        title=media["title"],
                        url=media["siteUrl"],
                        episodes=media["episodes"],
                        description=media["description"],
                        format=media["format"],
                        status=media["status"],
                        duration=media["duration"],
                        genres=media["genres"],
                        is_adult=media["isAdult"],
                        tags=media["tags"],
                        studios=media["studios"],
                        start_date=media["startDate"],
                        end_date=media["endDate"],
                        season=dict(
                            name=media["season"],
                            year=media["seasonYear"],
                            number=media["seasonInt"],
                        ),
                        country=media["countryOfOrigin"],
                        cover=media["coverImage"],
                        banner=media["bannerImage"],
                        source=media["source"],
                        hashtag=media["hashtag"],
                        synonyms=media["synonyms"],
                        score=dict(
                            mean=media["meanScore"],
                            average=media["averageScore"],
                        ),
                        next_airing=media["nextAiringEpisode"],
                        trailer=media["trailer"],
                        staff=media["staff"],
                        characters=media["characters"],
                        popularity=media["popularity"],
                        rankings=[
                            Ranking(
                                type=i["type"],
                                all_time=i["allTime"],
                                format=i["format"],
                                rank=i["rank"],
                                year=i["year"],
                                season=i["season"],
                            )
                            for i in media["rankings"]
                        ],
                    )

                    anime_list.append(
                        MediaList(
                            id=item["id"],
                            status=item["status"],
                            score=item["score"],
                            progress=item["progress"],
                            repeat=item["repeat"],
                            priority=item["priority"],
                            start_date=item["startedAt"],
                            complete_date=item["completedAt"],
                            update_date=item["updatedAt"],
                            create_date=item["createdAt"],
                            media=anime,
                        )
                    )

                for item in data["data"]["manga"]["mediaList"]:
                    media = item["media"]

                    manga = Manga(
                        id=media["id"],
                        title=media["title"],
                        url=media["siteUrl"],
                        chapters=media["chapters"],
                        description=media["description"],
                        status=media["status"],
                        genres=media["genres"],
                        is_adult=media["isAdult"],
                        tags=media["tags"],
                        studios=media["studios"],
                        start_date=media["startDate"],
                        end_date=media["endDate"],
                        season=dict(
                            name=media["season"],
                            year=media["seasonYear"],
                            number=media["seasonInt"],
                        ),
                        country=media["countryOfOrigin"],
                        cover=media["coverImage"],
                        banner=media["bannerImage"],
                        source=media["source"],
                        hashtag=media["hashtag"],
                        synonyms=media["synonyms"],
                        score=dict(
                            mean=media["meanScore"],
                            average=media["averageScore"],
                        ),
                        next_airing=media["nextAiringEpisode"],
                        trailer=media["trailer"],
                        staff=media["staff"],
                        characters=media["characters"],
                        volumes=media["volumes"],
                        popularity=media["popularity"],
                        rankings=[
                            Ranking(
                                type=i["type"],
                                all_time=i["allTime"],
                                format=i["format"],
                                rank=i["rank"],
                                year=i["year"],
                                season=i["season"],
                            )
                            for i in media["rankings"]
                        ],
                    )

                    manga_list.append(
                        MediaList(
                            id=item["id"],
                            status=item["status"],
                            score=item["score"],
                            progress=item["progress"],
                            repeat=item["repeat"],
                            priority=item["priority"],
                            start_date=item["startedAt"],
                            complete_date=item["completedAt"],
                            update_date=item["updatedAt"],
                            create_date=item["createdAt"],
                            media=manga,
                        )
                    )

                return anime_list, manga_list

            except Exception:
                pass
        return None

    async def get_list_item(self, name: str, id: int) -> Optional[MediaList]:
        """Returns list item from user.

        Args:
            name (str): Username.
            id (int): Media id.

        Returns:
            Optional[MediaList]: List item.
        """
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=LIST_ITEM_GET_QUERY,
                variables=dict(
                    name=name,
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
                item = data["data"]["MediaList"]
                return MediaList(
                    id=item["id"],
                    status=item["status"],
                    score=item["score"],
                    progress=item["progress"],
                    repeat=item["repeat"],
                    priority=item["priority"],
                    start_date=item["startedAt"],
                    complete_date=item["completedAt"],
                    update_date=item["updatedAt"],
                    create_date=item["createdAt"],
                )
            except Exception:
                pass
        return None

    async def get_activity(
        self,
        id: Union[int, str],
        content_type: str = "anime",
        page: int = 1,
        limit: int = 25,
    ) -> Optional[List[ListActivity]]:
        """Returns activity of a user.

        Args:
            id (Union[int, str]): Username or userid.
            content_type (str, optional): anime, manga, text or message. Defaults to "anime".
            page (int, optional): Current page. Defaults to 1.
            limit (int, optional): Maximum items per page. Defaults to 25.

        Raises:
            TypeError: If content type is not a string.
            TypeError: If id is invalid.

        Returns:
            Optional[List[ListActivity]]: User activity.
        """
        if isinstance(content_type, str):
            content_type = content_type.lower()
        else:
            raise TypeError(
                f"content_type argument must be a string, not '{content_type.__class__.__name__}'"
            )
        if isinstance(id, str) and id.isdecimal():
            id = int(id)
        elif isinstance(id, str):
            try:
                user = await self.get_user(name=id)
                id = user.id
            except Exception:
                raise TypeError(
                    f"id argument must be an int, not '{id.__class__.__name__}'"
                )
        elif not isinstance(id, int):
            raise TypeError(
                f"id argument must be an int, not '{id.__class__.__name__}'"
            )
        if content_type == "anime":
            return await self.get_anime_activity(user_id=id, page=page, limit=limit)
        elif content_type == "manga":
            return await self.get_manga_activity(user_id=id, page=page, limit=limit)
        elif content_type == "text":
            return await self.get_text_activity(user_id=id, page=page, limit=limit)
        elif content_type == "message":
            return await self.get_message_activity(user_id=id, page=page, limit=limit)

    async def get_anime_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[List[ListActivity]]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=LIST_ACTIVITY_QUERY,
                variables=dict(
                    user_id=user_id,
                    page=page,
                    per_page=limit,
                    activity_type="ANIME_LIST",
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
                items = data["data"]["Page"]["activities"]
                result = []

                for item in items:
                    media = item["media"]
                    anime = Anime(
                        id=media["id"],
                        title=media["title"],
                        url=media["siteUrl"],
                        episodes=media["episodes"],
                        description=media["description"],
                        format=media["format"],
                        status=media["status"],
                        duration=media["duration"],
                        genres=media["genres"],
                        is_adult=media["isAdult"],
                        tags=media["tags"],
                        studios=media["studios"],
                        start_date=media["startDate"],
                        end_date=media["endDate"],
                        season=dict(
                            name=media["season"],
                            year=media["seasonYear"],
                            number=media["seasonInt"],
                        ),
                        country=media["countryOfOrigin"],
                        cover=media["coverImage"],
                        banner=media["bannerImage"],
                        source=media["source"],
                        hashtag=media["hashtag"],
                        synonyms=media["synonyms"],
                        score=dict(
                            mean=media["meanScore"],
                            average=media["averageScore"],
                        ),
                        next_airing=media["nextAiringEpisode"],
                        trailer=media["trailer"],
                        staff=media["staff"],
                        characters=media["characters"],
                        popularity=media["popularity"],
                        rankings=[
                            Ranking(
                                type=i["type"],
                                all_time=i["allTime"],
                                format=i["format"],
                                rank=i["rank"],
                                year=i["year"],
                                season=i["season"],
                            )
                            for i in media["rankings"]
                        ],
                    )

                    result.append(
                        ListActivity(
                            id=item["id"],
                            status=item["status"],
                            progress=item["progress"],
                            url=item["siteUrl"],
                            date=item["createdAt"],
                            media=anime,
                        )
                    )

                return result
            except Exception:
                pass
        return None

    async def get_manga_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[List[ListActivity]]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        MANGA_ACTIVITY_QUERY = LIST_ACTIVITY_QUERY.replace(
            "episodes", "chapters\nvolumes"
        )
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=MANGA_ACTIVITY_QUERY,
                variables=dict(
                    user_id=user_id,
                    page=page,
                    per_page=limit,
                    activity_type="MANGA_LIST",
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
                items = data["data"]["Page"]["activities"]
                result = []

                for item in items:
                    media = item["media"]
                    manga = Manga(
                        id=media["id"],
                        title=media["title"],
                        url=media["siteUrl"],
                        chapters=media["chapters"],
                        description=media["description"],
                        status=media["status"],
                        genres=media["genres"],
                        is_adult=media["isAdult"],
                        tags=media["tags"],
                        studios=media["studios"],
                        start_date=media["startDate"],
                        end_date=media["endDate"],
                        season=dict(
                            name=media["season"],
                            year=media["seasonYear"],
                            number=media["seasonInt"],
                        ),
                        country=media["countryOfOrigin"],
                        cover=media["coverImage"],
                        banner=media["bannerImage"],
                        source=media["source"],
                        hashtag=media["hashtag"],
                        synonyms=media["synonyms"],
                        score=dict(
                            mean=media["meanScore"],
                            average=media["averageScore"],
                        ),
                        next_airing=media["nextAiringEpisode"],
                        trailer=media["trailer"],
                        staff=media["staff"],
                        characters=media["characters"],
                        volumes=media["volumes"],
                        popularity=media["popularity"],
                        rankings=[
                            Ranking(
                                type=i["type"],
                                all_time=i["allTime"],
                                format=i["format"],
                                rank=i["rank"],
                                year=i["year"],
                                season=i["season"],
                            )
                            for i in media["rankings"]
                        ],
                    )

                    result.append(
                        ListActivity(
                            id=item["id"],
                            status=item["status"],
                            progress=item["progress"],
                            url=item["siteUrl"],
                            date=item["createdAt"],
                            media=manga,
                        )
                    )

                return result
            except Exception:
                pass
        return None

    async def get_text_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[List[TextActivity]]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=TEXT_ACTIVITY_QUERY,
                variables=dict(
                    user_id=user_id,
                    page=page,
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
                items = data["data"]["Page"]["activities"]
                result = []

                for item in items:
                    result.append(
                        TextActivity(
                            id=item["id"],
                            reply_count=item["replyCount"],
                            text=item["text"],
                            text_html=item["textHtml"],
                            url=item["siteUrl"],
                            date=item["createdAt"],
                            user=User(
                                id=item["user"]["id"],
                                name=item["user"]["name"],
                                image=item["user"]["avatar"],
                            ),
                        )
                    )

                return result
            except Exception:
                pass
        return None

    async def get_message_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[List[TextActivity]]:

        result = []

        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=MESSAGE_ACTIVITY_QUERY,
                variables=dict(
                    user_id=user_id,
                    page=page,
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
                items = data["data"]["Page"]["activities"]

                for item in items:
                    result.append(
                        TextActivity(
                            id=item["id"],
                            reply_count=item["replyCount"],
                            text=item["text"],
                            text_html=item["textHtml"],
                            url=item["siteUrl"],
                            date=item["createdAt"],
                            user=User(
                                id=item["messenger"]["id"],
                                name=item["messenger"]["name"],
                                image=item["messenger"]["avatar"],
                            ),
                            recipient=User(
                                id=item["recipient"]["id"],
                                name=item["recipient"]["name"],
                                image=item["recipient"]["avatar"],
                            ),
                        )
                    )
            except Exception:
                pass

        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True
        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=MESSAGE_ACTIVITY_QUERY_SENT,
                variables=dict(
                    user_id=user_id,
                    page=page,
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
                items = data["data"]["Page"]["activities"]

                for item in items:
                    result.append(
                        TextActivity(
                            id=item["id"],
                            reply_count=item["replyCount"],
                            text=item["text"],
                            text_html=item["textHtml"],
                            url=item["siteUrl"],
                            date=item["createdAt"],
                            user=User(
                                id=item["messenger"]["id"],
                                name=item["messenger"]["name"],
                                image=item["messenger"]["avatar"],
                            ),
                            recipient=User(
                                id=item["recipient"]["id"],
                                name=item["recipient"]["name"],
                                image=item["recipient"]["avatar"],
                            ),
                        )
                    )
            except Exception:
                pass

        if len(result):
            return result

        return None

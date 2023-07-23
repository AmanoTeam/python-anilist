#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import List, Optional, Tuple, Union

import httpx

from .client_process import *

from .types import (
    Anime,
    Character,
    ListActivity,
    Manga,
    MediaList,
    PageInfo,
    Staff,
    TextActivity,
    User,
)
from .utils import (
    ANIME_GET_QUERY,
    ANIME_SEARCH_QUERY,
    API_URL,
    CHARACTER_GET_QUERY,
    CHARACTER_SEARCH_QUERY,
    HEADERS,
    LIST_ACTIVITY_QUERY,
    LIST_GET_QUERY_ANIME,
    LIST_GET_QUERY_MANGA,
    LIST_ITEM_GET_QUERY,
    MANGA_GET_QUERY,
    MANGA_SEARCH_QUERY,
    MESSAGE_ACTIVITY_QUERY,
    MESSAGE_ACTIVITY_QUERY_SENT,
    STAFF_GET_QUERY,
    STAFF_SEARCH_QUERY,
    TEXT_ACTIVITY_QUERY,
    USER_GET_QUERY,
    USER_SEARCH_QUERY,
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
        self,
        query: str,
        content_type: str = "anime",
        page: int = 1,
        limit: int = 10,
        pagination: bool = False,
    ) -> Optional[
        Union[
            tuple[Union[Anime, Manga, Character, Staff, User], PageInfo],
            Union[Anime, Manga, Character, Staff, User]]
    ]:
        """Used to search specified content type with the given query.

        Args:
            query (str): Search query.
            content_type (str, optional): anime, manga, character, staff or user. Defaults to "anime".
            page (int, optional): Current page. Defaults to 1.
            limit (int, optional): Maximum items per page. Defaults to 10.
            pagination (bool, optional): Option to return pagination info. Defaults to False.

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
            search, pages = await self.search_anime(query=query, page=page, limit=limit)
        elif content_type == "manga":
            search, pages = await self.search_manga(query=query, page=page, limit=limit)
        elif content_type in ["char", "character"]:
            search, pages = await self.search_character(
                query=query, page=page, limit=limit
            )
        elif content_type == "staff":
            search, pages = await self.search_staff(query=query, page=page, limit=limit)
        elif content_type == "user":
            search, pages = await self.search_user(query=query, page=page, limit=limit)
        else:
            raise TypeError("There is no such content type.")

        if pagination:
            return search, pages
        return search

    async def get(
        self,
        id: Union[int, str],
        content_type: str = "anime",
        page: int = 1,
        limit: int = 25,
        pagination: bool = False,
    ) -> Optional[tuple[Union[Anime, Manga, Character, Staff, List[MediaList], User], PageInfo]]:
        """Gets specified item from given id.

        Args:
            id (Union[int, str]): Item id.
            content_type (str, optional): anime, manga, character, staff, list_anime, list_manga or user. Defaults to "anime".
            page (int, optional): Current page. Defaults to 1. Only used for lists.
            limit (int, optional): Maximum items per page. Defaults to 25. Only used for lists.
            pagination (bool, optional): Option to return pagination info. Only used for lists. Defaults to False.

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
            elif content_type == "list_anime" or content_type == "list_manga":
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
        elif content_type == "list_anime":
            anime, pages = await self.get_list(
                user_id=id, limit=limit, page=page, content_type="anime"
            )
            if pagination:
                return anime, pages
            return anime
        elif content_type == "list_manga":
            manga, pages = await self.get_list(
                user_id=id, limit=limit, page=page, content_type="manga"
            )
            if pagination:
                return manga, pages
            return manga
        elif content_type == "user":
            raise TypeError("id argument must be a string for the user object.")
        else:
            raise TypeError("There is no such content type.")

    async def search_anime(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[tuple[list[Anime], PageInfo]]:
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
        data: Optional[dict] = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        return process_search_anime(data)

    async def search_manga(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[tuple[list[Manga], PageInfo]]:
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
        data: dict = response.json()
        if need_to_close:
            await self.httpx.aclose()
            self.httpx = None
        return process_search_manga(data)

    async def search_character(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[tuple[list[Character], PageInfo]]:
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
        return process_search_character(data)

    async def search_staff(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[tuple[list[Staff], PageInfo]]:
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
        return process_search_staff(data)

    async def search_user(
        self, query: str, limit: int, page: int = 1
    ) -> Optional[tuple[list[User], PageInfo]]:
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
        return process_search_user(data)

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
        return process_get_anime(data)

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
        return process_get_manga(data)

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
        return process_get_character(data)

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
        return process_get_staff(data)

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
        return process_get_user(data)

    async def get_list(
        self, user_id: int, limit: int, page: int = 1, content_type: str = "anime"
    ) -> Optional[tuple[List[MediaList], List[MediaList]]]:
        need_to_close = False
        if not self.httpx:
            self.httpx = httpx.AsyncClient(http2=True)
            need_to_close = True

        is_manga = "manga" in content_type

        response = await self.httpx.post(
            url=API_URL,
            json=dict(
                query=LIST_GET_QUERY_ANIME if not is_manga else LIST_GET_QUERY_MANGA,
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

        return process_get_list(data, content_type)

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
        return process_get_list_item(data)

    async def get_activity(
        self,
        id: Union[int, str],
        content_type: str = "anime",
        page: int = 1,
        limit: int = 25,
        pagination: bool = False,
    ) -> Union[Optional[tuple[ListActivity, PageInfo]], Optional[ListActivity]]:
        """Returns activity of a user.

        Args:
            id (Union[int, str]): Username or userid.
            content_type (str, optional): anime, manga, text or message. Defaults to "anime".
            page (int, optional): Current page. Defaults to 1.
            limit (int, optional): Maximum items per page. Defaults to 25.
            pagination (bool, optional): Option to return pagination info. Defaults to False.

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
                raise TypeError(f"could not get userid from username '{id}'")
        elif not isinstance(id, int):
            raise TypeError(
                f"id argument must be an int, not '{id.__class__.__name__}'"
            )

        activity: ListActivity
        pages: PageInfo
        if content_type == "anime":
            activity, pages = await self.get_anime_activity(
                user_id=id, page=page, limit=limit
            )
        elif content_type == "manga":
            activity, pages = await self.get_manga_activity(
                user_id=id, page=page, limit=limit
            )
        elif content_type == "text":
            activity, pages = await self.get_text_activity(
                user_id=id, page=page, limit=limit
            )
        elif content_type == "message":
            return await self.get_message_activity(user_id=id, page=page, limit=limit)
        else:
            raise TypeError(f"Invalid content_type ({content_type}")

        if pagination:
            return activity, pages
        return activity

    async def get_anime_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[ListActivity], PageInfo]]:
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
        return process_get_anime_activity(data)

    async def get_manga_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[ListActivity], PageInfo]]:
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
        return process_get_manga_activity(data)

    async def get_text_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[TextActivity], PageInfo]]:
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
        return process_get_text_activity(data)

    async def get_message_activity(
        self, user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[TextActivity], PageInfo]]:
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

        return process_get_message_activity(data)

    async def get_message_activity_sent(
            self, user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[TextActivity], PageInfo]]:
        need_to_close = False

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

        return process_get_message_activity_sent(data)

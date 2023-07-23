#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import List, Optional, Union

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


def api_query(query, variables, url=API_URL, headers=HEADERS):
    with httpx.Client(http2=True) as session:
        response = session.post(url=url, json=dict(query=query, variables=variables), headers=headers)
    return response


class Client:
    def __init__(self):
        self.httpx = None

    def __enter__(self):
        self.httpx = httpx.Client()
        return self

    def __exit__(self, *args):
        self.httpx = None
        return None

    def search(
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
            search, pages = self.search_anime(query=query, page=page, limit=limit)
        elif content_type == "manga":
            search, pages = self.search_manga(query=query, page=page, limit=limit)
        elif content_type in ["char", "character"]:
            search, pages = self.search_character(query=query, page=page, limit=limit)
        elif content_type == "staff":
            search, pages = self.search_staff(query=query, page=page, limit=limit)
        elif content_type == "user":
            search, pages = self.search_user(query=query, page=page, limit=limit)
        else:
            raise TypeError("There is no such content type.")

        if pagination:
            return search, pages
        return search

    def get(
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
            Optional[Union[Anime, Manga, Character, Staff, List[MediaList], User], PageInfo]:
            Returned items.
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
                return self.get_user(name=id)
            elif content_type == "list_anime" or content_type == "list_manga":
                try:
                    user = self.get_user(name=id)
                    id = user.id
                except Exception:
                    raise TypeError("user not found")
            else:
                raise TypeError(
                    f"id argument must be a string, not '{id.__class__.__name__}'"
                )
        if content_type == "anime":
            return self.get_anime(id=id)
        elif content_type == "manga":
            return self.get_manga(id=id)
        elif content_type in ["char", "character"]:
            return self.get_character(id=id)
        elif content_type == "staff":
            return self.get_staff(id=id)
        elif content_type == "list_anime":
            anime, pages = self.get_list(
                user_id=id, limit=limit, page=page, content_type="anime"
            )
            if pagination:
                return anime, pages
            return anime
        elif content_type == "list_manga":
            manga, pages = self.get_list(
                user_id=id, limit=limit, page=page, content_type="manga"
            )
            if pagination:
                return manga, pages
            return manga
        elif content_type == "user":
            raise TypeError("id argument must be a string for the user object.")
        else:
            raise TypeError("There is no such content type.")

    @staticmethod
    def search_anime(query: str, limit: int, page: int = 1) -> Optional[tuple[list[Anime], PageInfo]]:
        response = api_query(ANIME_SEARCH_QUERY, dict(search=query, page=page, per_page=limit, MediaType="ANIME"))
        data: Optional[dict] = response.json()
        return process_search_anime(data)

    @staticmethod
    def search_manga(query: str, limit: int, page: int = 1) -> Optional[tuple[list[Manga], PageInfo]]:
        response = api_query(MANGA_SEARCH_QUERY, dict(search=query, page=page, per_page=limit, MediaType="MANGA"))
        data = response.json()
        return process_search_manga(data)

    @staticmethod
    def search_character(query: str, limit: int, page: int = 1) -> Optional[tuple[list[Character], PageInfo]]:
        response = api_query(CHARACTER_SEARCH_QUERY, dict(search=query, page=page, per_page=limit))
        data = response.json()
        return process_search_character(data)

    @staticmethod
    def search_staff(query: str, limit: int, page: int = 1) -> Optional[tuple[list[Staff], PageInfo]]:
        response = api_query(STAFF_SEARCH_QUERY, dict(search=query, page=page, per_page=limit))
        data = response.json()
        return process_search_staff(data)

    @staticmethod
    def search_user(query: str, limit: int, page: int = 1) -> Optional[tuple[list[User], PageInfo]]:
        response = api_query(USER_SEARCH_QUERY, dict(search=query, page=page, per_page=limit))
        data = response.json()
        return process_search_user(data)

    @staticmethod
    def get_anime(id: int) -> Optional[Anime]:
        response = api_query(ANIME_GET_QUERY, dict(id=id, MediaType="ANIME"))
        data = response.json()
        return process_get_anime(data)

    @staticmethod
    def get_manga(id: int) -> Optional[Manga]:
        response = api_query(MANGA_GET_QUERY, dict(id=id, MediaType="MANGA"))
        data = response.json()
        return process_get_manga(data)

    @staticmethod
    def get_character(id: int) -> Optional[Character]:
        response = api_query(CHARACTER_GET_QUERY, dict(id=id))
        data = response.json()
        return process_get_character(data)

    @staticmethod
    def get_staff(id: int) -> Optional[Staff]:
        response = api_query(STAFF_GET_QUERY, dict(id=id))
        data = response.json()
        return process_get_staff(data)

    @staticmethod
    def get_user(name: str) -> Optional[User]:
        response = api_query(USER_GET_QUERY, dict(name=name))
        data = response.json()
        return process_get_user(data)

    @staticmethod
    def get_list(
            user_id: int, limit: int, page: int = 1, content_type: str = "anime"
    ) -> Optional[tuple[list[MediaList], PageInfo]]:
        is_manga = "manga" in content_type
        response = api_query(LIST_GET_QUERY_ANIME if not is_manga else LIST_GET_QUERY_MANGA,
                             dict(user_id=user_id, page=page, per_page=limit))
        data = response.json()
        return process_get_list(data, content_type)

    @staticmethod
    def get_list_item(name: str, id: int) -> Optional[MediaList]:
        """Returns an item in a list item from user.

        Args:
            name (str): Username.
            id (int): Media id.

        Returns:
            Optional[MediaList]: List item.
        """
        response = api_query(LIST_ITEM_GET_QUERY, dict(name=name, d=id))
        data = response.json()
        return process_get_list_item(data)

    def get_activity(
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
            Union[Optional[(ListActivity, PageInfo)], Optional[ListActivity]]: User activity.
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
                user = self.get_user(name=id)
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
            activity, pages = self.get_anime_activity(user_id=id, page=page, limit=limit)
        elif content_type == "manga":
            activity, pages = self.get_manga_activity(user_id=id, page=page, limit=limit)
        elif content_type == "text":
            activity, pages = self.get_text_activity(user_id=id, page=page, limit=limit)
        elif content_type == "message":
            return self.get_message_activity(user_id=id, page=page, limit=limit)
        else:
            raise TypeError(f"Invalid content_type ({content_type}")

        if pagination:
            return activity, pages
        return activity

    @staticmethod
    def get_anime_activity(user_id: int, limit: int, page: int = 1) \
            -> Optional[tuple[list[ListActivity], PageInfo]]:
        response = api_query(LIST_ACTIVITY_QUERY,
                             dict(user_id=user_id, page=page, per_page=limit, activity_type="ANIME_LIST"))
        data = response.json()
        return process_get_anime_activity(data)

    @staticmethod
    def get_manga_activity(user_id: int, limit: int, page: int = 1) \
            -> Optional[tuple[list[ListActivity], PageInfo]]:
        MANGA_ACTIVITY_QUERY = LIST_ACTIVITY_QUERY.replace(
            "episodes", "chapters\nvolumes"
        )
        response = api_query(MANGA_ACTIVITY_QUERY,
                             dict(user_id=user_id, page=page, per_page=limit, activity_type="MANGA_LIST"))
        data = response.json()
        return process_get_manga_activity(data)

    @staticmethod
    def get_text_activity(
            user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[TextActivity], PageInfo]]:
        response = api_query(TEXT_ACTIVITY_QUERY, dict(user_id=user_id, page=page, per_page=limit))
        data = response.json()
        return process_get_text_activity(data)

    @staticmethod
    def get_message_activity(
            user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[TextActivity], PageInfo]]:
        response = api_query(MESSAGE_ACTIVITY_QUERY, dict(user_id=user_id, page=page, per_page=limit))
        data = response.json()
        return process_get_message_activity(data)

    @staticmethod
    def get_message_activity_sent(
            user_id: int, limit: int, page: int = 1
    ) -> Optional[tuple[list[TextActivity], PageInfo]]:
        response = api_query(MESSAGE_ACTIVITY_QUERY_SENT, dict(user_id=user_id, page=page, per_page=limit))
        data = response.json()
        return process_get_message_activity_sent(data)

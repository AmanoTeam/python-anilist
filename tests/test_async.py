# SPDX-License-Identifier: MIT
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/> and the python-anilist contributors

import pytest

import anilist


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "query, content_type",
    [
        ("Bakemonogatari", "anime"),
        ("Bakemonogatari", "manga"),
        ("Senjougahara", "character"),
        ("Chiwa Saitou", "staff"),
        ("travis", "user"),
    ],
)
async def test_search(query, content_type):
    client = anilist.AsyncClient()
    assert await client.search(query, content_type, pagination=True) is not None
    assert await client.search(query, content_type, pagination=False) is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, content_type",
    [
        ("5081", "anime"),
        ("101311", "manga"),
        ("22037", "character"),
        ("95061", "staff"),
        ("travis", "user"),
        ("travis", "list_anime"),
        ("travis", "list_manga"),
    ],
)
async def test_get(id, content_type):
    client = anilist.AsyncClient()
    if "list" in content_type:
        assert await client.get(id, content_type, pagination=True) is not None
        assert await client.get(id, content_type, pagination=False) is not None
    else:
        assert await client.get(id, content_type) is not None


@pytest.mark.asyncio
async def test_get_list_item():
    client = anilist.AsyncClient()
    assert await client.get_list_item("travis", 132405) is not None
    assert await client.get_list_item("travis", 30) is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "id, content_type",
    [
        ("travis", "anime"),
        ("travis", "manga"),
        ("travis", "text"),
    ],
)
async def test_get_activity(id, content_type):
    client = anilist.Client()
    assert client.get_activity(id, content_type) is not None

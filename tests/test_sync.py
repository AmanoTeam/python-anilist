import pytest
import anilist


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
def test_search(query, content_type):
    client = anilist.Client()
    assert client.search(query, content_type) is not None


@pytest.mark.parametrize(
    "id, content_type",
    [
        ("5081", "anime"),
        ("101311", "manga"),
        ("22037", "character"),
        ("95061", "staff"),
        ("travis", "user"),
        ("travis", "list"),
    ],
)
def test_get(id, content_type):
    client = anilist.Client()
    assert client.get(id, content_type) is not None


def test_get_list_item():
    client = anilist.Client()
    assert client.get_list_item("travis", "5081") is not None
    assert client.get_list_item("travis", "72451") is not None


@pytest.mark.parametrize(
    "id, content_type",
    [
        ("travis", "anime"),
        ("travis", "manga"),
        ("travis", "text"),
    ],
)
def test_get_activity(id, content_type):
    client = anilist.Client()
    assert client.get_activity(id, content_type) is not None

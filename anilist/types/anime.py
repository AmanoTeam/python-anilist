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

from .character import Character
from .cover import Cover
from .date import Date
from .next_airing import NextAiring
from .title import Title
from .trailer import Trailer
from .score import Score
from .season import Season
from typing import Callable, Dict, List


class Anime:
    def __init__(
        self,
        *,
        id: int,
        title: Dict,
        url: str,
        episodes: int = None,
        description: str = None,
        format: str = None,
        status: str = None,
        duration: int = None,
        genres: List[str] = None,
        tags: Dict = None,
        studios: Dict = None,
        start_date: Dict = None,
        end_date: Dict = None,
        season: Dict = None,
        country: str = None,
        cover: Dict = None,
        banner: str = None,
        source: str = None,
        hashtag: str = None,
        synonyms: List[str] = None,
        score: Dict = None,
        next_airing: Dict = None,
        trailer: Dict = None,
        staff: Dict = None,
        characters: Dict = None,
    ):
        self.id = id
        self.title = Title(
            romaji=title["romaji"], english=title["english"], native=title["native"]
        )
        if url:
            self.url = url
        if episodes:
            self.episodes = episodes
        if description:
            self.description = description
            if len(description) > 500:
                self.description_short = description[0:500]
        if format:
            self.format = format
        if status:
            self.status = status
        if duration:
            self.duration = duration
        if genres:
            self.genres = genres
        if tags and len(tags) > 0:
            self.tags = [tag["name"] for tag in tags]
        if studios and len(studios["nodes"]) > 0:
            self.studios = [studio["name"] for studio in studios["nodes"]]
        if start_date:
            self.start_date = Date(
                year=start_date["year"],
                month=start_date["month"],
                day=start_date["day"],
            )
        if end_date:
            self.end_date = Date(
                year=end_date["year"], month=end_date["month"], day=end_date["day"]
            )
        if season:
            self.season = Season(
                name=season["name"], year=season["year"], number=season["number"]
            )
        if country:
            self.country = country
        if cover:
            self.cover = Cover(
                medium=cover["medium"],
                large=cover["large"],
                extra_large=cover["extraLarge"],
            )
        if banner:
            self.banner = banner
        if source:
            self.source = source
        if hashtag:
            self.hashtag = hashtag
        if synonyms:
            self.synonyms = synonyms
        if score:
            self.score = Score(mean=score["mean"], average=score["average"])
        if next_airing:
            self.next_airing = NextAiring(
                time_until=next_airing["timeUntilAiring"],
                at=next_airing["airingAt"],
                episode=next_airing["episode"],
            )
        if trailer:
            self.trailer = Trailer(
                id=trailer["id"],
                thumbnail=trailer["thumbnail"],
                site=trailer["site"],
            )
        if staff and len(staff["edges"]) > 0:
            self.staff = [
                Character(
                    id=character["node"]["id"], name=character["node"]["name"]["full"]
                )
                for character in staff["edges"]
            ]
        if characters and len(characters["edges"]) > 0:
            self.characters = [
                Character(
                    id=character["node"]["id"], name=character["node"]["name"]["full"]
                )
                for character in characters["edges"]
            ]

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())

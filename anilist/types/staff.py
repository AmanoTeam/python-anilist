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

from .name import Name
from .image import Image
from .date import Date
from typing import Callable, Dict, List


class Studio:
    def __init__(
        self,
        *,
        id: int,
        name: str,
        is_animation_studio: bool = False,
        url: str = None,
        favourites: int = None,
    ) -> None:
        self.id = id
        self.name = name
        self.is_animation_studio = is_animation_studio
        if url:
            self.url = url
        if favourites:
            self.favourites = favourites


class Staff:
    def __init__(
        self,
        *,
        id: int,
        name: Dict,
        role: str = None,
        language: str = None,
        image: Dict = None,
        url: str = None,
        favorites: int = None,
        description: str = None,
        occupations: List[str] = None,
        gender: str = None,
        birth_date: Dict = None,
        death_date: Dict = None,
        age: int = None,
        years_active: int = None,
        home_town: str = None,
        is_favorite: bool = None,
    ):
        self.id = id
        self.name = Name(
            first=name["first"],
            full=name["full"],
            native=name["native"],
            last=name["last"],
        )
        if role:
            self.role = role
        if language:
            self.language = language
        if image:
            self.image = Image(medium=image["medium"], large=image["large"])
        if url:
            self.url = url
        if favorites:
            self.favorites = favorites
        if description:
            self.description = description
        if occupations:
            self.occupations = occupations
        if gender:
            self.gender = gender
        if birth_date:
            self.birth_date = Date(
                year=birth_date["year"],
                month=birth_date["month"],
                day=birth_date["day"],
            )
        if death_date:
            self.death_date = Date(
                year=death_date["year"],
                month=death_date["month"],
                day=death_date["day"],
            )
        if age:
            self.age = age
        if years_active:
            self.years_active = years_active
        if home_town:
            self.home_town = home_town
        if is_favorite is not None:
            self.is_favorite = is_favorite

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())
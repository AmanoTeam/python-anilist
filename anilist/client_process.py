from typing import Optional

from .types import (
    Anime,
    Character,
    FavouritesUnion,
    ListActivity,
    Manga,
    MediaList,
    PageInfo,
    Ranking,
    Staff,
    Statistic,
    StatisticsUnion,
    Studio,
    TextActivity,
    User,
)


def construct_manga_object(media) -> Manga:
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

    return manga


def construct_anime_object(media: dict) -> Anime:
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

    return anime


def construct_character_object(media: dict) -> Character:
    return Character(
        id=media["id"],
        name=media["name"],
        image=media["image"],
        url=media["siteUrl"],
        favorites=media["favourites"],
        description=media["description"],
        media=media["media"],
        is_favorite=media["isFavourite"],
    )


def construct_staff_object(media: dict) -> Staff:
    return Staff(
        id=media["id"],
        name=media["name"],
        language=media["languageV2"],
        image=media["image"],
        description=media["description"],
        gender=media["gender"],
        birth_date=media["dateOfBirth"],
        death_date=media["dateOfDeath"],
        url=media["siteUrl"],
        favorites=media["favourites"],
        occupations=media["primaryOccupations"],
        age=media["age"],
        years_active=media["yearsActive"],
        home_town=media["homeTown"],
    )


def construct_studio_object(media: dict) -> Studio:
    return Studio(
        id=media["id"],
        name=media["name"],
        is_animation_studio=media["isAnimationStudio"],
        url=media["siteUrl"],
        favourites=media["favourites"],
    )


def process_search_anime(data: Optional[dict]) -> Optional[tuple[list[Anime], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["media"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            results = [
                Anime(id=item["id"], title=item["title"], url=item["siteUrl"])
                for item in items
            ]
            return results, pagination
        except Exception:
            pass
    return None


def process_search_manga(data: Optional[dict]) -> Optional[tuple[list[Manga], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["media"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            results = [
                Manga(id=item["id"], title=item["title"], url=item["siteUrl"])
                for item in items
            ]
            return results, pagination
        except Exception:
            pass
    return None


def process_search_character(data: dict) -> Optional[tuple[list[Character], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["characters"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            results = [
                Character(id=item["id"], name=item["name"]) for item in items
            ]
            return results, pagination
        except Exception:
            pass
    return None


def process_search_staff(data) -> Optional[tuple[list[Staff], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["staff"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            results = [Staff(id=item["id"], name=item["name"]) for item in items]
            return results, pagination
        except Exception:
            pass
    return None


def process_search_user(data) -> Optional[tuple[list[User], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["users"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            results = [
                User(id=item["id"], name=item["name"], image=item["avatar"])
                for item in items
            ]
            return results, pagination
        except Exception:
            pass
    return None


def process_get_anime(data) -> Optional[Anime]:
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
                relations=item["relations"],
            )
        except Exception:
            pass
    return None


def process_get_manga(data) -> Optional[Manga]:
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
                relations=item["relations"],
            )
        except Exception:
            pass
    return None


def process_get_character(data) -> Optional[Character]:
    if data["data"]:
        try:
            item = data["data"]["Character"]
            return construct_character_object(item)
        except Exception:
            pass
    return None


def process_get_staff(data) -> Optional[Staff]:
    if data["data"]:
        try:
            item = data["data"]["Staff"]
            return construct_staff_object(item)
        except Exception:
            pass
    return None


def process_get_user(data) -> Optional[User]:
    if data["data"]:
        try:
            item = data["data"]["User"]

            favourites = FavouritesUnion(
                anime=[construct_anime_object(i) for i in item["favourites"]["anime"]["nodes"]],
                manga=[construct_manga_object(i) for i in item["favourites"]["manga"]["nodes"]],
                characters=[construct_character_object(i) for i in item["favourites"]["characters"]["nodes"]],
                staff=[construct_staff_object(i) for i in item["favourites"]["staff"]["nodes"]],
                studios=[construct_studio_object(i) for i in item["favourites"]["studios"]["nodes"]],
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


def process_get_list(data: dict, content_type: str) -> Optional[tuple[list[MediaList], PageInfo]]:
    is_manga = "manga" in content_type
    res = []
    if data["data"]:
        try:
            if not is_manga:
                pg = data["data"]["anime"]["pageInfo"]
            else:
                pg = data["data"]["manga"]["pageInfo"]
            pagination = PageInfo(
                total_items=pg["total"],
                current=pg["currentPage"],
                last=pg["lastPage"],
            )

            if not is_manga:
                for item in data["data"]["anime"]["mediaList"]:
                    media = item["media"]
                    anime = construct_anime_object(media)

                    res.append(
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

            if is_manga:
                for item in data["data"]["manga"]["mediaList"]:
                    media = item["media"]
                    manga = construct_manga_object(media)

                    res.append(
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

            return res, pagination

        except Exception:
            pass
    return None


def process_get_list_item(data: dict) -> Optional[MediaList]:
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


def process_get_anime_activity(data) -> Optional[tuple[list[ListActivity], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["activities"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            result = []

            for item in items:
                media = item["media"]

                anime = construct_anime_object(media)

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

            return result, pagination
        except Exception:
            pass
    return None


def process_get_manga_activity(data: dict) -> Optional[tuple[list[ListActivity], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["activities"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

            result = []

            for item in items:
                media = item["media"]
                manga = construct_manga_object(media)

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

            return result, pagination
        except Exception:
            pass
    return None


def process_get_text_activity(data: dict) -> Optional[tuple[list[TextActivity], PageInfo]]:
    if data["data"]:
        try:
            items = data["data"]["Page"]["activities"]
            page = data["data"]["Page"]["pageInfo"]
            pagination = PageInfo(
                total_items=page["total"],
                current=page["currentPage"],
                last=page["lastPage"],
            )

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

            return result, pagination
        except Exception:
            pass
    return None


def process_get_message_activity(data: dict) -> Optional[tuple[list[TextActivity], PageInfo]]:
    result = []

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


def process_get_message_activity_sent(data: dict) -> Optional[tuple[list[TextActivity], PageInfo]]:
    return process_get_message_activity(data)  # Currently they are the same

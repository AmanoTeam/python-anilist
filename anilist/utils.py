#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

API_URL = "https://graphql.anilist.co"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Search
ANIME_SEARCH_QUERY = """
query($id: Int, $search: String, $page: Int = 1, $per_page: Int = 10) {
    Page(page: $page, perPage: $per_page) {
        media(id: $id, search: $search, type: ANIME, sort: POPULARITY_DESC) {
            id
            title {
                romaji
                english
                native
            }
            siteUrl
        }
    }
}
"""

MANGA_SEARCH_QUERY = """
query($id: Int, $search: String, $page: Int = 1, $per_page: Int = 10) {
    Page(page: $page, perPage: $per_page) {
        media(id: $id, search: $search, type: MANGA, sort: POPULARITY_DESC) {
            id
            title {
                romaji
                english
                native
            }
            siteUrl
        }
    }
}
"""

CHARACTER_SEARCH_QUERY = """
query($search: String, $page: Int = 1, $per_page: Int = 10) {
    Page(page: $page, perPage: $per_page) {
        characters(search: $search) {
            id
            name {
                first
                full
                native
                last
            }
        }
    }
}
"""

STAFF_SEARCH_QUERY = """
query ($name: String, $page: Int = 1, $per_page: Int = 10) {
    Page(page: $page, perPage: $per_page) {
        staff(search: $name, sort: SEARCH_MATCH) {
            id
            name {
                first
                full
                native
                last
            }
        }
    }
}
"""

USER_SEARCH_QUERY = """
    query ($name: String, $page: Int = 1, $per_page: Int = 10) {
        Page(page: $page, perPage: $per_page) {
            users(search: $name, sort: SEARCH_MATCH) {
                id
                name
                avatar {
                    large
                    medium
                }
            }
        }
    }
"""

# Get
ANIME_GET_QUERY = """
query($id: Int) {
    Page(page: 1, perPage: 1) {
        media(id: $id, type: ANIME) {
            id
            title {
                romaji
                english
                native
            }
            siteUrl
            episodes
            description
            format
            status
            duration
            genres
            isAdult
            tags {
                name
            }
            studios {
                nodes {
                    name
                }
            }
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            season
            seasonYear
            seasonInt
            countryOfOrigin
            coverImage {
                medium
                large
                extraLarge
            }
            bannerImage
            source
            hashtag
            synonyms
            meanScore
            averageScore
            popularity
            rankings {
                type
                allTime
                format
                rank
                year
                season
            }
            nextAiringEpisode {
                timeUntilAiring
                airingAt
                episode
            }
            trailer {
                id
                thumbnail
                site
            }
            staff(sort: FAVOURITES_DESC) {
                edges {
                    node {
                        name {
                            first
                            full
                            native
                            last
                        }
                        id
                    }
                }
            }
            characters(sort: FAVOURITES_DESC) {
                edges {
                    node {
                        name {
                            first
                            full
                            native
                            last
                        }
                        id
                    }
                    role
                }
            }
        }
    }
}
"""

MANGA_GET_QUERY = """
query($id: Int) {
    Page(page: 1, perPage: 1) {
        media(id: $id, type: MANGA) {
            id
            title {
                romaji
                english
                native
            }
            siteUrl
            chapters
            description
            status
            genres
            isAdult
            tags {
                name
            }
            studios {
                nodes {
                    name
                }
            }
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            season
            seasonYear
            seasonInt
            countryOfOrigin
            coverImage {
                medium
                large
                extraLarge
            }
            bannerImage
            source
            hashtag
            synonyms
            meanScore
            averageScore
            popularity
            rankings {
                type
                allTime
                format
                rank
                year
                season
            }
            nextAiringEpisode {
                timeUntilAiring
                airingAt
                episode
            }
            trailer {
                id
                thumbnail
                site
            }
            staff(sort: FAVOURITES_DESC) {
                edges {
                    node {
                        name {
                            first
                            full
                            native
                            last
                        }
                        id
                    }
                }
            }
            characters(sort: FAVOURITES_DESC) {
                edges {
                    node {
                        name {
                            first
                            full
                            native
                            last
                        }
                        id
                    }
                    role
                }
            }
            volumes
        }
    }
}
"""

CHARACTER_GET_QUERY = """
query($id: Int) {
    Character(id: $id, sort: FAVOURITES_DESC) {
        id
        name {
            first
            full
            native
            last
        }
        image {
            medium
            large
        }
        siteUrl
        favourites
        description
        media {
            edges {
                node {
                    title {
                        romaji
                        english
                        native
                    }
                    id
                    type
                }
            }
        }
        isFavourite
    }
}
"""

STAFF_GET_QUERY = """
query($id: Int) {
    Staff(id: $id, sort: FAVOURITES_DESC) {
        id
        name {
            first
            middle
            last
            full
            native
            userPreferred
        }
        languageV2
        image {
            large
            medium
        }
        description
        primaryOccupations
        gender
        dateOfBirth {
            year
            month
            day
        }
        dateOfDeath {
            year
            month
            day
        }
        age
        yearsActive
        homeTown
        siteUrl
        favourites
    }
}
"""

USER_GET_QUERY = """
query ($name: String) {
    User(name: $name) {
        id
        name
        about
        avatar {
            large
            medium
        }
        bannerImage
        favourites {
            anime {
                nodes {
                    id
                    title {
                        romaji
                        english
                        native
                    }
                    siteUrl
                    genres
                    isAdult
                    coverImage {
                        medium
                        large
                        extraLarge
                    }
                    bannerImage
                    source
                    hashtag
                    synonyms
                    averageScore
                    meanScore
                }
            }
            manga {
                nodes {
                    id
                    title {
                        romaji
                        english
                        native
                        userPreferred
                    }
                    siteUrl
                    genres
                    isAdult
                    coverImage {
                        medium
                        large
                        extraLarge
                    }
                    bannerImage
                    source
                    hashtag
                    synonyms
                    averageScore
                    meanScore
                }
            }
            characters {
                nodes {
                    id
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    image {
                        large
                        medium
                    }
                    description
                    gender
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    age
                    siteUrl
                    favourites
                }
            }
            staff {
                nodes {
                    id
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    languageV2
                    image {
                        large
                        medium
                    }
                    description
                    primaryOccupations
                    gender
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    dateOfDeath {
                        year
                        month
                        day
                    }
                    age
                    yearsActive
                    homeTown
                    siteUrl
                    favourites
                }
            }
            studios {
                nodes {
                    id
                    name
                    isAnimationStudio
                    siteUrl
                    favourites
                }
            }
        }
        statistics {
            anime {
                count
                meanScore
                minutesWatched
                episodesWatched
                statuses {
                    status
                    count
                }
                genres(sort: COUNT_DESC) {
                    genre
                    count
                }
                tags(sort: COUNT_DESC) {
                    tag {
                        name
                    }
                    count
                }
            }
            manga {
                count
                meanScore
                chaptersRead
                volumesRead
                statuses {
                    status
                    count
                }
                genres(sort: COUNT_DESC) {
                    genre
                    count
                }
                tags(sort: COUNT_DESC) {
                    tag {
                        name
                    }
                    count
                }
            }
        }
        siteUrl
        donatorTier
        donatorBadge
        createdAt
        updatedAt
        options {
            profileColor
        }
    }
}
"""

LIST_GET_QUERY = """
query ($user_id: Int, $page: Int = 1, $per_page: Int = 25) {
    anime: Page(page: $page, perPage: $per_page) {
        mediaList(userId: $user_id, sort: UPDATED_TIME_DESC, type: ANIME) {
            id
            status
            score(format: POINT_100)
            progress
            repeat
            priority
            startedAt {
                year
                month
                day
            }
            completedAt {
                year
                month
                day
            }
            updatedAt
            createdAt
            media {
                type
                id
                title {
                    romaji
                    english
                    native
                }
                siteUrl
                episodes
                description
                format
                status
                duration
                genres
                isAdult
                tags {
                    name
                }
                studios {
                    nodes {
                        name
                    }
                }
                startDate {
                    year
                    month
                    day
                }
                endDate {
                    year
                    month
                    day
                }
                season
                seasonYear
                seasonInt
                countryOfOrigin
                coverImage {
                    medium
                    large
                    extraLarge
                }
                bannerImage
                source
                hashtag
                synonyms
                meanScore
                averageScore
                popularity
                rankings {
                    type
                    allTime
                    format
                    rank
                    year
                    season
                }
                nextAiringEpisode {
                    timeUntilAiring
                    airingAt
                    episode
                }
                trailer {
                    id
                    thumbnail
                    site
                }
                staff(sort: FAVOURITES_DESC) {
                    edges {
                        node {
                            name {
                                first
                                full
                                native
                                last
                            }
                            id
                        }
                    }
                }
                characters(sort: FAVOURITES_DESC) {
                    edges {
                        node {
                            name {
                                first
                                full
                                native
                                last
                            }
                            id
                        }
                        role
                    }
                }
            }
        }
    }
    manga: Page(page: $page, perPage: $per_page) {
        mediaList(userId: $user_id, sort: UPDATED_TIME_DESC, type: MANGA) {
            id
            status
            score(format: POINT_100)
            progress
            repeat
            priority
            startedAt {
                year
                month
                day
            }
            completedAt {
                year
                month
                day
            }
            updatedAt
            createdAt
            media {
                type
                id
                title {
                    romaji
                    english
                    native
                }
                siteUrl
                chapters
                volumes
                description
                format
                status
                duration
                genres
                isAdult
                tags {
                    name
                }
                studios {
                    nodes {
                        name
                    }
                }
                startDate {
                    year
                    month
                    day
                }
                endDate {
                    year
                    month
                    day
                }
                season
                seasonYear
                seasonInt
                countryOfOrigin
                coverImage {
                    medium
                    large
                    extraLarge
                }
                bannerImage
                source
                hashtag
                synonyms
                meanScore
                averageScore
                popularity
                rankings {
                    type
                    allTime
                    format
                    rank
                    year
                    season
                }
                nextAiringEpisode {
                    timeUntilAiring
                    airingAt
                    episode
                }
                trailer {
                    id
                    thumbnail
                    site
                }
                staff(sort: FAVOURITES_DESC) {
                    edges {
                        node {
                            name {
                                first
                                full
                                native
                                last
                            }
                            id
                        }
                    }
                }
                characters(sort: FAVOURITES_DESC) {
                    edges {
                        node {
                            name {
                                first
                                full
                                native
                                last
                            }
                            id
                        }
                        role
                    }
                }
            }
        }
    }
}
"""

LIST_ITEM_GET_QUERY = """
query ($name: String, $id: Int) {
    MediaList(userName: $name, mediaId: $id) {
        id
        status
        score(format: POINT_100)
        progress
        repeat
        priority
        startedAt {
            year
            month
            day
        }
        completedAt {
            year
            month
            day
        }
        updatedAt 
        createdAt
    }
}
"""

# Activity
LIST_ACTIVITY_QUERY = """
query ($user_id: Int, $activity_type: ActivityType, $page: Int = 1, $per_page: Int = 25) {
    Page(page: $page, perPage: $per_page) {
        activities(userId: $user_id, type: $activity_type, sort: ID_DESC) {
            ... on ListActivity {
                type
                id
                status
                progress
                siteUrl
                createdAt
                media {
                    type
                    id
                    title {
                        romaji
                        english
                        native
                    }
                    siteUrl
                    episodes
                    chapters
                    volumes
                    description
                    format
                    status
                    duration
                    genres
                    isAdult
                    tags {
                        name
                    }
                    studios {
                        nodes {
                            name
                        }
                    }
                    startDate {
                        year
                        month
                        day
                    }
                    endDate {
                        year
                        month
                        day
                    }
                    season
                    seasonYear
                    seasonInt
                    countryOfOrigin
                    coverImage {
                        medium
                        large
                        extraLarge
                    }
                    bannerImage
                    source
                    hashtag
                    synonyms
                    meanScore
                    averageScore
                    popularity
                    rankings {
                        type
                        allTime
                        format
                        rank
                        year
                        season
                    }
                    nextAiringEpisode {
                        timeUntilAiring
                        airingAt
                        episode
                    }
                    trailer {
                        id
                        thumbnail
                        site
                    }
                    staff(sort: FAVOURITES_DESC) {
                        edges {
                            node {
                                name {
                                    first
                                    full
                                    native
                                    last
                                }
                                id
                            }
                        }
                    }
                    characters(sort: FAVOURITES_DESC) {
                        edges {
                            node {
                                name {
                                    first
                                    full
                                    native
                                    last
                                }
                                id
                            }
                            role
                        }
                    }
                }
            }
        }
    }
}
"""

TEXT_ACTIVITY_QUERY = """
query ($user_id: Int, $page: Int = 1, $per_page: Int = 25) {
    Page(page: $page, perPage: $per_page) {
        activities(userId: $user_id, type: TEXT, sort: ID_DESC) {
            ... on TextActivity {
                id
                replyCount
                text(asHtml: false)
                textHtml: text(asHtml: true)
                siteUrl
                createdAt
                user {
                    id
                    name
                    avatar {
                        large
                        medium
                    }
                }
            }
        }
    }
}
"""

MESSAGE_ACTIVITY_QUERY = """
query ($user_id: Int, $page: Int = 1, $per_page: Int = 25) {
    Page(page: $page, perPage: $per_page) {
        activities(userId: $user_id, type: MESSAGE, sort: ID_DESC) {
            ... on MessageActivity {
                id
              	recipient {
                  id
                  name
                  avatar {
                    large
                    medium
                  }
                }
              	messenger {
                  id
                  name
                  avatar {
                    large
                    medium
                  }
                }
                replyCount
                text: message(asHtml: false)
              	textHtml: message(asHtml: true)
              	siteUrl
              	createdAt
            }
        }
    }
}
"""

MESSAGE_ACTIVITY_QUERY_SENT = """
query ($user_id: Int, $page: Int = 1, $per_page: Int = 25) {
    Page(page: $page, perPage: $per_page) {
        activities(messengerId: $user_id, type: MESSAGE, sort: ID_DESC) {
            ... on MessageActivity {
                id
              	recipient {
                  id
                  name
                  avatar {
                    large
                    medium
                  }
                }
              	messenger {
                  id
                  name
                  avatar {
                    large
                    medium
                  }
                }
                replyCount
                text: message(asHtml: false)
              	textHtml: message(asHtml: true)
              	siteUrl
              	createdAt
            }
        }
    }
}
"""

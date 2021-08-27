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
query($id: Int, $per_page: Int, $search: String) {
    Page(page: 1, perPage: $per_page) {
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

CHARACTER_SEARCH_QUERY = """
query($per_page: Int, $search: String) {
    Page(page: 1, perPage: $per_page) {
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

MANGA_SEARCH_QUERY = """
query($id: Int, $per_page: Int, $search: String) {
    Page(page: 1, perPage: $per_page) {
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
                }
            }
        }
        isFavourite
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

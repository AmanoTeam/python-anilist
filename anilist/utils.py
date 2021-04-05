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
            characters(role: MAIN) {
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
            characters(role: MAIN) {
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
            volumes
        }
    }
}
"""

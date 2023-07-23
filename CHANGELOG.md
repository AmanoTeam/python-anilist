<!--
  ~ Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
  ~ 
  ~ SPDX-License-Identifier: MIT
  -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## 1.1.0 (July 23rd, 2023)

Large refactoring to remove duplicate code.

### Changed

- Rebase all classes to be subclasses of a main "Object" class, or "Hashable" if the class has an id. This was to avoid the repetitive __repr__, __str__, and raw() definitions in every class, as well as allow things like implementation of __eq__ to all classes by writing it in only one place. ([commit](https://github.com/r-hensley/python-anilist/commit/15d57c753c7b5eb6624bdbfb719f82fc68f743db))
- Add some basic info to the readme, as well as an example.
- Consolidate duplicated code between the synhronous and asynchronous files into one "client_process.py" file ([commit](https://github.com/r-hensley/python-anilist/commit/a568ac77883ee2225287df849a59dea7cd658253))
- The IDs being used for one of the tests in the test file were no longer found on the tested user's profile, so they have been updated to a new ID for the sake of a successful test ([commit](https://github.com/r-hensley/python-anilist/commit/b0825364e22d2ad3ee9f18e2cb1f302081e52e00))
- Consolidate API calls into a single "api_query()" function ([commit](https://github.com/r-hensley/python-anilist/commit/4066a5371a1573ab6e28e1ab5d6901af678ba184))
- Changed all the "try ... except ... pass" blocks to "try ... except ... raise" to ensure proper propagation of errors. If a user wishes to ignore all errors they should do that in their program rather than the library suppressing all errors with no logs ([commit](https://github.com/r-hensley/python-anilist/commit/cba69086587ac164d5fc55eddccc58f9e5680b7b))

## 1.0.9 (February 16th, 2022)

### Added

- hotfix: queries: add missing `pageInfo` from https://github.com/AmanoTeam/python-anilist/commit/2c9f7efd5127371fd09b6630c1564c13755131d1.

## 1.0.8 (February 16th, 2022)

### Added

- `.relations` for animes and mangas.

### Changed

- Separate queries into separate files.
- Happy new year (late).

## 1.0.7 (January 18th, 2022)

### Added

- Pagination.
- `rewatched` and `reread` activity status.

### Changed

- Fix .vscode gitignore.
- Fix user and staff search queries.
- Update get_activity type error.

## 1.0.6 (October 20th, 2021)

### Added

- Support for `Python 3.10`.

### Changed

- Fixed subpackages.

## 1.0.5 (August 4th, 2021)

### Added

- List get query.
- Staff get query.
- Staff search query.
- User search query.
- Fixed message activity.
- Added `alternative` attribute to the Name object.
- Message activities.
- Support for users, favourites, staff, statistics, rankings, and studios.
- Support for user list and text activities.

### Changed

- Fixed typos & bugs.
- Added `is_adult` to both anime and manga objects.
- Added user object to text activities.
- Added profile colors and other fields to the user object.
- Added timestamps to the date object.
- Tidied up and organized required fields in every object.

## 1.0.4 (April 5th, 2021)

### Changed

- Hotfix, fix a typo on get manga.

## 1.0.3 (April 4th, 2021)

### Added

- Support for characters.

### Changed

- HTTP2 enabled (async mode only).

## 1.0.2 (March 8th, 2021)

### Added

- Support for mangas.

### Changed

- Some bug fixes.

## 1.0.1 (March 8th, 2021)

### Changed

- Bug fixes.

## 1.0.0 (March 8th, 2021)

* First release

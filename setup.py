#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Amano Team <https://amanoteam.com/> and the python-anilist contributors

from setuptools import find_packages, setup

if __name__ == "__main__":
    with open("./README.md", "r") as file:
        readme = file.read()

    with open("./CHANGELOG.md", "r") as file:
        readme += "\n\n"
        readme += file.read()

    setup(
        long_description=readme,
        long_description_content_type="text/markdown",
    )

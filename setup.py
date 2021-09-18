#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from setuptools import find_packages, setup

with open("README.md", "r") as file:
    readme = file.read()

with open("CHANGELOG.md", "r") as file:
    readme += "\n\n"
    readme += file.read()

setup(
    name="python-anilist",
    version="1.0.5",
    packages=find_packages(exclude=["tests*"]),
    install_requires=["httpx[http2]>=0.14"],
    url="https://github.com/AmanoTeam/python-anilist",
    python_requires=">=3.6",
    author="AmanoTeam",
    author_email="contact@amanoteam.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    description="A simple wrapper for Anilist",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="wrapper python anilist sync async asyncio httpx graphl api",
)

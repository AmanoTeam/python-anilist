from anilist import (
    __author__ as author,
    __email__ as email,
    __license__ as license,
    __version__ as version,
)
from setuptools import find_packages, setup

with open("README.md", "r") as file:
    readme = file.read()

setup(
    name="python-anilist",
    version=version,
    packages=find_packages(),
    install_requires=["httpx[http2]>=0.14"],
    url="https://github.com/AmanoTeam/python-anilist",
    python_requires=">=3.8",
    author=author,
    author_email=email,
    license=license,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
        "Programming Language :: Python :: 3 :: Only",
    ],
    description="A simple wrapper for Anilist",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="wrapper python anilist sync async asyncio httpx graphl api",
)

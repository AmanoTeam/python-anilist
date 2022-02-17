# SPDX-License-Identifier: MIT
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/> and the python-anilist contributors

# Provides compatibility functions and values for older Python versions.

from typing import Union
from pkgutil import get_data
from types import ModuleType
from os import PathLike

__all__ = (
    "read_text",
    "Package",
    "Resource",
)

Package = Union[str, ModuleType]
Resource = Union[str, PathLike]


def read_text(
    package: Package,
    resource: Resource,
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """Return the decoded string of the resource.

    The decoding-related arguments have the same semantics as those of
    bytes.decode().

    This function is a shim for importlib.resources.read_text.
    """

    if isinstance(resource, PathLike):
        resource = str(resource.__fspath__())

    if isinstance(package, str):
        data = get_data(package=package, resource=resource)
    else:
        data = get_data(package=package.__name__, resource=resource)

    if data is None:
        raise ImportError("Cannot find module or improper loader.")

    return data.decode(encoding=encoding, errors=errors)

# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Amano Team <https://amanoteam.com/> and the python-anilist contributors

from typing import TYPE_CHECKING, Union
from pkgutil import get_data

if TYPE_CHECKING:
    from types import ModuleType

    Package = Union[str, ModuleType]


def read_text(
    package: Package,
    resource: str,
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """Return the decoded string of the resource.

    The decoding-related arguments have the same semantics as those of
    bytes.decode().

    This function is essentially a "polyfill" for
    importlib.resources.read_text.
    """
    if isinstance(package, str):
        data = get_data(package=package, resource=resource)
    else:
        data = get_data(package=package.__name__, resource=resource)

    if data is None:
        raise ImportError("Cannot find module or improper loader.")

    return data.decode(encoding=encoding, errors=errors)

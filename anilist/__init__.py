#!/usr/bin/env python3
# Copyright (C) 2021 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

__author__ = "AmanoTeam"
__email__ = "contact@amanoteam.com"
__license__ = "MIT"
__version__ = "1.0.5"

from . import types

from .sync_client import Client
from .async_client import Client as AsyncClient

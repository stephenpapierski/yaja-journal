# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 Stephen Papierski
Copyright (c) 2019 - 2022 AppSeed.us
"""

from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    url_prefix=''
)

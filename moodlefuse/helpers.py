#!/usr/bin/env python
# encoding: utf-8

import os

from functools import wraps

from moodlefuse.models.users import User
from moodlefuse.services import USERS


def get_cache_path_based_on_location(location):
    config_folder = os.path.join(os.path.expanduser('~'), '.moodlefuse')
    cache_base = os.path.join(config_folder, 'cache')
    return cache_base + '/' + "_".join(location)


def throws_moodlefuse_error(moodlefuse_error):
    def inner(f):
        def wrapped(*args):
            try:
                return f(*args)
            except Exception:
                raise moodlefuse_error()
        return wraps(f)(wrapped)
    return inner


def get_password_for_user(username):
    return USERS.get(
        User,
        username
    ).password

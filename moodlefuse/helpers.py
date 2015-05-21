#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.models.users import User
from moodlefuse.services import USERS


def get_cache_path_based_on_location(location):
    config_folder = os.path.join(os.path.expanduser('~'), '.moodlefuse')
    cache_base = os.path.join(config_folder, 'cache')
    return cache_base + '/' + "_".join(location)


def get_password_for_user(username):
    return USERS.get(
        User,
        username
    ).password

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.models.users import User
from moodlefuse.services import USERS

CACHE_BASE = '/tmp'


def get_cache_path_based_on_location(location):
    return CACHE_BASE + '/' + "_".join(location)


def get_password_for_user(username):
    return USERS.get(
        User,
        username
    ).password

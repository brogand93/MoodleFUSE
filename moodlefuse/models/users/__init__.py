#!/usr/bin/env python
# encoding: utf-8

"""This module creates a user service.
"""

from moodlefuse.model_manager import Service
from moodlefuse.models.users.models import User


class UsersService(Service):
    __model__ = User

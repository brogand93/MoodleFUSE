#!/usr/bin/env python
# encoding: utf-8

"""This module creates a user service.
"""

from moodlefuse.model_manager import Service
from moodlefuse.models.users.models import User

from moodlefuse.session import session


class UsersService(Service):
    __model__ = User

    def get_password(self, primarykey):
        user_object = session.query(User).filter(User.username == primarykey).one()
        return user_object.password

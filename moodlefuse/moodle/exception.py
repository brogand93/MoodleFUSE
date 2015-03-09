#!/usr/bin/env python
# encoding: utf-8

"""Class to handle Exceptions relating to Moodle actions
"""

from moodlefuse.exception import MoodleFuseException

class MoodleException(MoodleFuseException):

    def __init__(self):
        self.debug_info = "Moodle action failed to complete"

    def __str__(self):
        return str(MoodleFuseException + self.debug_info)


class LoginException(MoodleException):

    def __init__(self, username):
        self.debug_info = "Failed to log into account"

    def __str__(self):
        return str(MoodleException + self.debug_info)


class NotFoundException(MoodleException):

    def __init__(self, url):
        self.debug_info = "Coukd not connect to the url" + url

    def __str__(self):
        return repr(MoodleException + self.debug_info)
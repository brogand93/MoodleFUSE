#!/usr/bin/env python
# encoding: utf-8

"""Class to handle Exceptions relating to Moodle actions
"""

from moodlefuse.exception import MoodleFuseException


class MoodleException(MoodleFuseException):
    def __init__(self, specific_debug_info):
        debug_info = "Moodle action failed to complete - " + specific_debug_info
        super(MoodleException, self).__init__(debug_info)


class UnableToToggleEditing(MoodleException):
    def __init__(self):
        debug_info = "Could not toggle editing button"
        super(UnableToToggleEditing, self).__init__(debug_info)


class LoginException(MoodleException):
    def __init__(self):
        debug_info = "Failed to log into account for username provided in config"
        super(MoodleException, self).__init__(debug_info)


class NotFoundException(MoodleException):
    def __init__(self):
        debug_info = "Could not connect to the login URL provided in config"
        super(NotFoundException, self).__init__(debug_info)

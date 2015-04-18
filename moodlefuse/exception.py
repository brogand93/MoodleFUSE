#!/usr/bin/env python
# encoding: utf-8

"""Class to handle Exceptions relating to MoodleFUSE actions
"""


class MoodleFuseException(Exception):
    def __init__(self, debug_info):
        exception_reason = "ERROR ENCOUNTERED: MoodleFUSE has encountered an error."
        debug_info = debug_info
        self.message = exception_reason + debug_info

    def __str__(self):
        return self.message

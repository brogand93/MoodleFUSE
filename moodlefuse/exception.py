#!/usr/bin/env python
# encoding: utf-8

"""Class to handle Exceptions relating to MoodleFUSE actions
"""


class MoodleFuseException(BaseException):

    def __init__(self, debug_info):
        self.exception_reason = "ERROR ENCOUNTERED: MoodleFUSE has encountered an error."
        self.debug_info = debug_info

    def __str__(self):
        return str(
            self.exception_reason + '\n' + self.debug_info
        )

    def __add__(self, desired_addition):
        return str(self + desired_addition)

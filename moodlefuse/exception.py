#!/usr/bin/env python
# encoding: utf-8

class MoodleFuseException(BaseException):

    def __init__(self, debug_info):
        self.exception_reason = "ERROR ENCOUNTERED: MoodleFUSE has encountered an error."
        self.debug_info = debug_info

    def __str__(self):
        return repr(
            self.exception_reason + '\n' + self.debug_info
        )

    def __add__(self, desired_addition):
        return MoodleFuseException(self + desired_addition)
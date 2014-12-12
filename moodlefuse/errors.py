#!/usr/bin/env python
# encoding: utf-8

"""MoodleFUSE exception class"""


class MoodleFuseError(BaseException):

    _MOODLEFUSE_ERROR_MESSAGE = "MOODLEFUSE ERROR: Error encountered"

    def __init__(self, error_source):
        """
        Initialize a MoodleFUSE error
        """
        self.error_source = error_source

    def __call__(self):
        """
        call The error
        """
        general_message = self._MOODLEFUSE_ERROR_MESSAGE
        error_source = self.error_source()

        def error():
            raise Exception("{0} - {1}".format(
                general_message,
                error_source
            ))

        return error()

#!/usr/bin/env python
# encoding: utf-8


class MoodleFuseError(object):

    _MOODLEFUSE_ERROR_MESSAGE = "MOODLEFUSE ERROR: Error encountered"

    def __init__(self, error_source):
        self.error_source = error_source

    def __call__(self):
        def error():
            raise Exception("{1} - {2}".format(
                self._MOODLEFUSE_ERROR_MESSAGE,
                self.error_source
            ))

        return error()

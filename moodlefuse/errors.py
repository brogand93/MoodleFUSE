#!/usr/bin/env python
# encoding: utf-8

from functools import wraps

class MoodleFuseError():

    _MOODLEFUSE_ERROR_MESSAGE = "MOODLEFUSE ERROR: Error encoumntered while"

    def moodlefuse_error_template(self, error_source, error_reason):
        @wraps(error_reason)
        def error():
            print("{1} {2} - {3}".format(
                self._MOODLEFUSE_ERROR_MESSAGE,
                error_source,
                error_reason()
            ))
        return error()

    def unable_to_upload(self, fn):
        return self.moodlefuse_error_template("uploading resource", fn)

    def unable_to_download(self, fn):
        return self.moodlefuse_error_template("downloading resource", fn)

    def unable_to_authenticate(self, fn):
        return self.moodlefuse_error_template("authenticating", fn)

#!/usr/bin/env python
# encoding: utf-8


class Moodle(object):

    def __init__(self):
        pass


class MoodleException(BaseException):

    def __init__(self):
        self.message = "Unable to complete Moodle action"

    def __str__(self):
        return self.message

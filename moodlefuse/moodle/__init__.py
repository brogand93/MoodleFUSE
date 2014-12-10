#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.subject import Subject


class Moodle(Subject):

    def __init__(self):
        Subject.__init__(self)


class MoodleException(BaseException):

    def __init__(self):
        self.message = "Unable to complete Moodle action"

    def __str__(self):
        return self.message

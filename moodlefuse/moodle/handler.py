#!/usr/bin/env python
# encoding: utf-8

"""Class to handle base Moodle actions.
"""

from moodlefuse.moodle.api import MoodleAPI


class MoodleHandler(object):

    def __init__(self):
        self.moodle = MoodleAPI()

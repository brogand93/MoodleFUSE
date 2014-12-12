#!/usr/bin/env python
# encoding: utf-8

"""Class to handle base Moodle actions, it observes Moodle.
"""

import os

from moodlefuse.moodle.observer import Observer
from moodlefuse.moodle.api import MoodleAPI
from moodlefuse.moodle import MoodleException


class MoodleHandler(Observer):

    def __init__(self):
        Observer.__init__(self)
        self.moodle_api = MoodleAPI
        self._FS_ROOT = os.path.join(os.path.expanduser('~'), 'moodle')

    @staticmethod
    def handle_moodle_action(action, moodlefuse_error, args=None):
        try:
            return action(args)
        except MoodleException:
            moodlefuse_error()

    def update(self):
        raise NotImplementedError("Unable to update observer")

#!/usr/bin/env python
# encoding: utf-8

import os

from abc import ABCMeta, abstractmethod

from moodlefuse.moodle.api import MoodleAPI
from moodlefuse.moodle import MoodleException


class MoodleHandler(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.moodle_api = MoodleAPI
        self._FS_ROOT = os.path.join(os.path.expanduser('~'), 'moodle')

    @staticmethod
    def handle_moodle_action(action, moodlefuse_error, args=None):
        try:
            return action(args)
        except MoodleException:
            moodlefuse_error()

    @abstractmethod
    def update(self):
        raise NotImplementedError("Unable to update observer")

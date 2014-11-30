#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.moodle import MoodleException


class MoodleHandler(object):

    def __init__(self):
        self. _FS_ROOT = os.path.join(os.path.expanduser('~'), 'moodle')

    def handle_moodle_action(self, action, moodlefuse_error, args=None):
        try:
            action(args)
        except MoodleException:
            moodlefuse_error()

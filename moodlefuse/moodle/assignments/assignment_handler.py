#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.moodle_handler import MoodleHandler


class AssignmentHandler(MoodleHandler):

    def __init__(self):
        MoodleHandler.__init__(self)

    def update(self):
        self.sync_assignments()

    def sync_assignments(self):
        pass
#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.assignments.assignment_errors import AssignmentErrors
from moodlefuse.moodle.moodle_handler import MoodleHandler


class AssignmentHandler(MoodleHandler):

    def __init__(self):
        MoodleHandler.__init__(self)

    def update(self):
        self.sync_assignments()

    def sync_assignments(self):
        get_assignments_action = self.moodle_api.get_assignment
        get_assignments_error = AssignmentErrors.unable_to_download_assignment

        assignments = \
            MoodleHandler.handle_moodle_action(get_assignments_action, get_assignments_error)

        for assignment in assignments:
            print "Adding " + assignment

#!/usr/bin/env python
# encoding: utf-8

"""Class to handle assignment Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.courses.course_parser import CourseParser
from moodlefuse.moodle.handler import MoodleHandler


class AssignmentHandler(MoodleHandler):

    def __init__(self, emulator, js_emulator):
        super(self.__class__, self).__init__(emulator, js_emulator)

    def get_assignment_info_as_array(self):
        return ['Submissions', 'description']

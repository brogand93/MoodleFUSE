#!/usr/bin/env python
# encoding: utf-8

"""Class to handle base Moodle actions.
"""

from moodlefuse.moodle.api import MoodleAPI


class MoodleHandler(object):

    def __init__(self):
        self.moodle = MoodleAPI()

    def _enter_course_and_get_contents(self, courses_scrapper, course):
        course_link = self.parser.get_course_link(courses_scrapper, course)
        return self.moodle.get_course_contents(course_link)

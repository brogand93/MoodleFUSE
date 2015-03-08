#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to course incidents.
"""


from moodlefuse.moodle.exception import MoodleException


class UnableToObtainCourseList(MoodleException):

    def __init__(self):
        self.debug_info = "Failed to obtain course list from Moodle"

    def __str__(self):
        return repr(MoodleException + self.debug_info)


class UnableToObtainCategoryList(MoodleException):

    def __init__(self):
        self.debug_info = "Failed to obtain course category list from Moodle"

    def __str__(self):
        return repr(MoodleException + self.debug_info)

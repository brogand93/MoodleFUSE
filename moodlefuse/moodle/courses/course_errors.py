#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to course incidents.
"""

from moodlefuse.moodle.exception import MoodleException


class InvalidMoodleIndex(MoodleException):
    def __init__(self):
        debug_info = "Index page supplied in config is invalid"
        super(InvalidMoodleIndex, self).__init__(debug_info)


class UnableToObtainCourseList(MoodleException):
    def __init__(self):
        debug_info = "Failed to obtain course list from Moodle"
        super(UnableToObtainCourseList, self).__init__(debug_info)


class UnableToOAddCourseCategory(MoodleException):
    def __init__(self):
        debug_info = "Failed to create c ategory in Moodle"
        super(UnableToOAddCourseCategory, self).__init__(debug_info)


class UnableToObtainCategoryList(MoodleException):
    def __init__(self):
        debug_info = "Failed to obtain course category list from Moodle"
        super(UnableToObtainCategoryList, self).__init__(debug_info)

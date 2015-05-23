#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to course incidents.
"""

from moodlefuse.moodle.exception import MoodleException


class InvalidMoodleIndex(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Index page supplied in config is invalid"
        super(InvalidMoodleIndex, self).__init__(_DEBUG_INFO)


class UnableToObtainCourseList(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to obtain course list from Moodle"
        super(UnableToObtainCourseList, self).__init__(_DEBUG_INFO)


class UnableToAddCourseCategory(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to create category in Moodle"
        super(UnableToAddCourseCategory, self).__init__(_DEBUG_INFO)


class UnableToObtainCategoryList(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to obtain course category list from Moodle"
        super(UnableToObtainCategoryList, self).__init__(_DEBUG_INFO)

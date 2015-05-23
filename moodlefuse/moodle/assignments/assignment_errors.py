#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to course incidents.
"""

from moodlefuse.moodle.exception import MoodleException


class UnableToObtainSubmissionList(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to obtain assignment submission list from Moodle"
        super(UnableToObtainSubmissionList, self).__init__(_DEBUG_INFO)


class UnableToGradeAssignment(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to grade assignment"
        super(UnableToGradeAssignment, self).__init__(_DEBUG_INFO)


class UnableToFilterAssignments(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to filter assignment submissions"
        super(UnableToFilterAssignments, self).__init__(_DEBUG_INFO)

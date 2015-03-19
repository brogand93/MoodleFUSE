#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to resource incidents.
"""

from moodlefuse.moodle.exception import MoodleException


class UnableToUploadResource(MoodleException):

    def __init__(self):
        self.debug_info = "Failed to upload resource"

    def __str__(self):
        return repr(MoodleException + self.debug_info)


class UnableToDownloadResource(MoodleException):

    def __init__(self):
        self.debug_info = "Failed to download resource"

    def __str__(self):
        return repr(MoodleException + self.debug_info)


class UnableToObtainResourceList(MoodleException):

    def __init__(self):
        self.debug_info = "Failed to obtain resource list from Moodle"

    def __str__(self):
        return repr(MoodleException + self.debug_info)

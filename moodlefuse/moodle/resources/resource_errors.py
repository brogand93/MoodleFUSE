#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to resource incidents.
"""

from moodlefuse.moodle.exception import MoodleException


class UnableToObtainResourceList(MoodleException):
    def __init__(self):
        debug_info = "Failed to obtain resource list from Moodle"
        super(UnableToObtainResourceList, self).__init__(debug_info)


class UnableToUploadResource(MoodleException):
    def __init__(self):
        debug_info = "Failed to upload resource"
        super(UnableToUploadResource, self).__init__(debug_info)


class UnableToDownloadResource(MoodleException):
    def __init__(self):
        debug_info = "Failed to download resource"
        super(UnableToDownloadResource, self).__init__(debug_info)


class UnableToRenameFile(MoodleException):
    def __init__(self):
        debug_info = "Unable to rename moodle file"
        super(UnableToRenameFile, self).__init__(debug_info)


class UnableToModifyFile(MoodleException):
    def __init__(self):
        debug_info = "Unable to modify moodle file"
        super(UnableToModifyFile, self).__init__(debug_info)


class UnableToAddFile(MoodleException):
    def __init__(self):
        debug_info = "Unable to add moodle file"
        super(UnableToAddFile, self).__init__(debug_info)


class UnableToRemoveFile(MoodleException):
    def __init__(self):
        debug_info = "Unable to modify moodle file"
        super(UnableToRemoveFile, self).__init__(debug_info)

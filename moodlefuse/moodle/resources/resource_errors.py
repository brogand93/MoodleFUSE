#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to resource incidents.
"""

from moodlefuse.moodle.exception import MoodleException


class UnableToObtainResourceList(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to obtain resource list from Moodle"
        super(UnableToObtainResourceList, self).__init__(_DEBUG_INFO)


class UnableToUploadResource(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to upload resource"
        super(UnableToUploadResource, self).__init__(_DEBUG_INFO)


class UnableToGetLocalFile(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to get the local resource"
        super(UnableToGetLocalFile, self).__init__(_DEBUG_INFO)


class UnableToDownloadResource(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Failed to download resource"
        super(UnableToDownloadResource, self).__init__(_DEBUG_INFO)


class UnableToRenameFile(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Unable to rename moodle file"
        super(UnableToRenameFile, self).__init__(_DEBUG_INFO)


class UnableToModifyFile(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Unable to modify moodle file"
        super(UnableToModifyFile, self).__init__(_DEBUG_INFO)


class UnableToAddFile(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Unable to add moodle file"
        super(UnableToAddFile, self).__init__(_DEBUG_INFO)


class UnableToRemoveFile(MoodleException):
    def __init__(self):
        _DEBUG_INFO = "Unable to modify moodle file"
        super(UnableToRemoveFile, self).__init__(_DEBUG_INFO)

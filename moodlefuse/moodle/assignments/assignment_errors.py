#!/usr/bin/env python
# encoding: utf-8

"""Class to handle errors relating to assignment incidents.
"""

from moodlefuse.errors import MoodleFuseError


class AssignmentErrors(object):

    @staticmethod
    @MoodleFuseError
    def unable_to_upload_assignment():
        print "Unable to upload assignment"

    @staticmethod
    @MoodleFuseError
    def unable_to_download_assignment():
        print "Unable to download assignment"

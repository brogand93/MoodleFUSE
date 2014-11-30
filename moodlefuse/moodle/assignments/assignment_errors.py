#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.errors import MoodleFuseError

class AssignmentErrors(MoodleFuseError):

    @MoodleFuseError
    def unable_to_upload_assignment(self):
        print "Unable to upload assignment"

    @MoodleFuseError
    def unable_to_download_assignment(self):
        print "Unable to download assignment"

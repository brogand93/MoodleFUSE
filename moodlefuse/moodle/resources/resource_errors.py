#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.errors import MoodleFuseError


class ResourceErrors(object):

    @staticmethod
    @MoodleFuseError
    def unable_to_upload_resource():
        return "Unable to upload resource"

    @staticmethod
    @MoodleFuseError
    def unable_to_get_resource():
        return "Unable to get resource"

    @staticmethod
    @MoodleFuseError
    def unable_to_remove_resource():
        return "Unable to remove resource"

    @staticmethod
    @MoodleFuseError
    def unable_to_modify_resource():
        return "Unable to modify resource"

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.errors import MoodleFuseError


class ResourceErrors(MoodleFuseError):

    @MoodleFuseError
    def unable_to_upload_resource(self):
        return "Unable to upload resource"

    MoodleFuseError
    def unable_to_get_resource(self):
        return "Unable to get resource"

    @MoodleFuseError
    def unable_to_remove_resource(self):
        return "Unable to remove resource"

    @MoodleFuseError
    def unable_to_modify_resource(self):
        return "Unable to modify resource"

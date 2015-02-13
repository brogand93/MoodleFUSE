#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.resources.resource_errors import ResourceErrors
from moodlefuse.moodle.moodle_handler import MoodleHandler


class ResourceHandler(MoodleHandler):

    def sync_remote_resources_locally(self):
        get_resource_action = self.moodle_api.download_resources
        get_resource_error = ResourceErrors.unable_to_get_resource

        MoodleHandler.handle_moodle_action(get_resource_action, get_resource_error)

    @staticmethod
    def get_file_names_as_array():
        return ['lecture1.txt', 'testffile.txt']

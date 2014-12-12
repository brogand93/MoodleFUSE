#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.resources.resource_errors import ResourceErrors
from moodlefuse.moodle.moodle_handler import MoodleHandler


class ResourceHandler(MoodleHandler):

    def __init__(self):
        MoodleHandler.__init__(self)

    def update(self):
        self.sync_resources()

    def sync_resources(self):
        get_resource_action = self.moodle_api.download_resources
        get_resource_error = ResourceErrors.unable_to_get_resource

        resources = \
            MoodleHandler.handle_moodle_action(get_resource_action, get_resource_error)

        for resource in resources:
            print "Adding " + resource

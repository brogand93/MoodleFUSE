#!/usr/bin/env python
# encoding: utf-8

import time

from moodlefuse.moodle import Moodle
from moodlefuse.moodle.api import MoodleAPI


class MoodleWatcher(object):

    def __init__(self):
        self.moodle = Moodle()

    def poll_moodle(self, poll_delay):
        while True:
            resource_info = MoodleAPI.inspect_resources(MoodleAPI)
            moodle_changed = self.moodle_has_changed(resource_info)
            if moodle_changed:
                self.moodle.notify()

            time.sleep(poll_delay)

    def moodle_has_changed(self, current_resource_info):
        previous_resource_info = {
            "modified": 15
        }

        last_modified = current_resource_info.modified
        last_updated_at = previous_resource_info['modified']

        return last_modified < last_updated_at

#!/usr/bin/env python
# encoding: utf-8

"""Class to watch moodle and wait for changes
"""

import time
import threading


class MoodleWatcher(threading.Thread):

    def __init__(self, poll_delay=720000):
        super(MoodleWatcher, self).__init__()
        self.poll_delay = poll_delay

    def run(self):
        self._poll_moodle(self.poll_delay)

    def _poll_moodle(self, poll_delay):
        while True:
            self._poll_resources()
            self._poll_courses()
            time.sleep(poll_delay)

    def _poll_resources(self):
        pass

    def _poll_courses(self):
        pass

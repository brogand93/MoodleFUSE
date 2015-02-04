#!/usr/bin/env python
# encoding: utf-8

"""Class to watch moodle and wait for channges
"""

import time
import threading

from datetime import datetime

from moodlefuse.moodle.api import MoodleAPI


class MoodleWatcher(threading.Thread):

    def __init__(self, moodle):
        super(MoodleWatcher, self).__init__()
        self.moodle = moodle

    def run(self):
        poll_delay = 120*100*60
        self._poll_moodle(poll_delay)

    def _poll_moodle(self, poll_delay):
        while True:
            self._poll_resources()
            self._poll_courses()
            time.sleep(poll_delay)

    def _poll_resources(self):
        pass

    def _poll_courses(self):
        pass

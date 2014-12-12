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
        self._poll_moodle(1000000)

    def _poll_moodle(self, poll_delay):
        while True:
            moodle_last_updated = MoodleAPI.inspect_resources()
            moodle_changed = self._moodle_has_changed(moodle_last_updated)
            if moodle_changed:
                print "Detected change in Moodle"
                self.moodle.notify()

            time.sleep(poll_delay)

    def _moodle_has_changed(self, moodle_last_updated):
        # Dummy last synced time to trigger observer update
        last_synced = datetime(2014, 1, 1)

        return last_synced < moodle_last_updated

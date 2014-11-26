#!/usr/bin/env python
# encoding: utf-8

import thread
import time

class MoodleWatcher():

    def poll_moodle(poll_delay):
        while True:

            time.sleep(poll_delay)
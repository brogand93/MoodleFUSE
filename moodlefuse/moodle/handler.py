#!/usr/bin/env python
# encoding: utf-8

"""Class to handle base Moodle actions.
"""

import os

from moodlefuse.moodle.api import MoodleAPI
from moodlefuse.moodle.scraper import Scraper


class MoodleHandler(object):

    def __init__(self):
        self.moodle = MoodleAPI()
        self.scraper = Scraper()

    def remove_unicode(self, items):
        return [item.encode('utf-8') for item in items]

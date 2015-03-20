#!/usr/bin/env python
# encoding: utf-8

"""Base class to parse Moodle items
"""

from moodlefuse.moodle.scraper import Scraper


class Parser(object):

    def __init__(self):
        self.scraper = Scraper()

    def remove_unicode(self, items):
        return [item.encode('utf-8') for item in items]

    def get_link_from_item(self, item):
        if item is not None:
            return item['href']

        return None

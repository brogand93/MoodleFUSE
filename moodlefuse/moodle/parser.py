#!/usr/bin/env python
# encoding: utf-8

"""Base class to parse Moodle items
"""

from moodlefuse.moodle.scraper import Scraper
from moodlefuse.moodle import attributes


class Parser(object):

    def __init__(self):
        self.scraper = Scraper()

    def remove_special_chars(self, string):
        return string.replace(u'\xa0', '')

    def remove_unicode(self, items):
        return [item.encode(attributes.ENCODING) for item in items]

    def get_link_from_item(self, item):
        if item is not None:
            return item[attributes.LINKTEXT]

        return None

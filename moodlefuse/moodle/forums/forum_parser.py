#!/usr/bin/env python
# encoding: utf-8

"""Derived class to parse Moodle course items, it parses
   Moodle and therefor extends off of Parser
"""

from moodlefuse.moodle.parser import Parser
from moodlefuse.moodle import attributes
from moodlefuse.moodle import forums


class ForumParser(Parser):

    def __init__(self):
        super(ForumParser, self).__init__()

    def forum_exists_on_moodle(self, category_content, filename):
        activity_instances = self.scraper.get_html_items_with_divclass(
            category_content, attributes.INSTANCE)

        for activity in activity_instances:
            if forums.FORUM_LINK_CONTENT in str(activity):
                return True

        return False

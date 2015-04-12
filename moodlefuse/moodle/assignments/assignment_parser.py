#!/usr/bin/env python
# encoding: utf-8

"""Derived class to parse Moodle course items, it parses
   Moodle and therefor extends off of Parser
"""

from moodlefuse.moodle.parser import Parser


class AssignmentParser(Parser):

    def __init__(self):
        super(AssignmentParser, self).__init__()

    def get_all_assignment_names(self, assignment_content):
        names = []
        names_list = self.scraper.get_html_items_with_tdclass(assignment_content, 'cell c2')
        for name_item in names_list:
            name = name_item.get_text()
            if name != '':
                name = name.replace(" ", "_")
                name = name + "_submission"
                names.append(name)

        return names

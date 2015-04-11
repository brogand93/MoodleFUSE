#!/usr/bin/env python
# encoding: utf-8

"""Derived class to parse Moodle course items, it parses
   Moodle and therefor extends off of Parser
"""

from moodlefuse.moodle.parser import Parser


class AssignmentParser(Parser):

    def __init__(self):
        super(AssignmentParser, self).__init__()

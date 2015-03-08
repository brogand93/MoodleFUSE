#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.parser import Parser


class ResourceParser(Parser):

    def __init__(self):
        super(ResourceParser, self).__init__()

    def _parse_course_resources(self, categories, desired_categorie):
        pass

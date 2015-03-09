#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.resources.resource_parser import ResourceParser
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.moodle.handler import MoodleHandler


class ResourceHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.parser = ResourceParser()

    def get_file_names_as_array(self, category_contents):
        if category_contents is None:
            return []
        return self.parser.parse_course_resources(category_contents)

    def get_file_path(self, course, categorie, filename):
        pass

    def download_resource(self, location, moodle_url):
        pass

    def create_file(self, location):
        cache_path = get_cache_path_based_on_location(location)
        with open(cache_path, 'w'):
            return cache_path

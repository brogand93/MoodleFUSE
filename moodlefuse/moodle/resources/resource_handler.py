#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.handler import MoodleHandler
from moodlefuse.helpers import get_cache_path_based_on_location


class ResourceHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def get_file_names_as_array(self, course, categorie):
        pass

    def get_file_path(self, course, categorie, filename):
        pass

    def download_resource(self, location, moodle_url):
        pass

    def create_file(self, location):
        cache_path = get_cache_path_based_on_location(location)
        with open(cache_path, 'w'):
            return cache_path

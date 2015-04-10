#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.resources.resource_parser import ResourceParser
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.moodle.handler import MoodleHandler


class ResourceHandler(MoodleHandler):

    def __init__(self, emulator, js_emulator):
        super(self.__class__, self).__init__(emulator, js_emulator)
        self.parser = ResourceParser()

    def get_file_names_as_array(self, category_contents):
        if category_contents is None:
            return []
        return self.parser.parse_course_resources(category_contents)

    def get_file_path(self, category_contents, filename):
        if category_contents is None:
            return []
        return self.parser.parse_course_resource_url(
            category_contents,
            filename
        )

    def download_resource(self, location, moodle_url):
        cache_path = self.create_file(location)
        moodle_download_url = moodle_url + "?forcedownload=1"
        self.moodle.download_resources(cache_path, moodle_download_url)
        return cache_path

    def create_file(self, location):
        cache_path = get_cache_path_based_on_location(location)
        with open(cache_path, 'w'):
            return cache_path

    def add_resource(self, resource_path, category, resource_name):
        self.moodle.add_new_resource(category, resource_name, resource_path)

    def modify_resource(self, resource_path, category, resource_name):
        self.moodle.modify_existing_resource(category, resource_name, resource_path)

    def rename_resource(self, category, old_resource_name, new_resource_name):
        self.moodle.rename_existing_resource(category, old_resource_name, new_resource_name)

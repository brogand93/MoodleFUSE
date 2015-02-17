#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.moodle_handler import MoodleHandler
from moodlefuse.moodle.api import MoodleAPI


class ResourceHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.moodle = MoodleAPI()

    def get_file_names_as_array(self, course, categorie):
        categories = self.moodle.get_course_contents(2)
        return self._parse_course_resources(categories, categorie)

    def _parse_course_resources(self, categories_dictionary, desired_categorie):
        resources = []
        for categorie in categories_dictionary:
            if categorie['name'] == desired_categorie:
                for module in categorie['modules']:
                    for resource in module['contents']:
                        resources.append(resource['filename'])

        return resources

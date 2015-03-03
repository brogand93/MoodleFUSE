#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.moodle_handler import MoodleHandler
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.moodle.courses.course_handler import CourseHandler


class ResourceHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def get_file_names_as_array(self, course, categorie):
        courses = CourseHandler()
        course_id = courses.get_course_id_by_name(course)
        if course_id != 0:
            categories = self.moodle.get_course_contents(course_id)
            return self._parse_course_resources(categories, categorie)

    def get_file_path(self, course, categorie, filename):
        courses = CourseHandler()
        course_id = courses.get_course_id_by_name(course)
        if course_id != 0:
            categories = self.moodle.get_course_contents(course_id)
            return self._parse_course_resource_url(categories, categorie, filename)

    def download_resource(self, location, moodle_url):
        cache_path = get_cache_path_based_on_location(location)
        return self.moodle.download_resources(cache_path, moodle_url)

    def create_file(self, location):
        cache_path = get_cache_path_based_on_location(location)
        open(cache_path, 'w')
        return cache_path

    def _parse_course_resources(self, categories, desired_categorie):
        resources = []
        for categorie in categories:
            if categorie['name'] == desired_categorie:
                for module in categorie['modules']:
                    for resource in module['contents']:
                        resources.append(resource['filename'])

        return resources


    def _parse_course_resource_url(self, categories, desired_categorie, filename):
        for categorie in categories:
            if categorie['name'] == desired_categorie:
                for module in categorie['modules']:
                    for resource in module['contents']:
                        if resource['filename'] == filename:
                            return resource['fileurl']

        return None

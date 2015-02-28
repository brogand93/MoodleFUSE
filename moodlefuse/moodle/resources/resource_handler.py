#!/usr/bin/env python
# encoding: utf-8

"""Class to handle resource Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.moodle_handler import MoodleHandler
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

    def download_resource(self, moodle_url, location):
        return self.moodle.download_resources(location, moodle_url)

    def _parse_course_resources(self, categories, desired_categorie):
        resources = []
        for categorie in categories:
            if categorie['name'] == desired_categorie:
                for module in categorie['modules']:
                    for resource in module['contents']:
                        resources.append(resource['filename'])

        return resources


    def _parse_course_resource_url(self, categories, desired_categorie, filename):
        resource = None

        for categorie in categories:
            if categorie['name'] == desired_categorie:
                for module in categorie['modules']:
                    for resource in module['contents']:
                        if resource['filename'] == filename:
                            return  resource['fileurl']

        return resource

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.resources.resource_handler import ResourceHandler
from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.core import config


class FileSystemTranslator(object):

    def __init__(self):
        self.courses = CourseHandler()
        self.resources = ResourceHandler()

    def _location_is_in_root(self, location):
        return len(location) is 0

    def _location_is_in_course(self, location):
        return len(location) is 1

    def _location_is_in_course_categorie(self, location):
        return len(location) is 2

    def _location_is_file(self, location):
        return len(location) is 3

    def get_position_in_filesystem_as_array(self, path):
        path = path.replace(config['LOCAL_MOODLE_FOLDER'] + '/', '')
        if len(path) is 0:
            return []

        path_sections = path.split("/")
        return path_sections

    def open_file(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        if len(location) is 3:
            moodle_url = self.resources.get_file_path(location[0], location[1], location[2])
            if moodle_url is None:
                return self.resources.create_file(location)
            return self.resources.download_resource(location, moodle_url)

    def create_file(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        if len(location) is 3:
            cache_path = get_cache_path_based_on_location(location)
            open(cache_path, 'w')
            return cache_path

    def is_file(self, location):
        return self._location_is_file(location)

    def get_file_attributes(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        attributes = {
            'st_ctime': 1,
            'st_mtime': 2,
            'st_nlink': 7,
            'st_size': 4096,
            'st_gid': 1000,
            'st_uid': 1000,
            'st_atime': 1
        }
        if self.is_file(location):
            attributes['st_mode'] = 33188
        else: attributes['st_mode'] = 16877

        return attributes

    def get_directory_contents_based_on_path(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        dirents = ['.', '..']

        if self._location_is_in_root(location):
            dirents.extend(self.courses.get_courses_as_array())
        elif self._location_is_in_course(location):
            dirents.extend(self.courses.get_course_categories_as_array(location[0]))
        elif self._location_is_in_course_categorie(location):
            dirents.extend(self.resources.get_file_names_as_array(location[0], location[1]))

        return dirents

    def path_exists_in_moodle(self, path):
        location = self.get_position_in_filesystem_as_array(path)

        if self._location_is_in_root(location):
            return True
        elif self._location_is_in_course(location):
            return location[0] in self.courses.get_courses_as_array()
        elif self._location_is_in_course_categorie(location):
            return location[1] in self.courses.get_course_categories_as_array(location[0])

        return False

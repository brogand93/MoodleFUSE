#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.moodle.resources.resource_handler import ResourceHandler

import os


class FileSystemTranslator(object):

    @staticmethod
    def _location_is_in_root(location):
        return len(location) is 0

    @staticmethod
    def _location_is_in_course(location):
        return len(location) is 1

    @staticmethod
    def _location_is_in_course_categorie(location):
        return len(location) is 2

    @staticmethod
    def get_position_in_filesystem_as_array(path):
        path = path.strip(str(os.path.join(os.path.expanduser('~'), 'moodle')))
        if len(path) is 0:
            return []
        path_sections = path.split("/")
        return path_sections

    @staticmethod
    def get_directory_contents_based_on_path(path):
        location = FileSystemTranslator.get_position_in_filesystem_as_array(path)
        dirents = ['.', '..']

        if FileSystemTranslator._location_is_in_root(location):
            dirents.extend(CourseHandler.get_courses_as_array())
        elif FileSystemTranslator._location_is_in_course(location):
            dirents.extend(CourseHandler.get_course_categories_as_array('testcourse'))
        elif FileSystemTranslator._location_is_in_course_categorie(location):
            dirents.extend(ResourceHandler.get_file_names_as_array())

        return dirents

    @staticmethod
    def path_exists_in_moodle(path):
        location = FileSystemTranslator.get_position_in_filesystem_as_array(path)

        if FileSystemTranslator._location_is_in_root(location):
            return True
        elif FileSystemTranslator._location_is_in_course(location):
            return location[0] in CourseHandler.get_courses_as_array()
        elif FileSystemTranslator._location_is_in_course_categorie(location):
            return location[1] in CourseHandler.get_course_categories_as_array('testcourse')
        else:
            return False

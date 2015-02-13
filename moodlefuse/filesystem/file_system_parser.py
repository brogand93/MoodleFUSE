#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.moodle.resources.resource_handler import ResourceHandler

import os


class FileSystemParser(object):

    @staticmethod
    def get_position_in_filesystem_as_array(path):
        path = path.strip(str(os.path.join(os.path.expanduser('~'), 'moodle')))
        if len(path) is 0:
            return []
        path_sections = path.split("/")
        return path_sections

    @staticmethod
    def get_directory_contents_based_on_location(location):
        dirents = ['.', '..']

        if len(location) is 0:
            dirents.extend(CourseHandler.get_courses_as_array())

        if len(location) is 1:
            dirents.extend(CourseHandler.get_course_categories_as_array('testcourse'))

        if len(location) is 2:
            dirents.extend(ResourceHandler.get_file_names_as_array())

        return dirents

    @staticmethod
    def path_exists_in_moodle(location):
        if len(location) is 0:
            return True

        if len(location) is 1:
            return location[0] in CourseHandler.get_courses_as_array()

        if len(location) is 2:
            return location[1] in CourseHandler.get_course_categories_as_array('testcourse')

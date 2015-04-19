#!/usr/bin/env python
# encoding: utf-8

"""Class to parse a filesystem path
"""

from moodlefuse.core import config


class PathParser(object):

    @staticmethod
    def is_in_root(location):
        return len(location) is 0

    @staticmethod
    def is_in_course(location):
        return len(location) is 1

    @staticmethod
    def is_in_course_categorie(location):
        return len(location) is 2

    @staticmethod
    def is_file(location):
        return len(location) is 3

    @staticmethod
    def is_assignment(location):
        return len(location) is 4

    @staticmethod
    def is_assignment_submission(location):
        return len(location) is 5

    @staticmethod
    def get_position_in_filesystem_as_array(path):
        path = path.replace(config['LOCAL_MOODLE_FOLDER'] + '/', '')

        if len(path) is 0:
            return []

        path_sections = path.split("/")
        return path_sections

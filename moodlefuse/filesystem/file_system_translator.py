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
    def _location_is_file(location):
        return len(location) is 3

    @staticmethod
    def get_position_in_filesystem_as_array(path):
        path = path.replace(str(os.path.join(os.path.expanduser('~'), 'moodle/')), '')
        if len(path) is 0:
            return []

        path_sections = path.split("/")
        return path_sections

    @staticmethod
    def open_file(path):
        resources = ResourceHandler()
        location = FileSystemTranslator.get_position_in_filesystem_as_array(path)
        if len(location) is 3:
            moodle_url = resources._parse_course_resource_url(location[0], location[1], location[2])
            return resources.download_resource(location, moodle_url)

    @staticmethod
    def is_file(location):
        return FileSystemTranslator._location_is_file(location)

    @staticmethod
    def get_file_attributes(path):
        location = FileSystemTranslator.get_position_in_filesystem_as_array(path)
        attributes = {
            'st_ctime': 1,
            'st_mtime': 1,
            'st_nlink': 7,
            'st_size': 4096,
            'st_gid': 1000,
            'st_uid': 1000,
            'st_atime': 1
        }
        if FileSystemTranslator.is_file(location):
            attributes['st_mode'] = 33188
        else: attributes['st_mode'] = 16877

        return attributes

    @staticmethod
    def get_directory_contents_based_on_path(path):
        location = FileSystemTranslator.get_position_in_filesystem_as_array(path)
        dirents = ['.', '..']

        if FileSystemTranslator._location_is_in_root(location):
            courses = CourseHandler()
            dirents.extend(courses.get_courses_as_array())
        elif FileSystemTranslator._location_is_in_course(location):
            courses = CourseHandler()
            courseid = courses.get_course_id_by_name(location[0])
            dirents.extend(courses.get_course_categories_as_array(courseid))
        elif FileSystemTranslator._location_is_in_course_categorie(location):
            resources = ResourceHandler()
            dirents.extend(resources.get_file_names_as_array(location[0], location[1]))

        return dirents

    @staticmethod
    def path_exists_in_moodle(path):
        location = FileSystemTranslator.get_position_in_filesystem_as_array(path)
        courses = CourseHandler()

        if FileSystemTranslator._location_is_in_root(location):
            return True
        elif FileSystemTranslator._location_is_in_course(location):
            return location[0] in courses.get_courses_as_array()
        elif FileSystemTranslator._location_is_in_course_categorie(location):
            courseid = courses.get_course_id_by_name(location[0])
            return location[1] in courses.get_course_categories_as_array(courseid)

        return False

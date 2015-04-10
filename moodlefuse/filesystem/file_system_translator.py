#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.resources.resource_handler import ResourceHandler
from moodlefuse.moodle.emulator.js_enabled_emulator import JsEmulator
from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.moodle.emulator.core_emulator import CoreEmulator
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.filesystem.files.cache_file import CacheFile
from moodlefuse.filesystem.files.directory import Directory
from moodlefuse.core import config

import os


class FileSystemTranslator(object):

    def __init__(self):
        emulator = CoreEmulator(config['USERNAME'], config['PASSWORD'])
        js_emulator = JsEmulator(config['USERNAME'], config['PASSWORD'])
        emulator.login()
        js_emulator.login()
        self.courses = CourseHandler(emulator, js_emulator)
        self.resources = ResourceHandler(emulator, js_emulator)

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
        if self._location_is_file(location):
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            moodle_url = self.resources.get_file_path(category_contents, location[2])
            if moodle_url is None:
                return CacheFile.create_file(location)
            else:
                return self.resources.download_resource(location, moodle_url)

    def rename_file(self, old_path, new_path):
        old_location = self.get_position_in_filesystem_as_array(old_path)
        new_location = self.get_position_in_filesystem_as_array(new_path)
        if self._location_is_file(old_location):
            self.courses.enter_course_with_js(old_location[0])
            self.resources.rename_resource(old_location[1], old_location[2], new_location[3])

    def modify_file(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        if self._location_is_file(location):
            self.courses.enter_course_with_js(location[0])
            self.resources.modify_resource(path, location[1], location[2])

    def create_file(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        if self._location_is_file(location):
            cache_path = get_cache_path_based_on_location(location)
            cache_file = open(cache_path, 'w')
            cache_file.write(' ')
            cache_file.close()
            self.courses.enter_course_with_js(location[0])
            self.resources.add_resource(cache_path, location[1], location[2])
            return cache_path

    def is_file(self, location):
        return self._location_is_file(location)

    def make_directory(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        if self._location_is_in_course(location):
            pass
        else:
            self.courses.enter_course_and_get_contents(location[0])
            self.courses.add_new_category(location[1])

    def use_cache_file_or_get_update_file(self, location, cache_path):
        if not os.path.isfile(cache_path):
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            moodle_url = self.resources.get_file_path(category_contents, location[2])
            self.resources.download_resource(location, moodle_url)

    def get_file_attributes(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        if self.is_file(location):
            cache_path = get_cache_path_based_on_location(location)
            self.use_cache_file_or_get_update_file(location, cache_path)
            return CacheFile(cache_path).get_aattrs()
        else:
            return Directory().get_aattrs()

    def get_directory_contents_based_on_path(self, path):
        location = self.get_position_in_filesystem_as_array(path)
        dirents = ['.', '..']

        if self._location_is_in_root(location):
            dirents.extend(self.courses.get_courses_as_array())
        elif self._location_is_in_course(location):
            dirents.extend(self.courses.get_course_categories_as_array(location[0]))
        elif self._location_is_in_course_categorie(location):
            if location[0] == '.Trash-1000':
                return dirents
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            dirents.extend(self.resources.get_file_names_as_array(category_contents))

        return dirents

    def path_exists_in_moodle(self, path):
        location = self.get_position_in_filesystem_as_array(path)

        if self._location_is_in_root(location):
            return True
        elif self._location_is_in_course(location):
            return location[0] in self.courses.get_courses_as_array()
        elif self._location_is_in_course_categorie(location):
            return location[1] in \
                self.courses.get_course_categories_as_array(location[0])
        elif self._location_is_file(location):
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            return location[2] in self.resources.get_file_names_as_array(category_contents)
        return False

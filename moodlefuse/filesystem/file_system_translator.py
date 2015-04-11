#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.assignments.assignment_handler import AssignmentHandler
from moodlefuse.moodle.resources.resource_handler import ResourceHandler
from moodlefuse.moodle.emulator.js_enabled_emulator import JsEmulator
from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.moodle.emulator.core_emulator import CoreEmulator
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.filesystem.files.cache_file import CacheFile
from moodlefuse.filesystem.files.directory import Directory
from moodlefuse.filesystem.path_parser import PathParser
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
        self.assignments = AssignmentHandler(emulator, js_emulator)

    def open_file(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            moodle_url = self.resources.get_file_path(category_contents, location[2])
            if moodle_url is None:
                return CacheFile.create_file(location)
            else:
                return self.resources.download_resource(location, moodle_url)
        elif PathParser.is_assignment(location):
            return self.assignments.get_grades_csv(location)


    def rename_file(self, old_path, new_path):
        old_location = PathParser.get_position_in_filesystem_as_array(old_path)
        new_location = PathParser.get_position_in_filesystem_as_array(new_path)
        if PathParser.is_file(old_location):
            self.courses.enter_course_with_js(old_location[0])
            self.resources.rename_resource(old_location[1], old_location[2], new_location[3])

    def modify_file(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            self.courses.enter_course_with_js(location[0])
            self.resources.modify_resource(path, location[1], location[2])

    def create_file(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            cache_path = get_cache_path_based_on_location(location)
            cache_file = open(cache_path, 'w')
            cache_file.write(' ')
            cache_file.close()
            self.courses.enter_course_with_js(location[0])
            self.resources.add_resource(cache_path, location[1], location[2])
            return cache_path

    def make_directory(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_in_course(location):
            pass
        else:
            self.courses.enter_course_and_get_contents(location[0])
            self.courses.add_new_category(location[1])

    def use_cache_file_or_get_update_file(self, location, cache_path):
        if self.is_assignment_grading_form(location):
            CacheFile.create_file(location)
        elif not os.path.isfile(cache_path):
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            moodle_url = self.resources.get_file_path(category_contents, location[2])
            self.resources.download_resource(location, moodle_url)

    def is_assignment_grading_form(self, location):
        if(PathParser.is_assignment(location)):
            return location[3] == 'grades.csv'
        return False

    def file_is_assignment(self, location):
        course_contents = self.courses.enter_course_and_get_contents(location[0])
        category_contents = self.courses.get_course_category_contents(course_contents, location[1])
        return self.resources.is_assignment(category_contents, location[2])

    def represent_as_directory(self, location):
        return self.file_is_assignment(location) and not \
               self.is_assignment_grading_form(location)

    def represent_as_file(self, location):
        return (PathParser.is_file(location) or
               PathParser.is_assignment(location) or
               PathParser.is_assignment_submission(location)) and not \
               self.represent_as_directory(location)


    def get_file_attributes(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if self.represent_as_file(location):
            cache_path = get_cache_path_based_on_location(location)
            self.use_cache_file_or_get_update_file(location, cache_path)
            return CacheFile(cache_path).get_aattrs()
        else:
            return Directory().get_aattrs()


    def get_directory_contents_based_on_path(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        dirents = ['.', '..']

        if PathParser.is_in_root(location):
            dirents.extend(self.courses.get_courses_as_array())
        elif PathParser.is_in_course(location):
            dirents.extend(self.courses.get_course_categories_as_array(location[0]))
        elif PathParser.is_in_course_categorie(location):
            if location[0] == '.Trash-1000':
                return dirents
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            dirents.extend(self.resources.get_file_names_as_array(category_contents))
        elif PathParser.is_file(location):
            dirents.extend(self.assignments.get_assignment_info_as_array())

        return dirents

    def path_exists_in_moodle(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)

        if PathParser.is_in_root(location):
            return True
        elif PathParser.is_in_course(location):
            return location[0] in self.courses.get_courses_as_array()
        elif PathParser.is_in_course_categorie(location):
            return location[1] in \
                self.courses.get_course_categories_as_array(location[0])
        elif PathParser.is_file(location):
            course_contents = self.courses.enter_course_and_get_contents(location[0])
            category_contents = self.courses.get_course_category_contents(course_contents, location[1])
            return location[2] in self.resources.get_file_names_as_array(category_contents)
        elif PathParser.is_assignment(location):
            return location[3] in self.assignments.get_assignment_info_as_array()

        return False

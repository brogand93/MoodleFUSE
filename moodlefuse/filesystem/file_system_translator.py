#!/usr/bin/env python
# encoding: utf-8

"""Class to translate filesystem events to Moodle actions
"""

import os

from moodlefuse.moodle.assignments.assignment_handler import AssignmentHandler
from moodlefuse.moodle.resources.resource_handler import ResourceHandler
from moodlefuse.moodle.emulator.js_enabled_emulator import JsEmulator
from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.moodle.emulator.core_emulator import CoreEmulator
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.filesystem.remote_handler import RemoteHandler
from moodlefuse.filesystem.files.cache_file import CacheFile
from moodlefuse.filesystem.files.directory import Directory
from moodlefuse.filesystem.path_parser import PathParser
from moodlefuse.moodle import assignments
from moodlefuse.core import config


class FileSystemTranslator(object):

    def __init__(self):
        self.emulator = CoreEmulator(config['USERNAME'], config['PASSWORD'])
        self.js_emulator = JsEmulator(config['USERNAME'], config['PASSWORD'])
        self.emulator.login()
        self.js_emulator.login()
        course = CourseHandler(self.emulator, self.js_emulator)
        resource = ResourceHandler(self.emulator, self.js_emulator)
        assignment = AssignmentHandler(self.emulator, self.js_emulator)
        self.remote_handler = RemoteHandler(course, resource, assignment)

    def close_browsers(self):
        self.emulator.close()
        self.js_emulator.close()

    def open_file(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            moodle_url = self.remote_handler.get_remote_file_path(location)
            if moodle_url is None:
                return CacheFile.create_file(location)
            else:
                return self.remote_handler.download_updated_file(location, moodle_url)
        elif PathParser.is_assignment(location):
            return self.remote_handler.get_remote_grading_csv(location)

    def rename_file(self, old_path, new_path):
        old_location = PathParser.get_position_in_filesystem_as_array(old_path)
        new_location = PathParser.get_position_in_filesystem_as_array(new_path)
        if PathParser.is_file(old_location):
            self.remote_handler.rename_resource(old_location, new_location)

    def modify_file(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            self.modify_file(path)
        elif PathParser.is_assignment(location):
            self.remote_handler.modify_grades(location)

    def create_file(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            cache_path = get_cache_path_based_on_location(location)
            CacheFile(cache_path).create_file(location, ' ')
            self.remote_handler.add_resource(location, cache_path)
            return cache_path

    def make_directory(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_in_course_categorie(location):
            self.remote_handler.add_category(location)

    def use_cache_file_or_get_update_file(self, location, cache_path):
        if not os.path.isfile(cache_path):
            if self.is_assignment_grading_form(location):
                return self.remote_handler.get_remote_grading_csv(location)
            else:
                moodle_url = self.remote_handler.get_remote_file_path(location)
                return self.remote_handler.download_updated_file(location, moodle_url)
        return cache_path

    def is_assignment_grading_form(self, location):
        if PathParser.is_assignment(location):
            return location[3] == assignments.GRADES_FILENAME

        return False

    def remove_resource(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        if PathParser.is_file(location):
            return self.remote_handler.remove_resource(location)

    def file_is_assignment(self, location):
        return self.remote_handler.is_valid_assignment(location)

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
            cache_path = self.use_cache_file_or_get_update_file(location, cache_path)
            return CacheFile(cache_path).get_attrs()
        else:
            return Directory().get_aattrs()

    def get_directory_contents_based_on_path(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        dirents = ['.', '..']
        handle = {
            PathParser.is_in_root(location): self.remote_handler.get_remote_courses,
            PathParser.is_in_course(location): self.remote_handler.get_remote_categories,
            PathParser.is_in_course_categorie(location): self.remote_handler.get_remote_resourse_names,
            PathParser.is_file(location): self.remote_handler.get_remote_assignment_info,
            PathParser.is_assignment(location): self.remote_handler.get_remote_assignment_names,
        }

        if True in handle:
            dirents.extend((handle.get(True))(location))

        return dirents

    def path_exists_in_moodle(self, path):
        location = PathParser.get_position_in_filesystem_as_array(path)
        handle = {
            PathParser.is_in_root(location): self.remote_handler.is_valid_root,
            PathParser.is_in_course(location): self.remote_handler.is_valid_course,
            PathParser.is_in_course_categorie(location): self.remote_handler.is_valid_category,
            PathParser.is_file(location): self.remote_handler.is_valid_resource,
            PathParser.is_assignment(location): self.remote_handler.is_valid_assignment_info,
            PathParser.is_assignment_submission(location): self.remote_handler.is_valid_assignment_submission
        }

        if True in handle:
            return (handle.get(True))(location)
        else:
            return False

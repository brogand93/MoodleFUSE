#!/usr/bin/env python
# encoding: utf-8


class MoodleAPI(object):

    def inspect_resources(self):
        moodle_function = "core_files_inspect"
        print moodle_function

    def upload_resources(self, resources):
        moodle_function = "core_files_upload"
        print moodle_function

    def download_resources(self):
        moodle_function = "core_files_get_files"
        print moodle_function

    def get_courses(self):
        moodle_function = "core_course_get_courses"
        print moodle_function

    def get_course_sections(self):
        moodle_function = "core_course_get_categories"
        print moodle_function

    def create_course_section(self):
        moodle_function = "core_course_create_categories"
        print moodle_function

    def remove_course_section(self):
        moodle_function = "core_course_delete_categories"
        print moodle_function

    def get_assignment(self):
        moodle_function = "mod_assign_get_assignments"
        print moodle_function

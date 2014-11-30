#!/usr/bin/env python
# encoding: utf-8

class MoodleAPI():

    def inspect_resources(self):
        moodle_function = "core_files_inspect"
        pass

    def upload_resources(self, resources):
        moodle_function = "core_files_upload"
        pass

    def download_resources(self):
        moodle_function = "core_files_get_files"
        pass

    def get_courses(self):
        moodle_function = "core_course_get_courses"
        pass

    def get_course_sections(self):
        moodle_function = "core_course_get_categories"
        pass

    def create_course_section(self):
        moodle_function = "core_course_create_categories"
        pass

    def remove_course_section(self):
        moodle_function = "core_course_delete_categories"
        pass

    def get_assignment(self):
        moodle_unction = "mod_assign_get_assignments"
        pass

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle import MoodleException
from datetime import datetime


class MoodleAPI(object):

    @staticmethod
    def inspect_resources(args=None):
        print "=================================="
        print "Inspecting Resources"
        print "=================================="
        print "Setting last updated time to now"
        print "This will make observers update"
        updated = datetime.now()
        return updated

    @staticmethod
    def upload_resources(args=None):
        moodle_function = "core_files_upload"
        print moodle_function
        return

    @staticmethod
    def download_resources(args=None):
        print "=================================="
        print "Get Resources"
        print "=================================="
        print "Attempting to get resources"
        print "Failed to get resources"
        print "Raising Moodle exception"
        print "=================================="
        raise MoodleException()

    @staticmethod
    def get_courses(args=None):
        print "=================================="
        print "Get Courses"
        print "==================================="
        print "Attempting to get resources"
        print "Returning simulated Moodle courses array"
        return ['CA431', 'CA421', 'CA400']

    @staticmethod
    def get_course_sections(args=None):
        moodle_function = "core_course_get_categories"
        print moodle_function

    @staticmethod
    def create_course_section(args=None):
        moodle_function = "core_course_create_categories"
        print moodle_function

    @staticmethod
    def remove_course_section(args=None):
        moodle_function = "core_course_delete_categories"
        print moodle_function

    @staticmethod
    def get_assignment(args=None):
        print "=================================="
        print "Getting Assignments"
        print "=================================="
        print "Return dummy assignment called 'assignment1'"
        return ['assignment1.pdf']

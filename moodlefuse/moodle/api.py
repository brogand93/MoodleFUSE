#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle import Moodle


class MoodleAPI(object):

    @staticmethod
    def upload_resources(resourcelink):

        return

    @staticmethod
    def download_resources(resourcelink):

        return

    @staticmethod
    def get_courses(args=None):

        args = {
            "function": "core_course_get_courses"
        }
        return Moodle.rest_request(args)

    @staticmethod
    def get_course_resource_links(courseid):
        args = {
            "function": "core_course_get_contents",
            "courseid": courseid
        }
        return Moodle.rest_request(args)

    @staticmethod
    def get_course_sections(courseid):
        args = {
            "function": "core_course_get_categories",
            "courseid": courseid
        }
        return Moodle.rest_request(args)

    @staticmethod
    def create_course_categories(courseid, categories):
        args = {
            "function": "core_course_create_categories",
            "courseid": courseid,
            "categories": categories
        }
        return Moodle.rest_request(args)

    @staticmethod
    def remove_course_categorie(courseid, categories):
        args = {
            "function": "core_course_create_categories",
            "courseid": courseid,
            "categories": categories
        }
        moodle_function = "core_course_delete_categories"
        return Moodle.rest_request(args)

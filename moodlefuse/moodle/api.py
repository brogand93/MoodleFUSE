#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle import Moodle
from moodlefuse.moodle.requester import Requester


class MoodleAPI(object):

    def __init__(self):
        self.requester = Requester()


    def upload_resources(self, source_link, destination_link):
        args = {

        }
        return


    def download_resources(self, source_link, destination_link):
        args = {

        }
        return

    def get_courses(self):

        args = {
            "function": "core_course_get_courses"
        }

        return self.requester.rest_request(args)


    def get_course_resource_links(self, courseid, time_stamp):
        args = {
            "function": "core_course_get_contents",
            "courseid": courseid
        }
        return self.requester.rest_request(args)

    @staticmethod
    def get_course_sections(self, courseid):
        args = {
            "function": "core_course_get_categories",
            "courseid": courseid
        }
        return self.requester.rest_request(args)

    @staticmethod
    def create_course_categories(self, courseid, categories):
        args = {
            "function": "core_course_create_categories",
            "courseid": courseid,
            "categories": categories
        }
        return self.requester.rest_request(args)

    @staticmethod
    def remove_course_categorie(self, courseid, categories):
        args = {
            "function": "core_course_delete_categories",
            "courseid": courseid,
            "categories": categories
        }

        return self.requester.rest_request(args)

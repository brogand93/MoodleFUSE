#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.requester import Requester
from moodlefuse.core import config


class MoodleAPI(object):

    def __init__(self):
        self.requester = Requester()

    def upload_resources(self, source_link, destination_link):
        args = {
            "file_box": "@" + source_link,
            "filepath": destination_link,
            "token": config['MOODLE_TOKEN']
        }

        return self.requester.upload_request(args)

    def download_resources(self, destination_link, source_link):
        args = {
            "token": config['MOODLE_TOKEN']
        }

        return self.requester.download_request(args, source_link, destination_link)

    def get_courses(self):
        args = {
            "wsfunction": "core_course_get_courses",
            "wstoken": config['MOODLE_TOKEN'],
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def get_course_contents(self, courseid):
        args = {
            "wsfunction": "core_course_get_contents",
            "wstoken": config['MOODLE_TOKEN'],
            "courseid": courseid,
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def get_course_resource_links(self, courseid, time_stamp):
        args = {
            "wsfunction": "core_course_get_contents",
            "courseid": courseid,
            "wstoken": config['MOODLE_TOKEN'],
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def get_course_sections(self, courseid):
        args = {
            "wsfunction": "core_course_get_categories",
            "wstoken": config['MOODLE_TOKEN'],
            "courseid": courseid,
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def create_course_categories(self, courseid, categories):
        args = {
            "wsfunction": "core_course_create_categories",
            "wstoken": config['MOODLE_TOKEN'],
            "courseid": courseid,
            "categories": categories
        }

        return self.requester.rest_request(args)

    def remove_course_categorie(self, courseid, categories):
        args = {
            "wsfunction": "core_course_delete_categories",
            "wstoken": config['MOODLE_TOKEN'],
            "courseid": courseid,
            "categories": categories
        }

        return self.requester.rest_request(args)

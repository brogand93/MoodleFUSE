#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.requester import Requester


class MoodleAPI(object):

    def __init__(self):
        self.requester = Requester()

    def upload_resources(self, source_link, destination_link):
        args = {
            "file_box": "@" + source_link,
            "filepath": destination_link
        }

        return self.requester.upload_request(args)

    def download_resources(self, source_link, destination_link):
        args = {
            "remote_path": source_link
        }

        return self.requester.download_request(args)

    def get_courses(self):
        args = {
            "wsfunction": "core_course_get_courses"
        }

        return self.requester.rest_request(args)

    def get_course_resource_links(self, courseid, time_stamp):
        args = {
            "wsfunction": "core_course_get_contents",
            "courseid": courseid
        }

        return self.requester.rest_request(args)

    def get_course_sections(self, courseid):
        args = {
            "wsfunction": "core_course_get_categories",
            "courseid": courseid
        }

        return self.requester.rest_request(args)

    def create_course_categories(self, courseid, categories):
        args = {
            "wsfunction": "core_course_create_categories",
            "courseid": courseid,
            "categories": categories
        }

        return self.requester.rest_request(args)

    def remove_course_categorie(self, courseid, categories):
        args = {
            "wsfunction": "core_course_delete_categories",
            "courseid": courseid,
            "categories": categories
        }

        return self.requester.rest_request(args)

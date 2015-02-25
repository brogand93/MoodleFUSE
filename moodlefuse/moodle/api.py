#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.requester import Requester


class MoodleAPI(object):

    def __init__(self):
        self.requester = Requester()

    def upload_resources(self, source_link, destination_link):
        args = {
            "file_box": "@" + source_link,
            "filepath": destination_link,
            "token": 'c48133e52b502740fbce84eecf7e3110'
        }

        return self.requester.upload_request(args)

    def download_resources(self, source_link, destination_link):
        args = {
            "token": 'c48133e52b502740fbce84eecf7e3110'
        }

        return self.requester.download_request(args, source_link, destination_link)

    def get_courses(self):
        args = {
            "wsfunction": "core_course_get_courses",
            "wstoken": "c48133e52b502740fbce84eecf7e3110",
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def get_course_contents(self, courseid):
        args = {
            "wsfunction": "core_course_get_contents",
            "wstoken": 'c48133e52b502740fbce84eecf7e3110',
            "courseid": courseid,
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def get_course_resource_links(self, courseid, time_stamp):
        args = {
            "wsfunction": "core_course_get_contents",
            "courseid": courseid,
            "wstoken": 'c48133e52b502740fbce84eecf7e3110',
            "moodlewsrestformat": "json"
        }

        return self.requester.rest_request(args)

    def get_course_sections(self, courseid):
        args = {
            "wsfunction": "core_course_get_categories",
            "wstoken": 'c48133e52b502740fbce84eecf7e3110',
            "courseid": courseid,
            "moodlewsrestformat": "json"
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

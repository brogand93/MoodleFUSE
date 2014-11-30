#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.api import MoodleAPI


class MoodleHandler():

    def handle_moodle_action(self, action, error, args):
        try:
            action(args)
        except(MoodleException):
            error()


    def upload_to_moodle(self, items_to_upload, error):
        upload_action = MoodleAPI.upload_resources(items_to_upload)


    def download_from_moodle(self, error):
        pass
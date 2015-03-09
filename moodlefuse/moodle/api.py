#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.emulator import Emulator
from moodlefuse.core import config


class MoodleAPI(object):

    def __init__(self):
        self.emulator = Emulator(config['USERNAME'], config['PASSWORD'])
        self.emulator.login()

    def upload_resources(self, source_link, destination_link):
        pass

    def download_resources(self, destination_link, source_link):
        pass

    def get_courses(self):
        return self.emulator.get_courses()

    def get_course_contents(self, url):
        if url is not None:
            return self.emulator.get_course_categories(url)
        return None

    def get_course_resources(self, course, category):
        pass

    def get_course_sections(self, courseid):
        pass

    def create_course_categories(self, courseid, categories):
        pass

    def remove_course_categorie(self, courseid, categories):
        pass

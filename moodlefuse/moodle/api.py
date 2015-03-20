#!/usr/bin/env python
# encoding: utf-8

"""Class to act as a bridge between the Moodle emulator and handlers
"""

from moodlefuse.moodle.emulator import Emulator
from moodlefuse.core import config


class MoodleAPI(object):

    def __init__(self):
        self.emulator = Emulator(config['USERNAME'], config['PASSWORD'])
        self.emulator.login()

    def upload_resources(self, source_link, destination_link):
        pass

    def set_modify_moodle(self, modify=True):
        if modify is True:
            return self.emulator.turn_course_editing_on()
        else:
            return self.emulator.turn_course_editing_on()

    def follow_link(self, link):
        return self.emulator.open_link(link)

    def select_page_form(self):
        self.emulator.set_form_to_first_form()

    def download_resources(self, destination_link, source_link):
        self.emulator.download(destination_link, source_link)

    def get_courses(self):
        return self.emulator.get_courses()

    def get_course_contents(self, url):
        if url is not None:
            return self.emulator.get_course_categories(url)
        return None

    def create_course_categories(self, categoryname):
        pass

    def remove_course_categorie(self, categoryname):
        pass

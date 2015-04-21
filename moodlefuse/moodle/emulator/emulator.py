#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.helpers import throws_moodlefuse_error
from moodlefuse.moodle import exception
from moodlefuse.core import config
from moodlefuse import moodle


class Emulator(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def setup_emulator(self):
        pass

    def login(self):
        pass

    def turn_course_editing_on(self):
        pass

    def turn_course_editing_off(self):
        pass

    def close(self):
        pass

    @throws_moodlefuse_error(exception.NotFoundException)
    def open_login_page(self, open_url_function):
        if not config['MOODLE_WEB_ADDRESS'].endswith('php') and not config['MOODLE_WEB_ADDRESS'].endswith('html'):
            MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS'] + moodle.LOGIN_LOCATION
        else:
            MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS']

        open_url_function(MOODLE_LOGIN_URL)

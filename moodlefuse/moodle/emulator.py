#!/usr/bin/env python
# encoding: utf-8

"""Class to spin up a headless browser to handle Moodle interaction
"""

from bs4 import BeautifulSoup
from moodlefuse.core import config
from mechanize import Browser, CookieJar
from moodlefuse.moodle.exception import LoginException


class Emulator(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.setup_emulator()

    def setup_emulator(self):
        self.browser = Browser()
        self.cookiejar = CookieJar()
        self.browser.set_cookiejar(self.cookiejar)

    def login(self):
        MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS'] + '/login/index.php'
        self.browser.open(MOODLE_LOGIN_URL)
        self.browser.select_form(
            predicate=lambda form: form.attrs.get('id') == 'login'
        )
        self.browser.form.set_value(self.username, name='username')
        self.browser.form.set_value(self.password, name='password')
        resp = self.browser.submit()

        if resp.geturl().endswith('/login/index.php'):
            raise LoginException(self.username)

    def upload(self):
        pass

    def download(self, destination, source):
        self.browser.retrieve(source, destination)

    def open_link(self, url):
        response = self.browser.open(url)
        return BeautifulSoup(response.read())

    def turn_course_editing_on(self):
        response = self.browser.submit(label='Turn editing on')
        return BeautifulSoup(response.read())

    def turn_course_editing_off(self):
        response = self.browser.submit(label='Turn editing off')
        return BeautifulSoup(response.read())

    def get_courses(self):
        return self.open_link(config['MOODLE_INDEX_ADDRESS'])

    def get_course_categories(self, url):
        return self.open_link(url)

    def get_course_resource_names(self, url):
        return self.open_link(url)

    def download_resourse(self, resourcename):
        pass

    def upload_resource(self):
        pass

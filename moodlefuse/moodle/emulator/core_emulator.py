#!/usr/bin/env python
# encoding: utf-8

"""Class to spin up a headless browser to handle Moodle interaction
"""

from bs4 import BeautifulSoup
from moodlefuse.core import config
from mechanize import Browser, CookieJar
from moodlefuse.moodle.exception import LoginException


class CoreEmulator(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.setup_emulator()

    def setup_emulator(self):
        self.browser = Browser()
        self.browser.addheaders = [
            (
                'User-agent',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
            )
        ]
        self.cookiejar = CookieJar()
        self.browser.set_cookiejar(self.cookiejar)

    def login(self):
        if not config['MOODLE_WEB_ADDRESS'].endswith('php') and not config['MOODLE_WEB_ADDRESS'].endswith('html'):
            MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS'] + '/login/index.php'
        else:
            MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS']

        self.browser.open(MOODLE_LOGIN_URL)
        self.browser.select_form(
            predicate=lambda form: form.attrs.get('id') == 'login'
        )
        self.browser.form.set_value(self.username, name='username')
        self.browser.form.set_value(self.password, name='password')
        resp = self.browser.submit()

        if resp.geturl().endswith('/login/index.php'):
            raise LoginException(self.username)

    def download(self, destination, source):
        self.browser.retrieve(source, destination)

    def open_link(self, url):
        response = self.browser.open(url)
        return BeautifulSoup(response.read())

    def check_form_checkbox(self, checkboxname):
        self.browser.find_control(checkboxname).items[0].selected = True

    def add_form_content(self, inputname, content):
        self.browser.form.set_value(content, name=inputname)

    def close_form(self):
        self.browser.submit()

    def get_current_url(self):
        return self.browser.geturl()

    def set_form_to_first_form(self):
        self.browser.select_form(nr=0)

    def set_form_to_form_with_control_value(self, value):
        for form in self.browser.forms():
            for control in form.controls:

                if control.value == value:
                    self.browser.form = form

    def turn_course_editing_on(self):
        self.set_form_to_form_with_control_value('Turn editing on')
        response = self.browser.submit()
        return BeautifulSoup(response.read())

    def filter_assignment_submissions(self):
        self.browser.form = list(self.browser.forms())[2]
        self.browser.form["filter"] = ["submitted"]
        self.browser.form["perpage"] = ["100"]
        response = self.browser.submit()
        return BeautifulSoup(response.read())

    def turn_course_editing_off(self):
        self.set_form_to_form_with_control_value('Turn editing off')
        response = self.browser.submit()
        return BeautifulSoup(response.read())

    def get_courses(self):
        return self.open_link(config['MOODLE_INDEX_ADDRESS'])

    def get_course_categories(self, url):
        return self.open_link(url)

    def get_course_resource_names(self, url):
        return self.open_link(url)

    def close(self):
        self.browser.close()

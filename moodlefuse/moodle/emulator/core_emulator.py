#!/usr/bin/env python
# encoding: utf-8

"""Class to spin up a headless browser to handle Moodle interaction
"""

from mechanize import Browser, CookieJar
from bs4 import BeautifulSoup

from moodlefuse.moodle.emulator.emulator import Emulator
from moodlefuse.moodle.resources import resource_errors
from moodlefuse.helpers import throws_moodlefuse_error
from moodlefuse.moodle.courses import course_errors
from moodlefuse.moodle import exception, attributes
from moodlefuse.core import config
from moodlefuse import moodle


class CoreEmulator(Emulator):

    def __init__(self, username, password):
        super(CoreEmulator, self).__init__(username, password)
        self.setup_emulator()

    def setup_emulator(self):
        self.browser = Browser()
        self.browser.set_handle_robots(False)
        self.browser.addheaders = moodle.USER_AGENT
        self.cookiejar = CookieJar()
        self.browser.set_cookiejar(self.cookiejar)

    def login(self):
        self.open_login_page(self.browser.open)
        self.browser.select_form(
            predicate=lambda form: form.attrs.get('id') == attributes.LOGIN
        )
        self.browser.form.set_value(self.username, name='username')
        self.browser.form.set_value(self.password, name='password')
        resp = self.browser.submit()

        if resp.geturl().endswith(moodle.LOGIN_LOCATION):
            raise Exception

    @throws_moodlefuse_error(resource_errors.UnableToDownloadResource)
    def download(self, destination, source):
        source = str(source)
        if not source.startswith('http://') and not source.startswith('file://'):
            source = config['TEST_DATA'] + '/' + source

        self.browser.retrieve(source, destination)

    def open_link(self, url):
        response = self.browser.open(url)
        return BeautifulSoup(response.read())

    def check_form_checkbox(self, checkboxname):
        self.browser.find_control(checkboxname).items[0].selected = True

    def uncheck_form_checkbox(self, checkboxname):
        self.browser.find_control(checkboxname).items[0].selected = False

    def add_form_content(self, inputname, content):
        self.browser.form.set_value(content, name=inputname)

    def close_form(self):
        self.browser.submit()

    def set_form_to_first_form(self):
        self.browser.select_form(nr=0)

    def set_form_to_form_with_control_value(self, value):
        for form in self.browser.forms():
            for control in form.controls:
                if control.value == value:
                    self.browser.form = form

    @throws_moodlefuse_error(exception.UnableToToggleEditing)
    def turn_course_editing_on(self):
        self.set_form_to_form_with_control_value(moodle.EDIT_ON_MOODLE_BUTTON_TEXT)
        response = self.browser.submit()
        return BeautifulSoup(response.read())

    def _setup_assignments_for_parsing(self, submission_filter):
        self.set_form_to_form_with_control_value('Save and update table')
        self.browser.form["filter"] = [submission_filter]
        self.browser.form["perpage"] = ["100"]
        self.uncheck_form_checkbox('quickgrading')
        response = self.browser.submit()
        return BeautifulSoup(response.read())

    def filter_assignment_submissions(self):
        return self._setup_assignments_for_parsing("submitted")

    def unfilter_assignment_submissions(self):
        return self._setup_assignments_for_parsing("")

    @throws_moodlefuse_error(exception.UnableToToggleEditing)
    def turn_course_editing_off(self):
        self.set_form_to_form_with_control_value(moodle.EDIT_OFF_MOODLE_BUTTON_TEXT)
        response = self.browser.submit()
        return BeautifulSoup(response.read())

    @throws_moodlefuse_error(course_errors.InvalidMoodleIndex)
    def get_courses(self):
        return self.open_link(config['MOODLE_INDEX_ADDRESS'])

    @throws_moodlefuse_error(course_errors.UnableToObtainCategoryList)
    def get_course_categories(self, url):
        return self.open_link(url)

    @throws_moodlefuse_error(resource_errors.UnableToObtainResourceList)
    def get_course_resource_names(self, url):
        return self.open_link(url)

    def close(self):
        self.browser.close()

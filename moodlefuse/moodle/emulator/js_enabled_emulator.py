#!/usr/bin/env python
# encoding: utf-8

"""Class to spin up a javscript enabled browser to handle Moodle
   interaction
"""

import time

from selenium import webdriver
from xvfbwrapper import Xvfb

from moodlefuse.moodle.emulator.emulator import Emulator
from moodlefuse.moodle.resources import resource_errors
from moodlefuse.helpers import throws_moodlefuse_error
from moodlefuse.moodle.courses import course_errors
from moodlefuse.moodle import exception, paths
from moodlefuse.moodle import attributes
from moodlefuse.core import config


class JsEmulator(Emulator):

    def __init__(self, username, password):
        super(JsEmulator, self).__init__(username, password)
        self.setup_emulator()

    def setup_emulator(self):
        if config['DEBUG'] is False:
            self.vdisplay = Xvfb(width=1280, height=720)
            self.vdisplay.xvfb_cmd.append('-noreset')
            self.vdisplay.xvfb_cmd.append('-ac')
            self.vdisplay.start()
        self.driver = webdriver.Firefox()

    def open_add_resource_menu(self, category):
        element = self.driver.find_element_by_xpath(paths.CATEGORY.format(category))
        resource_menu = element.find_element_by_class_name(attributes.SECTION)
        resource_menu.click()

    def open_edit_resource_menu(self, category, resource_name):
        xpath = paths.RESOURCE.format(category, resource_name)
        element = self.driver.find_element_by_xpath(xpath)
        element = element.find_element_by_xpath(paths.THIRD_PARENT)
        element.find_element_by_xpath(paths.EDIT_BUTTON).click()
        element.find_element_by_xpath(paths.SETTINGS).click()

    @throws_moodlefuse_error(resource_errors.UnableToRemoveFile)
    def delete_resource(self, category, resource_name):
        xpath = paths.RESOURCE.format(category, resource_name)
        element = self.driver.find_element_by_xpath(xpath)
        element = element.find_element_by_xpath(paths.THIRD_PARENT)
        element.find_element_by_xpath(paths.EDIT_BUTTON).click()
        element.find_element_by_xpath(paths.DELETE).click()
        alert = self.driver.switch_to_alert()
        alert.accept()

    @throws_moodlefuse_error(resource_errors.UnableToRenameFile)
    def rename_file(self, category, old_name, new_name):
        self.open_edit_resource_menu(category, old_name)
        self.rename_file_from_edit_screen(new_name)
        self.driver.find_element_by_id(attributes.SUBMIT2_ID).click()

    def click_option(self, select, desired_option):
        element = self.driver.find_element_by_id(select)
        for option in element.find_elements_by_tag_name('option'):
            if option.text == desired_option:
                option.click()

    def filter_assignments(self):
        self.click_option('id_filter', 'No filter')
        self.click_option('id_perpage', '100')
        self.driver.find_element_by_xpath(paths.QUICK_GRADING_OPTION).click()

    def unfilter_assignments(self):
        self.driver.find_element_by_xpath(paths.QUICK_GRADING_OPTION).click()

    def grade_assignments(self, grades):
        self.filter_assignments()
        for grade in grades:
            element = self.driver.find_element_by_xpath(paths.USER_ROW.format(grade[1]))
            element = element.find_element_by_xpath(paths.PARENT)
            element = element.find_element_by_xpath(paths.GRADE_BOX)
            element.send_keys(webdriver.common.keys.Keys.CONTROL, 'a')
            element.send_keys(str(grade[2]))
            element.send_keys(webdriver.common.keys.Keys.RETURN)
            time.sleep(.5)
            self.driver.find_element_by_xpath(paths.CONTINUE).click()

        self.unfilter_assignments()

    def rename_file_from_edit_screen(self, new_name):
        time.sleep(.5)
        element = self.enter_text_into_textbox(attributes.NAME_ID, new_name)
        element.send_keys(webdriver.common.keys.Keys.TAB)
        element = self.driver.switch_to.active_element
        element.click()
        element.send_keys(webdriver.common.keys.Keys.CONTROL, 'a')
        element.send_keys(new_name)

    @throws_moodlefuse_error(resource_errors.UnableToAddFile)
    def add_resource(self, resource_name, resource_path):
        self.driver.find_element_by_xpath(paths.FILE).click()
        self.driver.find_element_by_name(attributes.SUBMIT).click()
        self.rename_file_from_edit_screen(resource_name)
        self.edit_resource_content(resource_path)
        self.driver.find_element_by_id(attributes.SUBMIT2_ID).click()

    @throws_moodlefuse_error(resource_errors.UnableToModifyFile)
    def edit_resource_content(self, resource_path):
        time.sleep(.5)
        self.driver.find_element_by_class_name(attributes.FILE_CONTENT).click()
        self.driver.find_element_by_class_name(attributes.DELETE_FILE).click()
        self.driver.find_element_by_class_name(attributes.CONFIRM).click()
        self.driver.find_element_by_xpath(paths.UPLOAD).click()
        element = self.driver.find_element_by_css_selector(attributes.FILE)
        element.send_keys(resource_path)
        self.driver.find_element_by_class_name(attributes.UPLOAD).click()

    @throws_moodlefuse_error(course_errors.UnableToOAddCourseCategory)
    def change_most_recent_categoryname(self, new_name):
        self.check_form_checkbox(attributes.DEFAULT_NAME_ID)
        self.enter_text_into_textbox(attributes.NAME_ID, new_name)
        self.close_form()

    @throws_moodlefuse_error(exception.LoginException)
    def login(self):
        self.open_login_page(self.driver.get)
        element = self.driver.find_element_by_id(attributes.USERNAME_ID)
        element.send_keys(self.username)
        element = self.driver.find_element_by_id(attributes.PASSWORD_ID)
        element.send_keys(self.password)
        self.driver.find_element_by_id(attributes.LOGIN_ID).click()

    def open_link(self, url):
        self.driver.get(url)

    def check_form_checkbox(self, checkboxid):
        if self.driver.find_element_by_id(checkboxid).is_selected():
            self.driver.find_element_by_id(checkboxid).click()

    def enter_text_into_textbox(self, textbox, text):
        element = self.driver.find_element_by_id(textbox)
        element.clear()
        element.send_keys(text)
        return element

    @throws_moodlefuse_error(exception.UnableToToggleEditing)
    def turn_course_editing_on(self):
        element = self.driver.find_element_by_xpath(paths.EDIT_ON)
        element.click()

    @throws_moodlefuse_error(exception.UnableToToggleEditing)
    def turn_course_editing_off(self):
        element = self.driver.find_element_by_xpath(paths.EDIT_OFF)
        element.click()

    def close_form(self):
        self.driver.find_element_by_id(attributes.SUBMIT_ID).click()

    def close(self):
        self.driver.quit()
        if config['DEBUG'] is False:
            self.vdisplay.stop()

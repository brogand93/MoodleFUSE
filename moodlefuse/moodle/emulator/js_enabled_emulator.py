#!/usr/bin/env python
# encoding: utf-8

"""Class to spin up a javscript enabled browser to handle Moodle
   interaction
"""

import time

from selenium import webdriver
from xvfbwrapper import Xvfb

from moodlefuse.moodle.resources import resource_errors
from moodlefuse.helpers import throws_moodlefuse_error
from moodlefuse.moodle.courses import course_errors
from moodlefuse.moodle import exception
from moodlefuse.core import config


class JsEmulator(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.setup_emulator()

    def setup_emulator(self):
        self.vdisplay = Xvfb(width=1280, height=720)
        self.vdisplay.xvfb_cmd.append('-noreset')
        self.vdisplay.xvfb_cmd.append('-ac')
        self.vdisplay.start()
        self.driver = webdriver.Firefox()

    def open_add_resource_menu(self, category):
        element = self.driver.find_element_by_xpath("//li[@aria-label='{0}']".format(category))
        resource_menu = element.find_element_by_class_name('section-modchooser-text')
        resource_menu.click()

    def open_edit_resource_menu(self, category, resource_name):
        xpath = "//li[@aria-label='{0}']//span[contains(text(), '{1}')]".format(
            category, resource_name
        )
        element = self.driver.find_element_by_xpath(xpath)
        element = element.find_element_by_xpath("../../..")
        element.find_element_by_xpath(".//a[contains(text(), 'Edit')]").click()
        element.find_element_by_xpath(".//span[contains(text(), 'Edit settings')]").click()

    @throws_moodlefuse_error(resource_errors.UnableToRemoveFile)
    def delete_resource(self, category, resource_name):
        xpath = "//li[@aria-label='{0}']//span[contains(text(), '{1}')]".format(
            category, resource_name
        )
        element = self.driver.find_element_by_xpath(xpath)
        element = element.find_element_by_xpath("../../..")
        element.find_element_by_xpath(".//a[contains(text(), 'Edit')]").click()
        element.find_element_by_xpath(".//span[contains(text(), 'Delete')]").click()
        alert = self.driver.switch_to_alert()
        alert.accept()

    @throws_moodlefuse_error(resource_errors.UnableToRenameFile)
    def rename_file(self, category, old_name, new_name):
        self.open_edit_resource_menu(category, old_name)
        self.rename_file_from_edit_screen(new_name)
        self.driver.find_element_by_id("id_submitbutton2").click()

    def open_assignment_grading_and_submission_page(self):
        self.driver.find_element_by_xpath("//a[containts(text(), 'View/grade all submissions')]").click()

    def rename_file_from_edit_screen(self, new_name):
        time.sleep(.5)
        element = self.enter_text_into_textbox("id_name", new_name)
        element.send_keys(webdriver.common.keys.Keys.TAB)
        element = self.driver.switch_to.active_element
        element.click()
        element.send_keys(webdriver.common.keys.Keys.CONTROL, 'a')
        element.send_keys(new_name)

    @throws_moodlefuse_error(resource_errors.UnableToAddFile)
    def add_resource(self, resource_name, resource_path):
        self.driver.find_element_by_xpath("//span[contains(text(), 'File') and @class='typename']").click()
        self.driver.find_element_by_name("submitbutton").click()
        self.rename_file_from_edit_screen(resource_name)
        self.edit_resource_content(resource_path)
        self.driver.find_element_by_id("id_submitbutton2").click()

    @throws_moodlefuse_error(resource_errors.UnableToModifyFile)
    def edit_resource_content(self, resource_path):
        time.sleep(.5)
        self.driver.find_element_by_class_name('fp-mainfile').click()
        self.driver.find_element_by_class_name('fp-file-delete').click()
        self.driver.find_element_by_class_name('fp-dlg-butconfirm').click()
        self.driver.find_element_by_xpath("//div[@class='fp-btn-add']").click()
        element = self.driver.find_element_by_css_selector("input[type='file']")
        element.send_keys(resource_path)
        self.driver.find_element_by_class_name("fp-upload-btn").click()

    @throws_moodlefuse_error(course_errors.UnableToOAddCourseCategory)
    def change_most_recent_categoryname(self, new_name):
        self.check_form_checkbox('id_usedefaultname')
        self.enter_text_into_textbox('id_name', new_name)
        self.close_form()

    @throws_moodlefuse_error(exception.NotFoundException)
    def open_login_page(self):
        if not config['MOODLE_WEB_ADDRESS'].endswith('php') and not config['MOODLE_WEB_ADDRESS'].endswith('html'):
            MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS'] + '/login/index.php'
        else:
            MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS']
        self.driver.get(MOODLE_LOGIN_URL)

    @throws_moodlefuse_error(exception.LoginException)
    def login(self):
        self.open_login_page()
        element = self.driver.find_element_by_id("username")
        element.send_keys(self.username)
        element = self.driver.find_element_by_id("password")
        element.send_keys(self.password)
        self.driver.find_element_by_id("loginbtn").click()

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
    def turn_editing_on(self):
        element = self.driver.find_element_by_xpath("//* [@type='submit'][@value='Turn editing on']")
        element.click()

    @throws_moodlefuse_error(exception.UnableToToggleEditing)
    def turn_editing_off(self):
        element = self.driver.find_element_by_xpath("//* [@type='submit'][@value='Turn editing off']")
        element.click()

    def close_form(self):
        self.driver.find_element_by_id("id_submitbutton").click()

    def close(self):
        self.driver.quit()
        self.vdisplay.stop()

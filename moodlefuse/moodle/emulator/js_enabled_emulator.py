#!/usr/bin/env python
# encoding: utf-8

import time
from selenium import webdriver
from moodlefuse.core import config


class JsEmulator(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.setup_emulator()

    def setup_emulator(self):
        self.driver = webdriver.Firefox()

    def open_add_resource_menu(self, category):
        element = self.driver.find_element_by_xpath("//li[@aria-label='{0}']".format(category))
        resource_menu = element.find_element_by_class_name('section-modchooser-text')
        resource_menu.click()

    def add_resource(self, resource_name, resource_path):
        element = self.driver.find_element_by_xpath("//span[contains(text(), 'File') and @class='typename']")
        element.click()
        self.driver.find_element_by_name("submitbutton").click()
        element = self.driver.find_element_by_id("id_name")
        element.send_keys(resource_name)
        element.send_keys(webdriver.common.keys.Keys.TAB)
        element = self.driver.switch_to.active_element
        element.send_keys(resource_name)
        element = self.driver.find_element_by_xpath("//div[@class='fp-btn-add']")
        element.click()
        element = self.driver.find_element_by_css_selector("input[type='file']")
        element.send_keys(resource_path)
        self.driver.find_element_by_class_name("fp-upload-btn").click()
        self.driver.find_element_by_id("id_submitbutton2").click()

    def login(self):
        _MOODLE_LOGIN_URL = config['MOODLE_WEB_ADDRESS'] + '/login/index.php'
        self.driver.get(_MOODLE_LOGIN_URL)
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

    def turn_editing_on(self):
        element = self.driver.find_element_by_xpath("//* [@type='submit'][@value='Turn editing on']")
        element.click()

    def upload(self, filepath, filename):
        pass

    def close_form(self):
        self.driver.find_element_by_id("id_submitbutton").click()

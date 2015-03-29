#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from moodlefuse.core import config


class JsEmulator(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.setup_emulator()

    def setup_emulator(self):
        self.driver = webdriver.Firefox()

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

    def upload(self, filepath, filename):
        pass

    def close_form(self):
        self.driver.find_element_by_id("id_submitbutton").click()

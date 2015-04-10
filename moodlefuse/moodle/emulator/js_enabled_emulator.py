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

    def open_edit_resource_menu(self, category, resource_name):
        xpath = "//li[@aria-label='{0}']//span[contains(text(), '{1}')]".format(
            category, resource_name
        )
        element = self.driver.find_element_by_xpath(xpath)
        element = element.find_element_by_xpath("../../..")
        element.find_element_by_xpath(".//a[contains(text(), 'Edit')]").click()
        element.find_element_by_xpath(".//span[contains(text(), 'Edit settings')]").click()

    def rename_file(self, category, old_name, new_name):
        self.open_edit_resource_menu(category, old_name)
        self.rename_file_from_edit_screen(new_name)
        self.driver.find_element_by_id("id_submitbutton2").click()

    def rename_file_from_edit_screen(self, new_name):
        time.sleep(.5)
        element = self.enter_text_into_textbox("id_name", new_name)
        element.send_keys(webdriver.common.keys.Keys.TAB)
        element = self.driver.switch_to.active_element
        element.click()
        element.send_keys(webdriver.common.keys.Keys.CONTROL, 'a')
        element.send_keys(new_name)

    def add_resource(self, resource_name, resource_path):
        self.driver.find_element_by_xpath("//span[contains(text(), 'File') and @class='typename']").click()
        self.driver.find_element_by_name("submitbutton").click()
        self.rename_file_from_edit_screen(resource_name)
        self.edit_resource_content(resource_path)
        self.driver.find_element_by_id("id_submitbutton2").click()

    def edit_resource_content(self, resource_path):
        time.sleep(.5)
        self.driver.find_element_by_class_name('fp-mainfile').click()
        self.driver.find_element_by_class_name('fp-file-delete').click()
        self.driver.find_element_by_class_name('fp-dlg-butconfirm').click()
        self.driver.find_element_by_xpath("//div[@class='fp-btn-add']").click()
        element = self.driver.find_element_by_css_selector("input[type='file']")
        element.send_keys(resource_path)
        self.driver.find_element_by_class_name("fp-upload-btn").click()

    def change_most_recent_categoryname(self, new_name):
        self.check_form_checkbox('id_usedefaultname')
        self.enter_text_into_textbox('id_name', new_name)
        self.close_form()

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
        return element

    def turn_editing_on(self):
        element = self.driver.find_element_by_xpath("//* [@type='submit'][@value='Turn editing on']")
        element.click()

    def turn_editing_off(self):
        element = self.driver.find_element_by_xpath("//* [@type='submit'][@value='Turn editing off']")
        element.click()

    def close_form(self):
        self.driver.find_element_by_id("id_submitbutton").click()

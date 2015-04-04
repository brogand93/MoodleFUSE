#!/usr/bin/env python
# encoding: utf-8

"""Class to act as a bridge between the Moodle emulator and handlers
"""


class MoodleAPI(object):

    def __init__(self, emulator, js_emulator):
        self.emulator = emulator
        self.js_emulator = js_emulator

    def upload_resources(self, source_link, destination_link):
        pass

    def set_modify_moodle(self, modify=True):
        if modify is True:
            return self.emulator.turn_course_editing_on()
        else:
            return self.emulator.turn_course_editing_on()

    def follow_link(self, link):
        return self.emulator.open_link(link)

    def follow_link_with_js(self, link):
        return self.js_emulator.open_link(link)

    def get_current_url(self):
        return self.emulator.get_current_url()

    def add_new_resource(self, category, resource_name, resource_path):
        self.js_emulator.turn_editing_on()
        self.js_emulator.open_add_resource_menu(category)
        self.js_emulator.add_resource(resource_name, resource_path)

    def change_category_name(self, newname):
        self.js_emulator.check_form_checkbox('id_usedefaultname')
        self.js_emulator.enter_text_into_textbox('id_name', newname)
        self.js_emulator.close_form()

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

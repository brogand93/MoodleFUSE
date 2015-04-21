#!/usr/bin/env python
# encoding: utf-8

"""Class to act as a bridge between the Moodle emulator and handlers
"""

from moodlefuse.moodle import requires_editing_moodle_js


class MoodleAPI(object):

    def __init__(self, emulator, js_emulator):
        self.emulator = emulator
        self.js_emulator = js_emulator

    def set_modify_moodle(self, modify=True):
        if modify is True:
            return self.emulator.turn_course_editing_on()
        else:
            return self.emulator.turn_course_editing_off()

    def follow_link(self, link):
        return self.emulator.open_link(link)

    def follow_link_with_js(self, link):
        return self.js_emulator.open_link(link)

    def filter_assignment_submissions(self):
        return self.emulator.filter_assignment_submissions()

    def unfilter_assignment_submissions(self):
        return self.emulator.unfilter_assignment_submissions()

    def modify_assignment_grades(self, grades):
        self.js_emulator.grade_assignments(grades)

    @requires_editing_moodle_js()
    def add_new_resource(self, category, resource_name, resource_path):
        self.js_emulator.open_add_resource_menu(category)
        self.js_emulator.add_resource(resource_name, resource_path)

    @requires_editing_moodle_js()
    def remove_existing_resource(self, category, resource_name):
        self.js_emulator.delete_resource(category, resource_name)

    @requires_editing_moodle_js()
    def modify_existing_resource(self, category, resource_name, resource_path):
        self.js_emulator.open_edit_resource_menu(category, resource_name)
        self.js_emulator.edit_resource_content(resource_path)

    @requires_editing_moodle_js()
    def rename_existing_resource(self, category, old_resource_name, new_resource_name):
        self.js_emulator.rename_file(category, old_resource_name, new_resource_name)

    @requires_editing_moodle_js()
    def change_category_name(self, new_name):
        self.js_emulator.change_most_recent_categoryname(new_name)

    def download_resources(self, destination_link, source_link):
        self.emulator.download(destination_link, source_link)

    def get_courses(self):
        return self.emulator.get_courses()

    def get_course_contents(self, url):
        if url is not None:
            return self.emulator.get_course_categories(url)
        return None

    def close_api(self):
        self.js_emulator.close()
        self.emulator.close()

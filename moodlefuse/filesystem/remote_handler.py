#!/usr/bin/env python
# encoding: utf-8

"""Class to carry out Moodle operations
"""

FUSE_TRASH = '.Trash-1000'


class RemoteHandler(object):

    def __init__(self, courses, resources, assignments):
        self.courses = courses
        self.resources = resources
        self.assignments = assignments

    def get_category_contents(self, location):
        course_contents = self.courses.enter_course_and_get_contents(location[0])
        return self.courses.get_course_category_contents(course_contents, location[1])

    def modify_grades(self, location):
        assignment_url = self.get_remote_assignment_path(location)
        return self.assignments.modify_grades(location, assignment_url)

    def get_remote_resourse_names(self, location):
        if location[0] == FUSE_TRASH:
            return None
        category_contents = self.get_category_contents(location)
        return self.resources.get_file_names_as_array(category_contents)

    def get_remote_grading_csv(self, location):
        assignment_url = self.get_remote_assignment_path(location)
        return self.assignments.get_grades_csv(location, assignment_url)

    def get_remote_courses(self, location=None):
        return self.courses.get_courses_as_array()

    def get_remote_categories(self, location):
        return self.courses.get_course_categories_as_array(location[0])

    def add_category(self, location):
        self.courses.enter_course_and_get_contents(location[0])
        self.courses.add_new_category(location[1])

    def add_resource(self, location, path):
        self.courses.enter_course_with_js(location[0])
        self.resources.add_resource(path, location[1], location[2])

    def modify_resource(self, location, path):
        self.courses.enter_course_with_js(location[0])
        self.resources.modify_resource(path, location[1], location[2])

    def remove_resource(self, location):
        self.courses.enter_course_with_js(location[0])
        self.resources.remove_resource(location[1], location[2])

    def rename_resource(self, old_location, new_location):
        self.courses.enter_course_with_js(old_location[0])
        self.resources.rename_resource(old_location[1], old_location[2], new_location[3])

    def get_remote_assignment_names(self, location):
        category_contents = self.get_category_contents(location)
        assignment_url = self.resources.get_assignment_url(category_contents, location[2])
        return self.assignments.get_assignment_submissions(assignment_url)

    def get_remote_file_path(self, location):
        category_contents = self.get_category_contents(location)
        return self.resources.get_file_path(category_contents, location[2])

    def get_remote_assignment_path(self, location):
        category_contents = self.get_category_contents(location)
        return self.resources.get_assignment_url(category_contents, location[2])

    def get_remote_assignment_info(self, location=None):
        return self.assignments.get_assignment_info_as_array()

    def get_remote_assignment_submissions(self, location):
        assignment_url = self.get_remote_assignment_path(location)
        return self.assignments.get_assignment_submissions(assignment_url)

    def download_updated_file(self, location, moodle_url):
        return self.resources.download_resource(location, moodle_url)

    def is_valid_root(self, location=None):
        return True

    def is_valid_course(self, location):
        return location[0] in self.get_remote_courses()

    def is_valid_category(self, location):
        return location[1] in self.get_remote_categories(location)

    def is_valid_resource(self, location):
        return location[2] in self.get_remote_resourse_names(location)

    def is_valid_assignment(self, location):
        category_contents = self.get_category_contents(location)
        return self.resources.is_assignment(category_contents, location[2])

    def is_valid_assignment_info(self, location):
        return location[3] in self.get_remote_assignment_info()

    def is_valid_assignment_submission(self, location):
        return location[4] in self.get_remote_assignment_submissions(location)

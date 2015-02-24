#!/usr/bin/env python
# encoding: utf-8

"""Class to handle course Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.moodle_handler import MoodleHandler
from moodlefuse.moodle.api import MoodleAPI


class CourseHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def get_courses_as_array(self):
        courses = self.moodle.get_courses()
        return self._parse_courses(courses)

    def get_course_id_by_name(self, coursename):
        courses = self.moodle.get_courses()
        for course in courses:
            if course['fullname'] == coursename:
                return course['id']

        return 0

    def _parse_courses(self, courses_dictionary):
        courses = []
        for course in courses_dictionary:
            if course['id'] is not 1:
                courses.append(course['fullname'])

        return courses

    def get_course_categories_as_array(self, course):
        categories = self.moodle.get_course_contents(course)
        return self._parse_course_categories(categories)

    def _parse_course_categories(self, categories_dictionary):
        categories = []
        for categorie in categories_dictionary:
            if categorie['id'] is not 1:
                categories.append(categorie['name'])

        return categories

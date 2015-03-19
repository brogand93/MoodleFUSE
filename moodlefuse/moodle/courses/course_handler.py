#!/usr/bin/env python
# encoding: utf-8

"""Class to handle course Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.courses.course_parser import CourseParser
from moodlefuse.moodle.handler import MoodleHandler


class CourseHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.parser = CourseParser()

    def get_courses_as_array(self):
        course_scraper = self.moodle.get_courses()
        return self.parser.parse_courses(course_scraper)

    def get_course_categories_as_array(self, course):
        course_contents = self.enter_course_and_get_contents(course)
        return self.parser.parse_course_category_titles(course_contents)

    def enter_course_and_get_contents(self, course):
        courses_scrapper = self.moodle.get_courses()
        course_link = self.parser.get_course_link(courses_scrapper, course)
        course_page = self.moodle.get_course_contents(course_link)
        return self.parser.parse_course_content_from_page(course_page)

    def get_course_category_contents(self, course_content, category):
        return self.parser.parse_course_category_from_course(
            course_content,
            category)

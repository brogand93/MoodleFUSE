#!/usr/bin/env python
# encoding: utf-8

"""Class to handle course Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.handler import MoodleHandler


class CourseHandler(MoodleHandler):

    def __init__(self):
        super(self.__class__, self).__init__()

    def get_courses_as_array(self):
        course_scraper = self.moodle.get_courses()
        return self._parse_courses(course_scraper)

    def _parse_courses(self, course_scraper):
        course_scraper = self.scraper.get_html_with_divclass(
            course_scraper, 'courses frontpage-course-list-all')

        courses = course_scraper.findAll(text=True)
        return self.remove_unicode(courses)

    def get_course_categories_as_array(self, course):
        courses_scrapper = self.moodle.get_courses()
        return self._parse_course_categories(courses_scrapper, course)

    def _parse_course_categories(self, course_scraper, course):
        course_link = self.scraper.get_link_from_linktext_in_divclass(
            course_scraper, 'courses frontpage-course-list-all', course)
        course_content = self.moodle.get_course_contents(course_link)
        course_categories_html = self.scraper.get_html_with_divclass(
            course_content, 'course-content')

        sections_html = course_categories_html.select('h3')
        sections = []
        for categorie in sections_html:
            sections.append(categorie.get_text())

        return self.remove_unicode(sections)

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.parser import Parser


class CourseParser(Parser):

    def __init__(self):
        super(CourseParser, self).__init__()

    def parse_courses(self, course_scraper):
        return self._parse_flat_courses(course_scraper)

    def _parse_flat_courses(self, course_scraper):
        course_scraper = self.scraper.get_html_with_divclass(
            course_scraper, 'courses frontpage-course-list-all')

        courses = course_scraper.findAll(text=True)
        return self.remove_unicode(courses)

    def _parse_table_courses(self, course_scraper):
        pass

    def parse_course_categories(self, course_content):
        categories_html = self.scraper.get_html_with_divclass(
            course_content, 'course-content')

        sections = self.scraper.get_text_from_taged_item(categories_html, 'h3')

        return self.remove_unicode(sections)

    def get_course_link(self, course_scraper, course):
        course_link = self.scraper.get_link_from_linktext_in_divclass(
            course_scraper, 'courses frontpage-course-list-all', course)

        return course_link
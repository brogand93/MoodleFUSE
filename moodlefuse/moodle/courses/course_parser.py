#!/usr/bin/env python
# encoding: utf-8

"""Derived class to parse Moodle course items, it parses
   Moodle and therefor extends off of Parser
"""

from moodlefuse.moodle.parser import Parser
from moodlefuse.moodle import attributes


class CourseParser(Parser):

    def __init__(self):
        super(CourseParser, self).__init__()

    def parse_courses(self, html):
        if self._html_is_table_format(html):
            return self._parse_table_courses(html)
        else:
            return self._parse_flat_courses(html)

    def _html_is_table_format(self, course_html):
        return self.scraper.get_html_with_divclass(
            course_html, attributes.COURSES) is None

    def _parse_flat_courses(self, course_html):
        course_html = self.scraper.get_html_with_divclass(
            course_html, attributes.COURSES)

        courses = course_html.findAll(text=True)
        return self.remove_unicode(courses)

    def _parse_table_courses(self, course_html):
        course_table = self.scraper.get_html_with_divclass(
            course_html, attributes.MODULES)

        courses_html = self.scraper.get_html_items_with_tdclass(
            course_table, attributes.FIRST_CELL)

        courses = self.scraper.get_text_from_html_list(courses_html)
        return self.remove_unicode(courses)

    def get_last_sections_edit_button(self, course_html):
        last_section_html = self.get_sections_settings_html(course_html)[-1]
        return self.get_link_from_item(last_section_html)

    def get_sections_settings_html(self, course_html):
        return self.scraper.get_all_html_with_atitle(
            course_html, attributes.EDIT_SUMMARY)

    def parse_course_category_titles(self, course_content):
        sections = self.scraper.get_text_from_taged_item(course_content, 'h3')
        return self.remove_unicode(sections)

    def parse_course_content_from_page(self, html):
        course_html = self.scraper.get_html_with_divclass(
            html, attributes.COURSE_CONTENT)

        return course_html

    def get_add_section_link(self, course_content):
        add_section_html = self.scraper.get_html_with_aclass(
            course_content, attributes.INCREASE_SECTIONS)

        return self.get_link_from_item(add_section_html)

    def parse_course_category_from_course(self, course_content, category):
        category_html = self.scraper.get_html_with_liarialabel(
            course_content, category
        )

        return category_html

    def get_course_link(self, course_scraper, course):
        course_link = self.scraper.get_link_from_linktext_in_divclass(
            course_scraper, attributes.COURSES, course)

        return course_link

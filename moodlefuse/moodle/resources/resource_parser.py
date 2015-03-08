#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.parser import Parser


class ResourceParser(Parser):

    def __init__(self):
        super(ResourceParser, self).__init__()

    def parse_course_resources(self, course_content):
        categories_html = self.scraper.get_html_with_divclass(
            course_content, 'course-content')

        pass


#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.parser import Parser


class ResourceParser(Parser):

    def __init__(self):
        super(ResourceParser, self).__init__()

    def parse_course_resources(self, category_content):
        resources_html = self.scraper.get_html_items_with_spanclass(
            category_content, 'instancename')

        return self.scraper.get_instances_from_span_list_with_type(
            resources_html, 'File'
        )


#!/usr/bin/env python
# encoding: utf-8

"""Derived class to parse Moodle resource items, it parses
   Moodle and therefor extends off of Parser
"""

from moodlefuse.moodle.parser import Parser
from moodlefuse.moodle import attributes
from moodlefuse.moodle import resources


class ResourceParser(Parser):

    def __init__(self):
        super(ResourceParser, self).__init__()

    def parse_course_resources(self, category_content):
        resources_html = self._get_resource_html(category_content)
        return self.scraper.get_instances_from_span_list(resources_html)

    def parse_course_resource_url(self, category_content, filename):
        activity_instances = self.scraper.get_html_items_with_divclass(
            category_content, attributes.INSTANCE)

        return self.scraper.get_link_from_span_list_with_type_and_name(
            activity_instances, resources.FILE, filename
        )

    def parse_course_assignment_url(self, category_content, filename):
        activity_instances = self.scraper.get_html_items_with_divclass(
            category_content, attributes.INSTANCE)

        return self.scraper.get_link_from_span_list_with_type_and_name(
            activity_instances, resources.ASSIGNMENT, filename
        )

    def _get_resource_html(self, category_content):
        return self.scraper.get_html_items_with_spanclass(
            category_content, attributes.INSTANCE_NAME)

#!/usr/bin/env python
# encoding: utf-8

from tests import MoodleFuseAppTestCase


class ResourcesTestCase(MoodleFuseAppTestCase):

    def list_resources_test(self):
        files = list(
            self.ops.readdir(self.filesystem_root + '/', None))

        assert self.utils.lists_are_equal(files, [])


    def list_resources_invalid_courses_test(self):
        files = list(
            self.ops.readdir(self.filesystem_root + '/', None))

        assert self.utils.lists_are_not_equal(files, [])
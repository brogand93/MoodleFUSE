#!/usr/bin/env python
# encoding: utf-8

from tests.resources.data.resources_results import true_resources, false_resources
from tests import MoodleFuseAppTestCase


class ResourcesTestCase(MoodleFuseAppTestCase):

    def list_resources_test(self):
        files = list(
            self.ops.readdir(
                self.filesystem_root + '/testcourse/week_1', None))

        print files
        assert self.utils.lists_are_equal(files, true_resources)

    def list_resources_invalid_resources_test(self):
        files = list(
            self.ops.readdir(
                self.filesystem_root + '/testcourse/week_1', None))

        assert self.utils.lists_are_not_equal(files, false_resources)
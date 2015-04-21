#!/usr/bin/env python
# encoding: utf-8
from moodlefuse.moodle.resources.resource_errors import UnableToDownloadResource
from tests.resources.data.resources_results import true_resources, false_resources
from tests import MoodleFuseAppTestCase
from tests.data import settings
from fuse import FuseOSError

import os


class ResourcesTestCase(MoodleFuseAppTestCase):

    def list_resources_test(self):
        files = list(
            self.ops.readdir(
                self.filesystem_root + '/testcourse/week_1', None))

        assert self.utils.lists_are_equal(files, true_resources)

    def list_resources_invalid_resources_test(self):
        files = list(
            self.ops.readdir(
                self.filesystem_root + '/testcourse/week_1', None))

        assert self.utils.lists_are_not_equal(files, false_resources)

    def download_resource_test(self):
        self.ops.open(
            self.filesystem_root + '/testcourse/week_1/t', os.O_RDONLY)

        self.assertTrue(os.path.exists(settings.DOWNLOADS + '/testfile'))
        os.remove(settings.DOWNLOADS + '/testfile')

    def get_resource_attributes_test(self):
        attributes = self.ops.getattr(
            self.filesystem_root + '/testcourse/week_1/r'
        )

        self.assertTrue(
            (attributes.has_key(key)) for key in (
                'st_atime',
                'st_ctime',
                'st_gid',
                'st_mode',
                'st_mtime',
                'st_nlink',
                'st_size',
                'st_uid'
            )
        )

    def get_resource_attributes_invalid_resource_test(self):
        self.assertRaises(FuseOSError, lambda:
                self.ops.getattr(
                    self.filesystem_root + '/testcourse/week_1/invalidresource'
                )
        )
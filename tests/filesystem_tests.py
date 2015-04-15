#!/usr/bin/env python
# encoding: utf-8

from tests import MoodleFuseAppTestCase
from tests.data.settings import DOWNLOADS

import os


class FilesystemTestCase(MoodleFuseAppTestCase):

    def cache_created_test(self):
        self.assertTrue(os.path.exists(DOWNLOADS))

    def mount_created_test(self):
        self.assertTrue(os.path.exists(self.filesystem_root))
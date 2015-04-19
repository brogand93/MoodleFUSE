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

    def flush_test(self):
        self.ops.flush('', None)

    def fsync_test(self):
        self.ops.fsync('', None, None)

    def utimens_test(self):
        self.ops.utimens('')

    def unlink_test(self):
        self.ops.unlink('')

    def remdir_test(self):
        self.ops.rmdir('')

    def ops_test(self):
        self.ops.__call__('flush', '/', {})

    def stat_test(self):
        self.assertEquals(
            self.ops.statfs(''),
            dict(f_bsize=512, f_blocks=4096, f_bavail=2048)
        )

#!/usr/bin/env python
# encoding: utf-8

import os
import shutil

from tests.utils import TestUtils
from unittest import TestCase
from moodlefuse import MoodleFuse
from tests.data import settings
from moodlefuse.filesystem.file_operations import FileOperationOverrider


class MoodleFuseTestCase(TestCase):
    pass

class MoodleFuseAppTestCase(MoodleFuseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.filesystem_root = os.path.join(
            os.path.expanduser('~'),
            settings.LOCAL_MOODLE_FOLDER
        )
        if not os.path.exists(cls.filesystem_root):
            os.mkdir(cls.filesystem_root)

        if not os.path.exists(settings.DOWNLOADS):
            os.mkdir(settings.DOWNLOADS)

        cls.app = MoodleFuse(settings, True)
        cls.ops = FileOperationOverrider(cls.filesystem_root)

    @classmethod
    def tearDownClass(cls):
        cls.ops.end_operations()

        if os.path.exists(cls.filesystem_root):
            os.rmdir(cls.filesystem_root)

        if os.path.exists(settings.DOWNLOADS):
            shutil.rmtree(settings.DOWNLOADS)

    def setUp(self):
        self.utils = TestUtils()

    def tearDown(self):
        pass

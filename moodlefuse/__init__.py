#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.filesystem import Filesystem


class MoodleFuse(object):

    def __init__(self):
        self._create_filesystem_root()
        Filesystem(str(os.path.join(os.path.expanduser('~'), 'moodle')))

    def _create_filesystem_root(self):
        moodle_fs_path = os.path.join(os.path.expanduser('~'), 'moodle')
        print moodle_fs_path
        if os.path.ismount(moodle_fs_path):
            print 'dahkja dasdsa'

        if not os.path.exists(moodle_fs_path):
            os.makedirs(moodle_fs_path)

        os.chmod(moodle_fs_path, 0700)

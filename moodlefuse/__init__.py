#!/usr/bin/env python
# encoding: utf-8

import os
import errno

from moodlefuse.filesystem import Filesystem


class MoodleFuse(object):

    def __init__(self):
        self._create_filesystem_root()
        Filesystem(str(os.path.join(os.path.expanduser('~'), 'moodle')))

    def _create_filesystem_root(self):
        moodle_fs_path = os.path.join(os.path.expanduser('~'), 'moodle')
        try:
            os.makedirs(moodle_fs_path)
        except OSError, e:
            if e.errno is not errno.EEXIST:
                raise e

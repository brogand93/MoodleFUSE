#!/usr/bin/env python
# encoding: utf-8

import os


class Setup(object):

    def _create_filesystem_root(self):
        moodle_fs_path = os.path.join(os.path.expanduser('~'), 'moodle')
        if not os.path.exists(moodle_fs_path):
            os.makedirs(moodle_fs_path)
        os.chmod(moodle_fs_path, 0700)

#!/usr/bin/env python
# encoding: utf-8

"""MoodleFUSE initialization
"""

import os
import errno

from moodlefuse.filesystem import Filesystem
from moodlefuse.core import setup, config
from moodlefuse.services import USERS


MOODLEFUSE_DATABASE_FILE = 'moodlefuse.sqlite'
MOODLEFUSE_CONFIG_FILE = 'moodlefuse.conf'
MOODLEFUSE_HIDDEN_FOLDER = '.moodlefuse'
DATABASE_CONF = 'alembic.ini'
MOODLEFUSE_CACHE = 'cache'


class MoodleFuse(object):

    def __init__(self, settings=None, testing=None):
        setup(settings)
        self._create_filesystem_root()
        Filesystem(config['LOCAL_MOODLE_FOLDER'], testing)

    def _create_filesystem_root(self):
        moodle_fs_path = config['LOCAL_MOODLE_FOLDER']
        try:
            os.makedirs(moodle_fs_path)
        except OSError as e:
            if e.errno is not errno.EEXIST:
                raise e

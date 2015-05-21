#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.filesystem.files.file import File
from moodlefuse.core import config


class CacheFile(File):

    def __init__(self, cache_path=None):
        super(CacheFile, self).__init__()
        if cache_path is not None:
            self.path = cache_path
            self.set_attrs()

    def set_attrs(self):
        if os.path.isfile(self.path):
            st = os.lstat(self.path)
            self.attrs = dict(
                (key, getattr(st, key)) for key in (
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

    def create_file(self, location, content=None):
        if 'DOWNLOADS' in config:
            cache_path = config['DOWNLOADS'] + '/testfile'
        else:
            cache_path = get_cache_path_based_on_location(location)
        with open(cache_path, 'w') as cache_file:
            if content is not None:
                cache_file.write(content)
            cache_file.close()
            self.path = cache_path
            self.set_attrs()
            return cache_path

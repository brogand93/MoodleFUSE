#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.filesystem.files.file import File
from moodlefuse.core import config


class CacheFile(File):

    def __init__(self, cache_path):
        super(CacheFile, self).__init__()
        self.path = cache_path
        st = os.lstat(cache_path)

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

    @staticmethod
    def create_file(location, content=None):
        if 'DOWNLOADS' in config:
            cache_path = config['DOWNLOADS'] + '/testfile'
        else:
            cache_path = get_cache_path_based_on_location(location)
        with open(cache_path, 'w') as cache_file:
            if content is not None:
                cache_file.write(content)
            cache_file.close()
            return cache_path

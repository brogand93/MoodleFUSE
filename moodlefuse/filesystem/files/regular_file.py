#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.filesystem.files.file import File


class RegularFile(File):

    def __init__(self, name, url, **kwargs):
        super(RegularFile, self).__init__(name, url, **kwargs)
        self.filepath = self.build_cache_filepath()

    def build_cache_filepath(self):
        return '~/.moodlefuse/cache/test'

    def create_cache_file(self):
        open(self.filepath, 'w+').close()

    def read(self, size, offset):
        if not os.path.exists(self.filepath):
            self.create_cache_file()

        with open(self.filepath, 'rb+') as f:
            f.seek(offset, 0)
            return f.read(size)

    def write(self, data, offset):
        with open(self.filepath, 'rb+') as f:
            f.seek(offset, 0)
            f.write(data)

        self.attrs['st_size'] += len(data)

    def truncate(self, length):
        with open(self.filepath, 'rb+') as f:
            f.truncate(length)

        self.attrs['st_size'] = length

    def rename(self, new_filepath):
        pass

    def sync(self):
        pass

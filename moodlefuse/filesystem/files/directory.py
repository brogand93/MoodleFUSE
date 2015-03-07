#!/usr/bin/env python
# encoding: utf-8

from stat import S_IFDIR, S_IREAD
from moodlefuse.filesystem.files.file import File


class Directory(File):

    def __init__(self, api, name, url, **kwargs):
        super(Directory, self).__init__(api, name, url, **kwargs)

        self.files = {}

        self.attrs['st_mode'] = (S_IFDIR | S_IREAD)

    def load_files(self):
        pass

    def create_file(self, name, mode):
        pass

    def get_files(self):
        return self.files

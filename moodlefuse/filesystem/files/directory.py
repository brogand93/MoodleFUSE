#!/usr/bin/env python
# encoding: utf-8

from stat import S_IFDIR, S_IREAD, S_IWRITE
from moodlefuse.filesystem.files.file import File
from fuse import fuse_get_context


class Directory(File):

    def __init__(self):
        super(Directory, self).__init__()
        uid, gid, _ = fuse_get_context()
        self.attrs['st_mode'] = (S_IFDIR | S_IREAD | S_IWRITE)
        self.attrs['st_size'] = 4096

    def get_aattrs(self):
        return self.attrs

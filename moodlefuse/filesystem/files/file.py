#!/usr/bin/env python
# encoding: utf-8

from stat import S_IFREG
from fuse import fuse_get_context
from time import time


class File(object):

    def __init__(self):
        uid, gid, _ = fuse_get_context()
        self.attrs = {
            'st_mode': (S_IFREG | 0o755),
            'st_mtime': time(),
            'st_atime': time(),
            'st_nlink': 0,
            'st_uid': uid,
            'st_gid': gid,
            'st_size': 0
        }

    def get_attrs(self):
        return self.attrs

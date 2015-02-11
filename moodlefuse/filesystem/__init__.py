#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.filesystem.file_operations import FileOperationOverrider
from fuse import FUSE


class Filesystem(object):

    def __init__(self, mount):
        FUSE(FileOperationOverrider(mount), mount, foreground=True)

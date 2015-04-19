#!/usr/bin/env python
# encoding: utf-8

"""MoodleFUSE filesystem initialization
"""

from fuse import FUSE

from moodlefuse.filesystem.file_operations import FileOperationOverrider


class Filesystem(object):

    def __init__(self, mount, testing=False):
        if not testing:
            FUSE(FileOperationOverrider(mount), mount, foreground=True)

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.filesystem.file_operations import FileOperationOverrider
from fuse import FUSE
from sh import umount


class Filesystem(object):

    def __init__(self, mount):
        print 'sadsadasd'
        FUSE(FileOperationOverrider, mount)
        print 'sadsadasd2'
        umount(mount)
        print 'sadsadasd3'

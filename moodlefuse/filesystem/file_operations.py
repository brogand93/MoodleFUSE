#!/usr/bin/env python
# encoding: utf-8

"""Filesystem operations classs, overrides FUSE operations
"""

import errno
import os

from fuse import FuseOSError, Operations

from moodlefuse.filesystem.file_system_translator import FileSystemTranslator


class FileOperationOverrider(Operations):

    def __init__(self, root):
        self.root = os.path.realpath(root)
        self.translator = FileSystemTranslator()

    def end_operations(self):
        self.translator.close_browsers()

    def __call__(self, op, path, *args):
        return super(FileOperationOverrider, self).__call__(
            op, self.root + path, *args
        )

    def access(self, path, mode):
        if not self.translator.path_exists_in_moodle(path):
            raise FuseOSError(errno.EACCES)

    def create(self, path, mode, fi=None):
        cache_path = self.translator.create_file(path)
        if cache_path is not None:
            return os.open(cache_path, os.O_WRONLY)
        else:
            return 1

    def flush(self, path, fh):
        pass

    def fsync(self, path, fdatasync, fh):
        pass

    def getattr(self, path, fh=None):
        if not self.translator.path_exists_in_moodle(path):
            raise FuseOSError(errno.ENOENT)
        else:
            return self.translator.get_file_attributes(path)

    def mkdir(self, path, mode):
        self.translator.make_directory(path)

    def open(self, path, flags):
        cache_path = self.translator.open_file(path)
        if cache_path is not None:
            return os.open(cache_path, flags)
        else:
            return 1

    def read(self, path, length, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def readdir(self, path, fh):
        dirents = self.translator.get_directory_contents_based_on_path(path)
        for r in dirents:
            yield r

    def release(self, path, fh):
        return os.close(fh)

    def rename(self, old, new):
        self.translator.rename_file(old, new)

    def rmdir(self, path):
        pass

    def statfs(self, path):
        return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)

    def truncate(self, path, length, fh=None):
        cache_path = self.translator.open_file(path)
        with open(cache_path, 'r+') as cache_file:
            cache_file.truncate(length)

    def unlink(self, path):
        self.translator.remove_resource(path)

    def utimens(self, path, times=None):
        pass

    def write(self, path, buf, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        response = os.write(fh, buf)
        self.translator.modify_file(path)
        return response

    link = None

    chmod = None

    chown = None

    mknod = None

    readlink = None

    symlink = None

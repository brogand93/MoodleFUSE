#!/usr/bin/env python
# encoding: utf-8

import os
import errno

from moodlefuse.filesystem.file_system_translator import FileSystemTranslator
from fuse import FuseOSError, Operations


class FileOperationOverrider(Operations):

    def __init__(self, root):
        self.root = os.path.realpath(root)

    def __call__(self, op, path, *args):
        return super(FileOperationOverrider, self).__call__(
            op, self.root + path, *args
        )

    def access(self, path, mode):
        if not FileSystemTranslator.path_exists_in_moodle(path):
            raise FuseOSError(errno.EACCES)

    def create(self, path, mode, fi=None):
        print 'create'
        return os.open(path, os.O_WRONLY | os.O_CREAT, mode)

    def flush(self, path, fh):
        print 'flush'
        return os.fsync(fh)

    def fsync(self, path, fdatasync, fh):
        print 'fsync'
        return self.flush(path, fh)

    def getattr(self, path, fh=None):
        return FileSystemTranslator.get_file_attributes(path)

    def mknod(self, path, mode, dev):
        print 'mknod'
        return os.mknod(path, mode, dev)

    def mkdir(self, path, mode):
        print 'mkdir'
        return os.mkdir(path, mode)

    def open(self, path, flags):
        cache_path = FileSystemTranslator.open_file(path)
        if cache_path is not None:
            return os.open(cache_path, flags)
        else:
            return 1

    def read(self, path, length, offset, fh):
        print 'read'
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def readdir(self, path, fh):
        dirents = FileSystemTranslator.get_directory_contents_based_on_path(path)
        for r in dirents:
            yield r

    def readlink(self, path):
        print 'readlink'
        pathname = os.readlink(path)
        return pathname

    def release(self, path, fh):
        print 'release'
        return os.close(fh)

    def rename(self, old, new):
        print 'rename'
        return os.rename(old, new)

    def rmdir(self, path):
        print 'rmdir'
        return os.rmdir(path)

    def statfs(self, path):
        print 'statfs'
        stv = os.statvfs(path)
        return dict(
            (key, getattr(stv, key)) for key in (
                'f_bavail', 'f_bfree',
                'f_blocks', 'f_bsize',
                'f_favail', 'f_ffree',
                'f_files', 'f_flag',
                'f_frsize', 'f_namemax'
            )
        )

    def symlink(self, name, target):
        print 'symlink'
        return os.symlink(name, target)

    def unlink(self, path):
        print 'unlink'
        return os.unlink(path)

    def utimens(self, path, times=None):
        print 'utimens'
        return os.utime(path, times)

    def write(self, path, buf, offset, fh):
        print 'write'
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    link = None

    chmod = None

    chown = None

    truncate = None

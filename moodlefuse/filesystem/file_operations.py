#!/usr/bin/env python
# encoding: utf-8

import os
import errno


from fuse import FuseOSError, Operations


class FileOperationOverrider(Operations):

    def __init__(self, root):
        self.root = os.path.realpath(root)

    def __call__(self, op, path, *args):
        return super(FileOperationOverrider, self).__call__(
            op, self.root + path, *args
        )

    def access(self, path, mode):
        print 'access'
        if not os.access(path, mode):
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        print 'chmod'
        return os.chmod(path, mode)

    def chown(self, path, uid, gid):
        print 'chown'
        return os.chown(path, uid, gid)

    def getattr(self, path, fh=None):
        print 'getattr'
        st = os.lstat(path)
        return dict(
            (key, getattr(st, key)) for key in (
                'st_atime', 'st_ctime',
                'st_gid', 'st_mode',
                'st_mtime', 'st_nlink',
                'st_size', 'st_uid'
            )
        )

    def readdir(self, path, fh):
        print 'readdir'
        dirents = ['.', '..']
        if os.path.isdir(path):
            dirents.extend(os.listdir(path))
        for r in dirents:
            yield r

    def readlink(self, path):
        print 'readlink'
        pathname = os.readlink(path)
        return pathname

    def mknod(self, path, mode, dev):
        print 'mknod'
        return os.mknod(path, mode, dev)

    def rmdir(self, path):
        print 'rmdir'
        return os.rmdir(path)

    def mkdir(self, path, mode):
        print 'mkdir'
        return os.mkdir(path, mode)

    def statfs(self, path):
        print 'statfs'
        stv = os.statvfs(path)
        return dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
            'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files', 'f_flag',
            'f_frsize', 'f_namemax'))

    def unlink(self, path):
        print 'unlink'
        return os.unlink(path)

    def symlink(self, name, target):
        print 'symlink'
        return os.symlink(name, target)

    def rename(self, old, new):
        print 'rename'
        return os.rename(old, new)

    def link(self, target, name):
        print 'link'
        return os.link(target, name)

    def utimens(self, path, times=None):
        print 'utimens'
        return os.utime(path, times)

    # File methods
    # ============

    def open(self, path, flags):
        print 'open'
        return os.open(path, flags)

    def create(self, path, mode, fi=None):
        print 'create'
        return os.open(path, os.O_WRONLY | os.O_CREAT, mode)

    def read(self, path, length, offset, fh):
        print 'read'
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        print 'write'
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    def truncate(self, path, length, fh=None):
        print 'truncate'
        with open(path, 'r+') as f:
            f.truncate(length)

    def flush(self, path, fh):
        print 'flush'
        return os.fsync(fh)

    def release(self, path, fh):
        print 'release'
        return os.close(fh)

    def fsync(self, path, fdatasync, fh):
        print 'fsync'
        return self.flush(path, fh)

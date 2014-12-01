#!/usr/bin/env python
# encoding: utf-8

from functools import wraps


def requires_user_information(fn):
    @wraps(fn)
    def decorated(*args):
        args['token'] = 'dummy token'
        return fn(*args)

    return decorated

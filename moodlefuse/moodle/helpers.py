#!/usr/bin/env python
# encoding: utf-8

from functools import wraps


def requires_user_token(fn):
    @wraps(fn)
    def decorated(*args):
        args['token'] = 'c48133e52b502740fbce84eecf7e3110'
        return fn(args)

    return decorated

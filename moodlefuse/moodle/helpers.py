#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.core import config
from functools import wraps


def requires_user_token(fn):
    @wraps(fn)
    def decorated(*args):
        args['token'] = config['MOODLE_TOKEN']
        return fn(args)

    return decorated

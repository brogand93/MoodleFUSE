#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.helpers import requires_user_information


class MoodleRequester(object):

    @staticmethod
    @requires_user_information
    def make_request(args):
        pass

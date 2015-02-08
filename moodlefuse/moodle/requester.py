#!/usr/bin/env python
# encoding: utf-8

import requests

from urllib import urlencode
from moodlefuse.moodle.helpers import requires_user_token


class Requester(object):

    @requires_user_token
    def rest_request(self, args):
        destination = 'webservice/rest/server.php'
        url = self._create_moodle_request_url(destination, args)
        response = requests.get(url)

        return response

    @requires_user_token
    def upload_request(self, args):
        destination = 'webservice/upload.php'
        url = self._create_moodle_request_url(destination, args)
        response = requests.get(url)

        return response

    @requires_user_token
    def download_request(self, args):
        destination = 'webservice/pluginfile.php'
        url = self._create_moodle_request_url(destination, args)
        response = requests.get(url)

        return response

    def _generate_args_url(self, args):
        keys = sorted(args.keys())
        values = sorted(map(args.get, keys))

        return urlencode(
            list(
                zip(keys, values)
            )
        )

    def _create_moodle_request_url(self, destination, args):
        args_url = self._generate_args_url(args)

        request_url = '%s/%s?%s' % (
            'http://www.moodle.dcu.ie',
            destination,
            args_url
        )

        return request_url

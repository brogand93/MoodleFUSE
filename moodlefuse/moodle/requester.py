#!/usr/bin/env python
# encoding: utf-8

import json
import requests

from urllib import urlencode, urlretrieve


class Requester(object):

    def rest_request(self, args):
        destination = 'webservice/rest/server.php'
        url = self._create_moodle_request_url(destination, args)
        response = requests.get(url)
        response_data = json.loads(response.text)

        return response_data

    def upload_request(self, args):
        destination = 'webservice/upload.php'
        url = self._create_moodle_request_url(destination, args)
        response = requests.get(url)

        return response

    def download_request(self, args, location):
        destination = 'webservice/pluginfile.php'
        url = self._create_moodle_request_url(destination, args)
        cache_path = '/home/brogand/.moodlefuse/cache/' + location[0] + '_' + location[1] + '_' + location[2]
        urlretrieve(url, cache_path)
        return cache_path

    def _generate_args_url(self, args):
        keys = sorted(args.keys())
        values = map(args.get, keys)

        return urlencode(
            list(
                zip(keys, values)
            )
        )

    def _create_moodle_request_url(self, destination, args):
        args_url = self._generate_args_url(args)

        request_url = '%s/%s?%s' % (
            'http://192.168.56.103/moodle',
            destination,
            args_url
        )

        return request_url

#!/usr/bin/env python
# encoding: utf-8

import json
import requests

from moodlefuse.helpers import get_cache_path_based_on_location
from urllib import urlencode, urlretrieve
from moodlefuse.core import config


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

    def download_request(self, args, source, location):
        if source != None:
            url = self._create_moodle_download_url(source, args)
            cache_path = get_cache_path_based_on_location(location)

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

    def _create_moodle_download_url(self, path, args):
        args_url = self._generate_args_url(args)

        request_url = '%s?&%s' % (
            path,
            args_url
        )

        return request_url

    def _create_moodle_request_url(self, destination, args):
        args_url = self._generate_args_url(args)

        request_url = '%s/%s?%s' % (
            config['MOODLE_WEB_ADDRESS'],
            destination,
            args_url
        )

        return request_url

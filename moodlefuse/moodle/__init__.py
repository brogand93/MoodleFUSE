#!/usr/bin/env python
# encoding: utf-8

import requests

class Moodle():

    @staticmethod
    def rest_request():

        url = Moodle._create_request_url('dummytoken', 'function')
        response = requests.get(url)

        return response

    @staticmethod
    def _create_request_url(token, function):

        token_payload = 'wstoken=%s' % (token)
        function_payload = 'wsfunction=%s' % function

        request_url = '%s/webservice/%s/server.php?%s&%s' % (
            'http://www.moodle.dcu.ie',
            'rest',
            token_payload,
            function_payload
        )

        return request_url


class MoodleException(BaseException):

    def __init__(self):
        self.message = "Unable to complete Moodle action"

    def __str__(self):
        return self.message

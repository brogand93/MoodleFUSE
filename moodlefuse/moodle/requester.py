#!/usr/bin/env python
# encoding: utf-8

import requests

class Requester(object):

    def rest_request(self):

        url = self._create_rest_request_url('dummytoken', 'dummyfunction')
        response = requests.get(url)

        return response

    def upload_request(self):

        url = self._create_file_upload_request_url('dummytoken', '~/testfile.txt', '/')
        response = requests.get(url)

        return response

    def download_request(self):

        url = self._create_file_download_request_url('dummytoken', '~/testfile.txt')
        response = requests.get(url)

        return response

    def _create_rest_request_url(self, token, function):

        token_payload = 'wstoken=%s' % (token)
        function_payload = 'wsfunction=%s' % (function)

        request_url = '%s/webservice/%s/server.php?%s&%s' % (
            'http://www.moodle.dcu.ie',
            'rest',
            token_payload,
            function_payload
        )

        return request_url


    def _create_file_upload_request_url(self, token, file_to_upload, file_destination):

        token_payload = 'token=%s' % (token)
        file_source_payload = 'file_box=%s' % (file_to_upload)
        file_destination_payload = 'filepath=%s' % (file_destination)


        request_url = '%s/webservice/upload.php?%s&%s&%s' % (
            'http://www.moodle.dcu.ie',
            token_payload,
            file_source_payload,
            file_destination_payload
        )

        return request_url


    def _create_file_download_request_url(self, token, file_to_download):

        token_payload = 'token=%s' % (token)

        request_url = '%s/webservice/pluginfile.php?%s%s' % (
            'http://www.moodle.dcu.ie',
            token_payload,
            file_to_download
        )

        return request_url

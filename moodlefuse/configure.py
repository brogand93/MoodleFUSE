#!/usr/bin/env python
# encoding: utf-8

import os
import argparse

from ConfigParser import SafeConfigParser


def main():
    Configurer()


class Configurer(object):

    def __init__(self):
        config_folder = self._create_config_folder()
        self._create_config_file(config_folder)
        self._create_filesystem_folder()
        self._create_file_cache()

    def _create_config_folder(self):
        config_folder = os.path.join(os.path.expanduser('~'), '.moodlefuse')
        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        os.chmod(config_folder, 0700)
        return config_folder

    def _create_file_cache(self):
        config_folder = os.path.join(os.path.expanduser('~'), '.moodlefuse/cache')
        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        os.chmod(config_folder, 0700)
        return config_folder

    def _create_config_file(self, config_folder):
        args = self._generate_args()
        profile = args.pop('profile')
        config_file_path = config_folder + '/moodlefuse.conf'
        config = self._modify_config_profile(config_file_path, profile)
        config_file = open(config_file_path, 'w+')
        config.write(config_file)

    def _generate_args(self):
        parser = argparse.ArgumentParser(
            'Command line utility for configuring moodlefuse'
        )

        parser.add_argument(
            '-p',
            '--profile',
            required=False,
            help='The profile to configure, default is initial',
            default='initial'
        )

        args = parser.parse_args()

        return vars(args)

    def _modify_config_profile(self, config_file, profile):
        config = SafeConfigParser()
        config.read(config_file)

        if not config.has_section(profile):
            config.add_section(profile)

        config = self._set_attributes_of_profile(config, profile)

        return config

    def _set_attributes_of_profile(self, config, profile):
        config = self._set_attribute_of_profile(
            config, profile, 'moodle_web_address', 'Moodle server address', 'hhtp://www.moodle.dcu.ie'
        )
        config = self._set_attribute_of_profile(
            config, profile, 'local_moodle_folder', 'Local Moodle folder', '~/moodle'
        )

        while True:
            config = self._set_attribute_of_profile(
                config, profile, 'moodle_token', 'Moodle REST user token', ''
            )
            if config.get(profile, 'moodle_token') is not '':
                break

        return config

    def _set_attribute_of_profile(self, config, profile, attribute, message, default):
        if config.has_option(profile, attribute):
            default = config.get(profile, attribute)

        attribute_value = self._read_in_config_attribute_or_use_default(message, default)

        config.set(profile, attribute, attribute_value)
        return config

    def _read_in_config_attribute_or_use_default(self, message, default):
        attribute = raw_input(message + ' [' + default + ']: ')
        if attribute == '':
            attribute = default

        return attribute

    def _create_filesystem_folder(self):
        config_folder = os.path.join(os.path.expanduser('~'), 'moodle')
        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        os.chmod(config_folder, 0700)
        return config_folder

#!/usr/bin/env python
# encoding: utf-8

import os
import argparse

from ConfigParser import SafeConfigParser


def main():
    config_folder = _create_config_folder()
    _create_config_file(config_folder)


def _create_config_folder():
    config_folder = os.path.join(os.path.expanduser('~'), '.moodlefuse')
    if not os.path.exists(config_folder):
        os.makedirs(config_folder)
    os.chmod(config_folder, 0700)
    return config_folder


def _create_config_file(config_folder):
    args = _generate_args()
    profile = args.pop('profile')
    config_file_path = config_folder + '/moodlefuse.conf'
    config = _modify_config_profile(config_file_path, profile)
    config_file = open(config_file_path, 'w+')
    config.write(config_file)


def _generate_args():
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


def _modify_config_profile(config_file, profile):
    config = SafeConfigParser()
    config.read(config_file)

    if not config.has_section(profile):
        config.add_section(profile)

    config = _set_attributes_of_profile(config, profile)

    return config


def _set_attributes_of_profile(config, profile):
    config = _set_attribute_of_profile(
        config, profile, 'moodle_web_address', 'Moodle server address', 'moodle.dcu.ie'
    )
    config = _set_attribute_of_profile(
        config, profile, 'local_moodle_folder', 'Local Moodle folder', '~/moodle'
    )
    while True:
        config = _set_attribute_of_profile(
            config, profile, 'moodle_token', 'Moodle REST user token', ''
        )
        if config.get(profile, 'moodle_token') is not '':
            break

    return config


def _set_attribute_of_profile(config, profile, attribute, message, default):
    if config.has_option(profile, attribute):
        default = config.get(profile, attribute)

    attribute_value = _read_in_config_attribute_or_use_default(message, default)

    config.set(profile, attribute, attribute_value)
    return config


def _read_in_config_attribute_or_use_default(message, default):
    attribute = raw_input(message + ' [' + default + ']: ')
    if attribute == '':
        attribute = default

    return attribute

#!/usr/bin/env python
# encoding: utf-8

"""Class to setup MoodleFUSE
"""

import os
import sys
import argparse

from ConfigParser import SafeConfigParser
from moodlefuse.model_manager import setup_model

config = {}


def setup(settings=None):
    if settings is not None:
        from_object(settings)
    else:
        args = _generate_args()
        profile = args.pop('profile')
        config['DEBUG'] = args.pop('debug')
        config_file = _load_config_file()
        _config_from_config_profile(config_file, profile)
        load_database()


def load_database():
    database_file = os.path.join(
        os.path.expanduser('~'),
        '.moodlefuse/moodlefuse.sqlite'
    )
    setup_model('sqlite:///' + database_file)


def from_object(obj):
    for key in dir(obj):
        if key.isupper():
            config[key] = getattr(obj, key)


def _generate_args():
    """
    Generate command line arguments for moodlefuse.
    @return: args.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p',
        '--profile',
        required=False,
        help='The profile to run moodlefuse with, default is initial',
        default='initial'
    )

    parser.add_argument(
        '-d',
        '--debug',
        required=False,
        help='Turn debug on for application',
        default=False
    )

    args = parser.parse_args()

    return vars(args)


def _load_config_file():
    """
    Checks that the user's configuration file exists and returns its path.
    @return: The path to the user's configuration file.
    """
    config_file = os.path.join(
        os.path.expanduser('~'),
        '.moodlefuse/moodlefuse.conf'
    )

    if not os.path.exists(config_file):
        sys.exit('No configuration found, please run moodlefuse-configure')

    return config_file


def _config_from_config_profile(config_file, profile):
    """
    Configures moodlefuse app based on configuration profile.
    @param config_file: current config file configuration.
    @param profile: the profile to set the attribute in.
    """
    configuration = SafeConfigParser()
    configuration.read(config_file)

    if not configuration.has_section(profile):
        sys.exit(
            'No profile matching ' +
            profile +
            ' found in configuration, please run moodlefuse-configure -p ' +
            profile)

    for attribute in configuration.options(profile):
        if attribute == 'local_moodle_folder':
            config[attribute.upper()] = str(
                os.path.join(
                    os.path.expanduser('~'),
                    configuration.get(
                        profile,
                        attribute
                    )
                ))
        else:
            config[attribute.upper()] = configuration.get(profile, attribute)

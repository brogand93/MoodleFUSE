#!/usr/bin/env python
# encoding: utf-8

import os


def get_cache_path_based_on_location(location):
    config_folder = os.path.join(os.path.expanduser('~'), '.moodlefuse')
    cache_base = os.path.join(config_folder, 'cache')
    return cache_base + '/' +  "_".join(location)

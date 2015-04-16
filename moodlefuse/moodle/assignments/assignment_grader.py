#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.core import config
import csv


class AssignmentGrader(object):

    def __init__(self):
        pass

    def format_csv(self, location):
        if 'DOWNLOADS' in config:
            csv_path = config['DOWNLOADS'] + '/grades.csv'
        else:
            csv_path = get_cache_path_based_on_location(location)
        with open(csv_path, 'wt') as f:
            writer = csv.writer(f)
            writer.writerow(('Name', 'Email Address', 'Grade'))
            f.close()
        return csv_path

    def add_user_names_and_emails(self, csv_path, assignment_content):
        with open(csv_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(('test', 'test@test'))
            writer.writerow(('test1', 'test1@test1'))
            f.close()

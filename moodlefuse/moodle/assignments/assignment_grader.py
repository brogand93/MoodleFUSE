#!/usr/bin/env python
# encoding: utf-8

"""Class to handle assignment grading for lecturers.
"""

import csv

from moodlefuse.moodle.assignments import GRADES_FILENAME
from moodlefuse.helpers import get_cache_path_based_on_location
from moodlefuse.core import config


class AssignmentGrader(object):

    def __init__(self):
        pass

    def _get_csv_path(self, location):
        if 'DOWNLOADS' in config:
            return config['DOWNLOADS'] + '/' + GRADES_FILENAME
        else:
            return get_cache_path_based_on_location(location)

    def left_format_entry(self, entry, number):
        return str(entry.ljust(number))

    def add_row(self, writer, left, middle, right):
        writer.writerow(
            (
                self.left_format_entry(left, 25),
                self.left_format_entry(middle, 35),
                self.left_format_entry(right, 10)
            )
        )

    def format_csv(self, location):
        csv_path = self._get_csv_path(location)
        with open(csv_path, 'wt') as f:
            writer = csv.writer(f)
            self.add_row(writer, 'Name', 'Email', 'Grade')
            f.close()

        return csv_path

    def read_csv_grades(self, location):
        grades = []
        csv_path = self._get_csv_path(location)
        with open(csv_path, 'rt') as f:
            reader = csv.reader(f)
            for row in list(reader)[1:]:
                grades.append([element.strip() for element in row])

        return grades

    def get_modified(self, location, old_grades):
        new = self.read_csv_grades(location)
        old = zip(old_grades[0], old_grades[1], old_grades[2])
        print old
        print new

    def add_user_information(self, csv_path, grading_info):
        with open(csv_path, 'a') as f:
            writer = csv.writer(f)
            self.add_user_rows(writer, grading_info)
            f.close()

        return csv_path

    def add_user_rows(self, writer, user_grading_info):
        for name, email, grade in \
                zip(user_grading_info[0], user_grading_info[1], user_grading_info[2]):
            self.add_user_row(writer, name, email, grade)

    def add_user_row(self, writer, name, email, grade):
        self.add_row(writer, name, email, grade)


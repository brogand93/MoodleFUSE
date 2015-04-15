#!/usr/bin/env python
# encoding: utf-8

"""Class to handle assignment Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.assignments.assignment_grader import AssignmentGrader
from moodlefuse.moodle.assignments.assignment_parser import AssignmentParser
from moodlefuse.moodle.handler import MoodleHandler


class AssignmentHandler(MoodleHandler):

    def __init__(self, emulator, js_emulator):
        super(self.__class__, self).__init__(emulator, js_emulator)
        self.grader = AssignmentGrader()
        self.parser = AssignmentParser()

    def get_assignment_info_as_array(self):
        return ['Submissions', 'grades.csv']

    def get_assignment_submissions(self, assignment_url):
        if 'grading' not in assignment_url:
            assignment_url = assignment_url + "&action=grading"
        self.moodle.follow_link(assignment_url)
        assignment_submissions = self.moodle.filter_assignment_submissions()
        return self.parser.get_all_assignment_names(assignment_submissions)

    def fill_grades_file_with_template(self, location):
        csv = self.grader.format_csv(location)
        self.grader.add_user_names_and_emails(csv, None)
        return csv

    def get_grades_csv(self, location):
        return self.fill_grades_file_with_template(location)

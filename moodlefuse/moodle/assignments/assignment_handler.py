#!/usr/bin/env python
# encoding: utf-8

"""Class to handle assignment Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.assignments.assignment_grader import AssignmentGrader
from moodlefuse.moodle.assignments.assignment_parser import AssignmentParser
from moodlefuse.moodle.handler import MoodleHandler
from moodlefuse.moodle import assignments


class AssignmentHandler(MoodleHandler):

    def __init__(self, emulator, js_emulator):
        super(self.__class__, self).__init__(emulator, js_emulator)
        self.grader = AssignmentGrader()
        self.parser = AssignmentParser()

    def get_assignment_info_as_array(self):
        return [assignments.SUBMISSIONS_FILENAME, assignments.GRADES_FILENAME]

    def get_grading_url(self, assignment_url):
        if 'grading' not in assignment_url:
            assignment_url = assignment_url + assignments.GRADING_URL_EXTENSION

        return assignment_url

    def get_assignment_content(self, assignment_url):
        assignment_url = self.get_grading_url(assignment_url)
        return self.moodle.follow_link(assignment_url)

    def get_assignment_submissions(self, assignment_url):
        self.get_assignment_content(assignment_url)
        assignment_submissions = self.moodle.filter_assignment_submissions()
        return self.parser.get_all_submission_names(assignment_submissions)

    def populate_grading_form(self, location, grading_info):
        csv = self.grader.format_csv(location)
        csv = self.grader.add_user_information(csv, grading_info)
        return csv

    def get_grade_info_from_url(self, assignment_url):
        self.get_assignment_content(assignment_url)
        assignment_submissions = self.moodle.unfilter_assignment_submissions()
        return self.get_grading_info(assignment_submissions)

    def get_grading_info(self, assignment_submissions):
        names = self.parser.get_all_student_names(assignment_submissions)
        emails = self.parser.get_all_student_emails(assignment_submissions)
        grades = self.parser.get_all_student_grades(assignment_submissions)
        return (names, emails, grades)

    def modify_grades(self, location, assignment_url):
        old_grading_info = self.get_grade_info_from_url(assignment_url)
        grades = self.grader.get_modified(location, old_grading_info)
        self.moodle.follow_link_with_js(self.get_grading_url(assignment_url))
        self.moodle.modify_assignment_grades(grades)

    def get_grades_csv(self, location, assignment_url):
        grading_info = self.get_grade_info_from_url(assignment_url)
        return self.populate_grading_form(location, grading_info)

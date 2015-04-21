from tests import MoodleFuseAppTestCase
from tests.assignments.data.assignments_results import \
    true_assignment_submissions, grades_header, \
    true_assignment_info, false_assignment_submissions
from fuse import FuseOSError
from data.settings import DOWNLOADS

import os
import csv

class AssignmentsTestCase(MoodleFuseAppTestCase):

    def list_assignment_info_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse/e/test', None))

        assert self.utils.lists_are_equal(files, true_assignment_info)

    def list_assignment_info__invalid_info_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse/e/test', None))

        assert self.utils.lists_are_not_equal(files, false_assignment_submissions)


    def list_assignment_submissions_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse/e/test/Submissions', None))

        assert self.utils.lists_are_equal(files, true_assignment_submissions)

    def list_assignment_submissions_invalid_submissions_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse/e/test/submissions', None))

        assert self.utils.lists_are_not_equal(files, false_assignment_submissions)

    def enter_assignment_invalid_assignment_test(self):
        self.assertRaises(FuseOSError, lambda:
                self.ops.access(
                    self.filesystem_root + '/testcourse/e/invalidassignment', None
                )
        )

    def open_assignment_grading_form_test(self):
        status = self.ops.open(
            self.filesystem_root + '/testcourse/e/test/grades.csv', os.O_RDONLY)

        self.assertTrue(status > 1)

    def assignment_grades_form_cached_test(self):
        self.ops.open(
            self.filesystem_root + '/testcourse/e/test/grades.csv', os.O_RDONLY)

        self.assertTrue(os.path.exists(
                os.path.join(DOWNLOADS, 'grades.csv')
            )
        )

    def assignment_grading_formatted_test(self):
        self.ops.open(
            self.filesystem_root + '/testcourse/e/test/grades.csv', os.O_RDONLY)

        csv_file = os.path.join(DOWNLOADS, 'grades.csv')
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            self.assertTrue(
                self.utils.lists_are_equal(
                    list(reader)[0], grades_header
                )
            )

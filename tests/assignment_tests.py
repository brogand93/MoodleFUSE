from tests import MoodleFuseAppTestCase
from tests.assignments.data.assignments_results import \
    true_assignment_submissions, false_assignment_submissions, \
    true_assignment_info, false_assignment_submissions
from fuse import FuseOSError


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
                    self.filesystem_root + '/testcourse/week_1/e/invalidassignment', None
                )
        )
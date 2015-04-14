from tests import MoodleFuseAppTestCase
from tests.assignments.data.assignments_results import \
    true_assignment_submissions, false_assignment_submissions


class AssignmentsTestCase(MoodleFuseAppTestCase):

    def list_assignment_submissions_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse/e/test/submissions', None))

        print files
        assert self.utils.lists_are_equal(files, true_assignment_submissions)

    def list_assignment_submissions_invalid_submissions_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse/e/test/submissions', None))

        assert self.utils.lists_are_not_equal(files, false_assignment_submissions)
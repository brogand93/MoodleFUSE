from tests.courses.data.course_results import true_courses, false_courses
from tests import MoodleFuseAppTestCase


class CoursesTestCase(MoodleFuseAppTestCase):

    def list_courses_test(self):
        files = list(
            self.ops.readdir(self.filesystem_root + '/', None))

        assert self.utils.lists_are_equal(files, true_courses)


    def list_courses_invalid_courses_test(self):
        files = list(
            self.ops.readdir(self.filesystem_root + '/', None))

        assert self.utils.lists_are_not_equal(files, false_courses)
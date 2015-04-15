from tests.courses.data.course_results import true_courses, false_courses
from tests import MoodleFuseAppTestCase
from fuse import FuseOSError


class CoursesTestCase(MoodleFuseAppTestCase):

    def list_courses_test(self):
        files = list(
            self.ops.readdir(self.filesystem_root + '/', None))

        assert self.utils.lists_are_equal(files, true_courses)


    def list_courses_invalid_courses_test(self):
        files = list(
            self.ops.readdir(self.filesystem_root + '/', None))

        assert self.utils.lists_are_not_equal(files, false_courses)

    def enter_course_invalid_course_test(self):
        self.assertRaises(FuseOSError, lambda:
                self.ops.access(
                    self.filesystem_root + '/invalidcourse', None
                )
        )

    def get_coursee_attributes_test(self):
        attributes = self.ops.getattr(
            self.filesystem_root + '/testcourse'
        )

        self.assertTrue(
            (attributes.has_key(key)) for key in (
                'st_atime',
                'st_ctime',
                'st_gid',
                'st_mode',
                'st_mtime',
                'st_nlink',
                'st_size',
                'st_uid'
            )
        )

    def get_course_attributes_invalid_course_test(self):
        self.assertRaises(FuseOSError, lambda:
                self.ops.getattr(
                    self.filesystem_root + '/invalidcourse'
                )
        )


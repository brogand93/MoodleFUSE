from tests import MoodleFuseAppTestCase
from tests.categories.data.categories_results import true_categories, false_categories
from fuse import FuseOSError

class CourseCategoriesTestCase(MoodleFuseAppTestCase):

    def list_course_categories_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse', None))

        assert self.utils.lists_are_equal(files, true_categories)

    def list_course_categories_invalid_categories_test(self):
        files = list(self.ops.readdir(
            self.filesystem_root + '/testcourse', None))

        assert self.utils.lists_are_not_equal(files, false_categories)

    def enter_course_category_invalid_course_category_test(self):
        self.assertRaises(FuseOSError, lambda:
                self.ops.access(
                    self.filesystem_root + '/testcourse/invalidcategory', None
                )
        )
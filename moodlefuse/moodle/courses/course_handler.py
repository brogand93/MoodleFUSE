#!/usr/bin/env python
# encoding: utf-8

import os

from moodlefuse.moodle.courses.course_errors import CourseErrors
from moodlefuse.moodle.moodle_handler import MoodleHandler
from moodlefuse.moodle.api import MoodleAPI


class CourseHandler(MoodleHandler):

    def __init__(self):
        MoodleHandler.__init__(self)

    def update(self):
        self.sync_courses()

    def sync_courses(self):
        get_courses_action = self.moodle_api.get_courses
        get_courses_error = CourseErrors.unable_to_sync_courses

        courses = \
            MoodleHandler.handle_moodle_action(MoodleHandler, get_courses_action, get_courses_error)

        for course in courses:
            course_folder_path = os.path.join(self._FS_ROOT, course)
            if not os.path.exists(course_folder_path):
                os.makedirs(course_folder_path)

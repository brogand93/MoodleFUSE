#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.errors import MoodleFuseError


class CourseErrors(object):

    @staticmethod
    @MoodleFuseError
    def unable_to_sync_courses():
        return "Unable to sync courses"

    @staticmethod
    @MoodleFuseError
    def unable_to_create_course():
        return "Unable to create course"

    @staticmethod
    @MoodleFuseError
    def unable_to_add_course_section():
        return "Unable to add course section"

    @staticmethod
    @MoodleFuseError
    def unable_to_remove_course():
        return "Unable to remove course"

    @staticmethod
    @MoodleFuseError
    def unable_to_remove_course_section():
        return "Unable to remove course section"

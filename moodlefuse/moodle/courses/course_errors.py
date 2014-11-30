#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.errors import MoodleFuseError


class CourseErrors(MoodleFuseError):

    @MoodleFuseError
    def unable_to_sync_courses(self):
        return "Unable to sync courses"

    @MoodleFuseError
    def unable_to_create_course(self):
        return "Unable to create course"

    @MoodleFuseError
    def unable_to_add_course_section(self):
        return "Unable to add course section"

    @MoodleFuseError
    def unable_to_remove_course(self):
        return "Unable to remove course"

    @MoodleFuseError
    def unable_to_remove_course_section(self):
        return "Unable to remove course section"

#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.errors import MoodleFuseError

class CourseErrors():

    @MoodleFuseError.unable_to_upload
    def unable_to_upload_resource(self):
        pass

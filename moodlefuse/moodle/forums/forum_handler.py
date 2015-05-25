#!/usr/bin/env python
# encoding: utf-8

"""Class to handle assignment Moodle actions, it extends MoodleHandler
   and therefor is an observer of Moodle.
"""

from moodlefuse.moodle.forums.forum_parser import ForumParser
from moodlefuse.moodle.handler import MoodleHandler


class ForumHandler(MoodleHandler):

    def __init__(self, emulator, js_emulator):
        super(self.__class__, self).__init__(emulator, js_emulator)
        self.parser = ForumParser()

    def is_forum(self, course_content, location):
        return self.parser.forum_exists_on_moodle(
            course_content,
            location[-1]
        )

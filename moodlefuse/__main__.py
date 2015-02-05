#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.assignments.assignment_handler import AssignmentHandler
from moodlefuse.moodle.resources.resource_handler import ResourceHandler
from moodlefuse.moodle.courses.course_handler import CourseHandler
from moodlefuse.moodle.moodle_watcher import MoodleWatcher
from moodlefuse.moodle import Moodle


def main():
    moodle = Moodle()
    moodle.attach(AssignmentHandler())
    moodle.attach(ResourceHandler())
    moodle.attach(CourseHandler())
    watcher = MoodleWatcher(moodle)
    watcher.start()


if __name__ == "__main__":
    main()

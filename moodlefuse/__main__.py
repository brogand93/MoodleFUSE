#!/usr/bin/env python
# encoding: utf-8

from moodlefuse.moodle.moodle_watcher import MoodleWatcher
from moodlefuse import MoodleFuse


def main():
    MoodleFuse()
    watcher = MoodleWatcher()
    watcher.start()


if __name__ == "__main__":
    main()

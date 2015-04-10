#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase
from moodlefuse import MoodleFuse


class MoodleFuseTestCase(TestCase):
    pass

class MoodleFuseAppTestCase(MoodleFuseTestCase):

    def setUp(self):
        MoodleFuse()
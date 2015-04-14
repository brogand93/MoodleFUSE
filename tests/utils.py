#!/usr/bin/env python
# encoding: utf-8


class TestUtils(object):

    @staticmethod
    def lists_are_equal(list1, list2):
        return sorted(list1) == sorted(list2)

    @staticmethod
    def lists_are_not_equal(list1, list2):
        return sorted(list1) != sorted(list2)
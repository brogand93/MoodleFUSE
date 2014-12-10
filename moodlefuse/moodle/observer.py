#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod


class Observer(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

#!/usr/bin/env python
# encoding: utf-8


class Moodle(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class MoodleException(BaseException):

    def __init__(self):
        self.message = "Unable to complete Moodle action"

    def __str__(self):
        return self.message

#!/usr/bin/env python
# encoding: utf-8

import os

from setuptools import setup


def read_file(name):
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        name
    )
    data = open(filepath)
    try:
        return data.read()
    except IOError:
        print "could not read %r" % name
        data.close()


PROJECT = 'moodlefuse'
VERSION = '0.0.1'
URL = 'http://github.com/brogand1993/MoodleFUSE'
AUTHOR = 'Darren Brogan'
AUTHOR_EMAIL = 'brogand2@mail.dcu.ie'
DESC = "FUSE filesystem based on moodle implementation"
LONG_DESC = read_file('README.rst')
REQUIRES = [
    'SQLAlchemy',
    'requests',
    'alembic',
    'fusepy'
]

setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=LONG_DESC,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='Apache License (2.0)',
    package_data={},
    packages=[
        'moodlefuse',
        'moodlefuse.moodle',
        'moodlefuse.moodle.courses',
        'moodlefuse.moodle.resources',
        'moodlefuse.moodle.assignments'
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points="""
        [console_scripts]
        moodlefuse = moodlefuse.__main__:main
        moodlefuse-configure = moodlefuse.configure:main
    """
)

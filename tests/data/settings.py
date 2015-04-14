import os

DEBUG = False
MOODLE_WEB_ADDRESS = 'file://' + os.path.dirname(os.path.realpath(__file__)) + '/login/index.html'
MOODLE_INDEX_ADDRESS = 'file://' + os.path.dirname(os.path.realpath(__file__)) + '/homepage.html'
LOCAL_MOODLE_FOLDER = os.path.join(os.path.expanduser('~'), 'tmp')
USERNAME = 'testuser'
PASSWORD = 'testpassword'
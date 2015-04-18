import os

DEBUG = False
MOODLE_WEB_ADDRESS = 'file://' + \
                     os.path.join(
                         os.path.dirname(os.path.realpath(__file__)),
                         '../moodle_implementation'
                     ) + '/login/index.html'
MOODLE_INDEX_ADDRESS = 'file://' + \
                     os.path.join(
                         os.path.dirname(os.path.realpath(__file__)),
                         '../moodle_implementation'
                     ) + '/homepage.html'
LOCAL_MOODLE_FOLDER = os.path.join(os.path.expanduser('~'), 'tmp')
USERNAME = 'testuser'
PASSWORD = 'testpassword'
TEST_DATA = 'file://' + os.path.join(
                 os.path.dirname(os.path.realpath(__file__)),
                 '../moodle_implementation'
             )
DOWNLOADS = os.path.join(
                 os.path.dirname(os.path.realpath(__file__)),
                 '../moodle_implementation'
             ) + '/downloads'
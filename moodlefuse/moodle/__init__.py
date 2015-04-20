#!/usr/bin/env python
# encoding: utf-8

from functools import wraps


LOGIN_LOCATION = '/login/index.php'
EDIT_ON_MOODLE_BUTTON_TEXT = 'Turn editing on'
EDIT_OFF_MOODLE_BUTTON_TEXT = 'Turn editing off'
USER_AGENT = [
    ('User-Agent',
     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
     (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36'),
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
    ('Cache-Control', 'max-age=0'),
    ('Accept-Language', 'en-GB,en-US;q=0.8,en;q=0.6'),
    ('Connection', 'keep-alive')
]


def requires_editing_moodle_js():
    def inner(f):
        def wrapped(*args):
            args[0].js_emulator.turn_course_editing_on()
            result = f(*args)
            args[0].js_emulator.turn_course_editing_off()
            return result
        return wraps(f)(wrapped)
    return inner

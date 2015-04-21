#!/usr/bin/env python
# encoding: utf-8

PARENT = '..'
THIRD_PARENT = '../../..'
CATEGORY = '//li[@aria-label="{0}"]'
GRADE_BOX = './/input[@class="quickgrade"]'
UPLOAD = '//div[@class="fp-btn-add"]'
DELETE = './/span[contains(text(), "Delete")]'
EDIT_BUTTON = './/a[contains(text(), "Edit")]'
CONTINUE = '//input[@type="submit"][@value="Continue"]'
SETTINGS = './/span[contains(text(), "Edit settings")]'
EDIT_ON = '//* [@type="submit"][@value="Turn editing on"]'
EDIT_OFF = '//* [@type="submit"][@value="Turn editing off"]'
FILE = '//span[contains(text(), "File") and @class="typename"]'
RESOURCE = '//li[@aria-label="{0}"]//span[contains(text(), "{1}")]'
USER_ROW = '//td[@class="cell c3 email" and contains(text(), "{0}")]'
QUICK_GRADING_OPTION = '//input[@name="quickgrading" and @class="ignoredirty"]'

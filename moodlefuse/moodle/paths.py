#!/usr/bin/env python
# encoding: utf-8

THIRD_PARENT = '../../..'
CATEGORY = '//li[@aria-label="{0}"]'
UPLOAD = '//div[@class="fp-btn-add"]'
DELETE = './/span[contains(text(), "Delete")]'
EDIT_BUTTON = './/a[contains(text(), "Edit")]'
SETTINGS = './/span[contains(text(), "Edit settings")]'
EDIT_ON = '//* [@type="submit"][@value="Turn editing on"]'
EDIT_OFF = '//* [@type="submit"][@value="Turn editing off"]'
FILE = '//span[contains(text(), "File") and @class="typename"]'
RESOURCE = '//li[@aria-label="{0}"]//span[contains(text(), "{1}")]'

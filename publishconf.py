#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://weilet.me"
FEED_DOMAIN = SITEURL

RELATIVE_URLS = False

# filetime_from_git is very slow. Use it in production only
# to avoid slow build times during development


DELETE_OUTPUT_DIRECTORY = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Weilet'
SITENAME = "Weilet's Workshop"
STATIC_PATHS = ['images', 'extra']
SITELOGO = '/images/rick.png'
SITESUBTITLE = 'Don\'t be evil'
FAVICON = '/images/favicon.ico'
SITEURL = 'https://weilet.github.io'


PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'Flex'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

SOCIAL = (
    ('github', 'https://weilet.github.io'),
    ('rss', 'https://weilet.github.io/feeds/all.rss.xml'),
)

SUMMARY_MAX_LENGTH = 10
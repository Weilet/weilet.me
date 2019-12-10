#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = "Weilet"
SITENAME = "Weilet's Workshop"
SITESUBTITLE = "Don't be evil"
SITEURL = "https://weilet.github.io"

PATH = "content"

# Regional Settings
TIMEZONE = "Asia/Shanghai"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}


PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "extract_toc",
    "liquid_tags.img",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
THEME = "elegant"
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("Github", "https://github.com/Pelican-Elegant/", "Elegant Github Repository"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
)

# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra/_redirects"]
EXTRA_PATH_METADATA = {"extra/_redirects": {"path": "_redirects"}}

if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

FREELISTS_NAME = "oracle-l"
FREELISTS_FILTER = True

# Legal
SITE_LICENSE = """
    Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>.
    """
HOSTED_ON = {"name": "Github Pages", "url": "https://pages.github.com/"}


# Landing Page
PROJECTS_TITLE = "Recent Repositories"
PROJECTS = [
      {
        "name": "wox_ext",
        "url": "https://github.com/Weilet/wox_ext",
        "description": "self-made wox extension",
    },
    {
        "name": "LBlog",
        "url": "https://github.com/Weilet/LBlog",
        "description": "a light blog powered by flask",
    },
]

LANDING_PAGE_TITLE = "Recent Activities"

DISQUS_FILTER = True
UTTERANCES_FILTER = True

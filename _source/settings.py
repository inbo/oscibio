#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = "LifeWatch INBO blog"
SITEURL = ""  # Set
AUTHOR = "LifeWatch INBO team"

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
MARKUP = "md"

# Reading settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = None
DEFAULT_DATE_FORMAT  = "%B %d, %Y"
SUMMARY_MAX_LENGTH = -1

# Directory settings
DELETE_OUTPUT_DIRECTORY = False # Change
PATH = ""
ARTICLE_DIR = "posts"
PAGE_DIR = "pages"
STATIC_PATHS = (
    ("images"),
    ("files"),
)
OUTPUT_PATH = "../" # One level above the _source folder

# URLs
ARTICLE_URL = "posts/{slug}.html" # Both slug and slug.html will work
ARTICLE_SAVE_AS = "posts/{slug}.html"

# Feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Theme
THEME = "../../spoonbill-lifewatch" # Relative link to theme repository

# External services
DISQUS_SITENAME = "" # Set
GOOGLE_ANALYTICS = "" # Set
GOOGLE_WEBMASTER = "" # Set
GITHUB_URL = "https://github.com/organizations/LifeWatchINBO"
TWITTER_URL = "https://twitter.com/LifeWatchINBO"

# Blogroll
LINKS = (
    ("Research Institute for Nature and Forest (INBO)", "http://www.inbo.be"),
    ("Belgian LifeWatch portal", "http://www.lifewatch.be"),
    ("European LifeWatch portal", "http://www.lifewatch.eu"),
)

# Social widget
SOCIAL = (
    ("Follow us on Twitter", "https://twitter.com/LifeWatchINBO"),
    ("Our GitHub repositories", "https://github.com/organizations/LifeWatchINBO"),
    ("Subscribe to updates", SITEURL + "/" + FEED_ALL_RSS),
)

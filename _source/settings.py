#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = "LifeWatch INBO"
SITEURL = "https://lifewatch.inbo.be/blog"
TITLE = "Towards more efficient biodiversity monitoring"
SUBTITLE = "We blog about ideas, challenges and technologies related to building "\
           "an open terrestrial and freshwater observatory in Flanders for the "\
           "LifeWatch research infrastructure."
AUTHOR = "LifeWatch INBO team"
DISCLAIMER = "The views expressed on this blog represent the ideas of the author(s) and are not to be considered an INBO or institutional policy. Unless stated otherwise, all content on this <a xmlns:dct=\"http://purl.org/dc/terms/\" property=\"dct:title\" href=\"https://lifewatch.inbo.be/blog\">LifeWatch INBO blog</a> is licensed under a <a rel =\"license\" href=\"http://creativecommons.org/licenses/by/4.0/\"> Creative Commons Attribution 4.0 International License</a>."

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
MARKUP = (("md"),)

# Reading settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = None
DEFAULT_DATE_FORMAT  = "%B %d, %Y"
SUMMARY_MAX_LENGTH = 0

# Directory settings
PATH = ""
ARTICLE_PATHS = ["posts"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = [
    "images",
    "files"
]
OUTPUT_PATH = "../" # root
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = (
    (".git"),
    (".gitignore"),
    ("humans.txt"),
    ("robots.txt"),
)
CACHE_CONTENT = False

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
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Theme
THEME = "../../eurasian-spoonbill" # Relative link to theme repository

# External services
DISQUS_SITENAME = "lifewatchinbo"
GOOGLE_ANALYTICS = "UA-42312007-1"
GOOGLE_WEBMASTER = "bHOQjaP_2zAxd-nxU1TDYpBAasDIAgtgbSKcckig3iQ"
GITHUB_URL = "https://github.com/inbo"
TWITTER_NAME = "LifeWatchINBO"
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
    ("Our GitHub repositories", "https://github.com/inbo"),
    ("Subscribe to updates", SITEURL + "/" + FEED_ALL_RSS),
)

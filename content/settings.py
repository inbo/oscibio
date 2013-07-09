#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = "LifeWatch INBO"
SITEURL = "http://lifewatch.inbo.be/blog"
TITLE = "Towards more efficient biodiversity monitoring"
SUBTITLE = "We blog about ideas, challenges and technologies related to building "\
           "an open terrestrial and freshwater observatory in Flanders for the "\
           "LifeWatch research infrastructure."
AUTHOR = "LifeWatch INBO team"
DISCLAIMER = "The views expressed on this blog represent the ideas of the author(s) "\
             "and are not to be considered an INBO or institutional policy. "\
             "Unless stated otherwise, <a xmlns:cc=\"http://creativecommons.org/ns#\" "\
             "href=\"http://lifewatch.inbo.be/blog\" property=\"cc:attributionName\" "\
             "rel=\"cc:attributionURL\">all content</a> is licensed under a "\
             "<a rel =\"license\" href=\"http://creativecommons.org/licenses/by/3.0/\">"\
             "Creative Commons Attribution 3.0 Unported License</a>."

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
MARKUP = (("md"),)

# Reading settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = None
DEFAULT_DATE_FORMAT  = "%B %d, %Y"
SUMMARY_MAX_LENGTH = 0

# Directory settings
DELETE_OUTPUT_DIRECTORY = False # Change
PATH = ""
ARTICLE_DIR = "posts"
PAGE_DIR = "pages"
STATIC_PATHS = (
    ("images"),
    ("files"),
)
OUTPUT_PATH = "../output" # Sibling directory of `content`

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
THEME = "../../eurasian-spoonbill" # Relative link to theme repository

# External services
DISQUS_SITENAME = "lifewatchinbo"
GOOGLE_ANALYTICS = "UA-42312007-1"
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

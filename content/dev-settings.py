#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from settings import *

SITEURL = "http://localhost:8080"

# Directory settings
OUTPUT_PATH = "../test-output"

# Reading settings
DEFAULT_PAGINATION = None # To test pagination

# External services
GOOGLE_ANALYTICS = "UA-XXXXX-X" # Don't track while coding
DISQUS_SITENAME = "" # Don't link to existing Disqus forum while coding
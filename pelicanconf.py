#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'maggick'
SITENAME = 'Recettes d\'arrière grand-mère'
SITEURL = 'https://maggick.fr/receipts'
SITETITLE = SITENAME

PATH = 'content'
RELATIVE_ULRS = True
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extra/.nojekyll']
EXTRA_PATH_METADATA = {'extra/.nojekyll':{'path':'.nojekyll'},}

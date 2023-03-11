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

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extra/.nojekyll']
EXTRA_PATH_METADATA = {'extra/.nojekyll':{'path':'.nojekyll'},}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

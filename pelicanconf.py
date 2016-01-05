#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoxMaSk'
SITENAME = 'Trigger Happy'
SITESUBTITLE = 'a bridge between your internet services'

SITEURL = 'http://blog.trigger-happy.eu'
TIMEZONE = 'Europe/Paris'

PATH = 'content'


DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
# Blogroll
LINKS = (('Trigger Happy Website', 'http://trigger-happy.eu'),
         ('Documentation', 'http://trigger-happy.readthedocs.org/'),
         ('Source Code', 'https://github.com/foxmask/django-th'),
         ('Trello board', 'https://trello.com/b/Jf0eTBQR/trigger-happy'),
         ('Compare Trigger Happy', 'https://alternativeto.net/software/trigger-happy/'),
         ("Author's Blog Posts", 'http://foxmask.trigger-happy.eu'),)

# Social widget
SOCIAL = (('@triggerhappyeu', 'https://twitter.com/triggerhappyeu'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'github_activity']

# for the plugin sitemap
SITEMAP = {'format': 'xml'}

DISQUS_SITENAME = "blogtriggerhappyeu"
FEED_DOMAIN = 'http://blog.trigger-happy.eu'
FEED_ATOM = 'main.atom.xml'
FEED_RSS = 'main.rss.xml'
# https://github.com/getpelican/pelican-plugins/tree/master/github_activity
GITHUB_ACTIVITY_FEED = 'https://github.com/foxmask.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 10

TWITTER_USERNAME = 'triggerhappyeu'
GITHUB_URL = 'https://github.com/foxmask/django-th'

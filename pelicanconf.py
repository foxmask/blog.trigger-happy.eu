#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoxMaSk'
SITENAME = 'Trigger Happy'
SITESUBTITLE = 'a bridge between your internet services'

SITEURL = 'https://blog.trigger-happy.eu'
TIMEZONE = 'Europe/Paris'

THEME = '../pelican-themes/pelican-bootstrap3/'


PATH = 'content'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
#TAG_FEED_RSS = 'feeds/%s.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10

# theme bootstrap https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
BANNER_SUBTITLE = 'a bridge between your internet services'
BANNER = '/static/banner.png'
DISPLAY_TAGS_ON_SIDEBAR = False
BOOTSTRAP_NAVBAR_INVERSE = True

#GITHUB_USER = "foxmask"
#GITHUB_REPO_COUNT = 5
#GITHUB_SKIP_FORK = False
#GITHUB_SHOW_USER_LINK = False

DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 20
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_FEEDS_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
RECENT_POST_COUNT = 5

TWITTER_CARDS = True
TWITTER_USERNAME = 'triggerhappyeu'
TWITTER_WIDGET_ID = 669143142793412608

CUSTOM_LICENSE='Unless otherwise stated, all articles are published under the <a href="http://www.wtfpl.net/about/">WTFPL</a> license.'

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')
TIPUE_SEARCH = True
SEARCH_URL = 'search.html'

# AVATAR = '/static/cactus.png'

# ABOUT_ME = '<a href="/pages/a-propos">Passionné par les Logiciels Libres</a>'

# Standard
DEFAULT_CATEGORY = 'General'

#ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
#ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Blogroll
LINKS = (('Trigger Happy Website', 'https://trigger-happy.eu'),
         ('Say thanks', 'https://saythanks.io/to/foxmask'),
         ('Documentation', 'http://trigger-happy.readthedocs.org/'),
         ('RSS', 'https://blog.trigger-happy.eu/feeds/all.rss.xml'),
         ('Atom', 'https://blog.trigger-happy.eu/feeds/all.atom.xml'),
         ('Source Code', 'https://github.com/foxmask/django-th'),
         ('Trello board', 'https://trello.com/b/Jf0eTBQR/trigger-happy'),
         ('Compare Trigger Happy', 'https://alternativeto.net/software/trigger-happy/'),
         ("Author's Blog Posts", 'https://foxmask.trigger-happy.eu'),
         ("Stats", 'https://blog.trigger-happy.eu/stats.html'),
)

FREE_PROJECT = True
# Social widget
# SOCIAL = (('@triggerhappyeu', 'https://twitter.com/triggerhappyeu'),)


DEFAULT_PAGINATION = 10

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'pelican-page-order', 'tag_cloud', 'github_activity', 'related_posts', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code',
           'neighbors', 'github_activity', 'tipue_search']

# related_posts plugin - https://github.com/getpelican/pelican-plugins/tree/master/related_posts
RELATED_POSTS_MAX = 5

# Following items are often useful when publishing

# for the plugin sitemap
SITEMAP = {'format': 'xml'}

DISQUS_SITENAME = "blogtriggerhappyeu"

# pour le theme octopress
#SIDEBAR_IMAGE = '/static/cactus.png'
#SEARCH_BOX = True
#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_CATEGORIES_ON_MENU = True
#DISPLAY_FEEDS_ON_MENU = True

CATEGORY_IN_SIDEBAR = False


FEED_DOMAIN = 'https://blog.trigger-happy.eu'
FEED_ATOM = 'main.atom.xml'
FEED_RSS = 'main.rss.xml'

# https://github.com/getpelican/pelican-plugins/tree/master/github_activity
GITHUB_ACTIVITY_FEED = ''
GITHUB_ACTIVITY_MAX_ENTRIES = 10

TWITTER_USERNAME = 'triggerhappyeu'
GITHUB_URL = 'https://github.com/foxmask/django-th'

ARTICLE_PATHS = ['news', 'tuto']

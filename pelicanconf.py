#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'WANG Aiyong'
SITENAME = u'WANG Aiyong blog'
SITEURL = 'http://gepcel.github.io'

MARKUP = ('md', 'ipynb')

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/gepcel'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme using
THEME = "pelican-themes/yihui"



DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'cn': '%Y-%m-%d',
}

ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
#STATIC_PATHS = 'sources'
#OUTPUT_SOURCES = True


#---------config or pelican-plugins--------
PLUGIN_PATHS=["pelican-plugins"]
PLUGINS=['interlinks','render_math', 'liquid_tags.img', 'liquid_tags.video', 
'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code', 'liquid_tags.literal', 'ipynb.markup']

#-------config of plugin: interlinks-------
#interlinks used
INTERLINKS = {
    'python': 'http://python.org',
	'pelican': 'http://docs.getpelican.com',
	'mpl': 'http://matplotlib.org/',
	'matplotlib': 'http://matplotlib.org/',
	'ipython': 'http://ipython.org',
	'yihui': 'http://yihui.name',
	'pygments': 'http://pygments.org',
	'jinja2': 'http://jinja.pocoo.org',
	'markdown': 'http://daringfireball.net/projects/markdown',
	'chunjuan': 'http://blog.pchome.net/1269/',
	'pandas': 'http://pandas.pydata.org/',
	'cartopy': 'http://scitools.org.uk/cartopy/index.html',
}

#-------config of plugin: latex
#bying setting LATEX='artical', make the latex(most mathjax) to render
#in some specific article with a "Latex:" metadata without anyvalue
LATEX = 'article'

# EXTRA_HEADER = open('_nb_header.html').read() #.decode('utf-8')
NOTEBOOK_DIR = 'notebooks'
STATIC_PATHS = ['images', 'code', 'notebooks']

IGNORE_FILES = ['.ipynb_checkpoints', '*.tmp']

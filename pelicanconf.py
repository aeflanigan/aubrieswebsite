from pathlib import Path

AUTHOR = 'Aubrie Flanigan'
SITENAME = "Aubrie's Site"
SITEURL = ''
SITESUBTITLE = "Welcome to my awesome website!"

PATH = 'content'
ARTICLE_PATHS = [p.absolute() for p in Path(PATH).glob('**/articles/*.md')]
PAGE_PATHS = [p.absolute() for p in Path(PATH).glob('**/pages/*.md')]

# Settings for html5up-massively theme
# For featured article to always be the latest article, set value to -1
FEATURED_ARTICLE = 'article-one'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = './themes/html5up-massively'
THEME_STATIC_DIR = '.'
THEME_STATIC_PATHS = ['static']

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# TODO: Aubrie, fill this out with your social media links
SOCIAL = (('twitter', 'https://www.linkedin.com/'),
          ('facebook', 'https://www.facebook.com/'),
          ('instagram', 'https://www.instagram.com/'),
          ('github', 'https://github.com/aeflanigan/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

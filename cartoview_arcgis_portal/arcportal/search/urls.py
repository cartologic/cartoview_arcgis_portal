__author__ = 'Ahmed Nour Eldeen'

from django.conf.urls import patterns, url
import views
from .. import *

url_patterns = patterns('',
    url(r'^$', views.search, name=SEARCH_URL_NAME)
)
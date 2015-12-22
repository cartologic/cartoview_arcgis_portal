__author__ = 'Ahmed Nour Eldeen'

from django.conf.urls import patterns, url
import views

url_patterns = patterns('',
    url(r'^$', views.search, name="search")
)
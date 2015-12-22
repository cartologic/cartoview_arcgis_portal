__author__ = 'Ahmed Nour Eldeen'

from django.conf.urls import patterns, url
import rest_views

rest_url_patterns = patterns('',
     url(r'^self$', rest_views.community, name="community"),
     url(r'^groups$', rest_views.groups, name="community_groups"),
     url(r'^users/(?P<username>[^/]+)$', rest_views.community_users, name="community_users"),
 )
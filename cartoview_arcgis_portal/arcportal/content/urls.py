__author__ = 'Ahmed Nour Eldeen'

import os

from django.conf.urls import patterns, url, static

import views
import rest_views


url_patterns = patterns('',
    url(r'^newItem/$', views.new_item, name="content.new_item"),
    url(r'^editItem/(?P<item_id>[^/]+)/$', views.edit_item, name="content.edit_item")
)


current_folder, filename = os.path.split(os.path.abspath(__file__))
rest_url_patterns = patterns('',
    url(r'^users/(?P<username>[^/]+)$', rest_views.user_items, name="arcportal_user_items"),
    url(r'^items/(?P<item_id>[^/]+)$', rest_views.items, name="items"),
    url(r'^items/(?P<item_id>[^/]+)/data$', rest_views.item_data, name="item_data"),
    url(r'^items/(?P<item_id>[^/]+)/info/thumbnail/(?P<file_name>[^/]+)$', rest_views.item_thumbnail, name="item_data"),
)



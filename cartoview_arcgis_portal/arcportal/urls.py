__author__ = 'AhmedNourEldeen'

from django.conf.urls import patterns, include, url
import views
import token_manager.urls as token_urls
import content.urls as content_urls
import search.urls as search_urls
import community.urls as community_urls


url_sub_patterns = patterns('',
                            url(r'^$', views.sharing_home, name="arcportal_sharing_home"),
                            url(r'^rest$', views.sharing_home, name="arcportal_rest_home"),
                            url(r'^rest/info$', views.info, name="arcportal_rest_info"),

                            url(r'^rest/', include(token_urls.url_patterns)),
                            url(r'^portals/$', views.portal, name="arcportal_portals"),
                            url(r'^portals/self$', views.portal, name="arcportal_portals_self"),
                            url(r'^rest/portals/self$', views.portal, name="arcportal_rest_portals_self"),

                            url(r'', include(token_urls.url_patterns)),

                            url(r'^content/', include(content_urls.url_patterns)),
                            url(r'^rest/content/', include(content_urls.rest_url_patterns)),
                            url(r'^rest/search', include(search_urls.url_patterns)),
                            url(r'^rest/community/', include(community_urls.rest_url_patterns)),

                            )

urlpatterns = patterns('',
                       url(r'^$', views.portal, name="arcportal_home"),
                       url(r'^sharing/', include(url_sub_patterns)),
                       )



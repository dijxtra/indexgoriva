from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('apps.pregledindexa.views',
    url(r'^$', 'index', name='home_view'),
    url(r'^gorivo/$', 'index'),
    url(r'^indeksi/$', 'index'),
    url(r'^impressum/$', 'impressum', name='impressum_view'),
    url(r'^gorivo/(?P<gorivo_id>\d+)$', 'gorivo', name='gorivo_view'),
    url(r'^indeksi/(?P<gorivo_id>\d+)$', 'indeksi', name='indeksi_view'),
    url(r'^set_limit/(?P<view_name>\w+)/(?P<gorivo_id>\d+)$', 'set_limit', name='set_limit_view'),
)

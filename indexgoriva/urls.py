from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.pregledindexa.views.index', name='home_view'),
    url(r'^gorivo/(?P<gorivo_id>\d+)$', 'apps.pregledindexa.views.gorivo', name='gorivo_view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

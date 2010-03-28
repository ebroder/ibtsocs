import os

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from ibtsocs.root.feeds import PostFeed

feeds = {
    'posts': PostFeed,
}

static = {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__), 'root', 'static'))}

urlpatterns = patterns(
    '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^posts/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    (r'^feeds?/$', 'django.views.generic.simple.redirect_to', {'url': '/feeds/posts'}),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', static),
    (r'^(?P<path>robots.txt)$', 'django.views.static.serve', static),
)

urlpatterns += patterns(
    'ibtsocs.root.views',
    (r'^$', 'index'),
    (r'^posts/new/$', 'create'),
    (r'^posts/(\d+)/$', 'display'),
    (r'^vote/(\d+)/(up|down)$', 'vote'),
)

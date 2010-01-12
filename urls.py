from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from ibtsocs.root.feeds import PostFeed

feeds = {
    'posts': PostFeed,
}

urlpatterns = patterns(
    '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^posts/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

urlpatterns += patterns(
    'ibtsocs.root.views',
    (r'^$', 'index'),
    (r'^posts/new/$', 'create'),
    (r'^posts/(\d+)/$', 'display'),
    (r'^posts/(\d+)/(up|down)vote/$', 'vote'),
)

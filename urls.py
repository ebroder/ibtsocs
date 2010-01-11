from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^posts/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
)

urlpatterns += patterns(
    'ibtsocs.root.views',
    (r'^$', 'index'),
    (r'^posts/(\d+)/$', 'display'),
    (r'^posts/(\d+)/(up|down)vote/$', 'vote'),
)

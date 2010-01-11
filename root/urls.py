from django.conf.urls.defaults import *

urlpatterns = patterns(
    'ibtsocs.root.views',
    (r'^$', 'index'),
    (r'^posts/(\d+)/$', 'display'),
)

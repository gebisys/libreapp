from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.conf import settings
from  news.feeds import ArchiveFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.index_view'),
	url(r"^post/(?P<year>\d{4})/(?P<mounth>\d{1,2})/(?P<day>\d{2})/(?P<slug>[\w-]+)$", 'news.views.post'),
    url(r'^feed/$', ArchiveFeed()),
    
    # archivos estaticos
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),

    url(r'^user/$', 'news.views.createuser'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

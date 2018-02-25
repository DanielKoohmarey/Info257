from django.conf.urls import patterns, include, url
from info257.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compsci.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', home),
    url(r'^$', home),
    url(r'^courses/', courses),
    url(r'^professors/', professors),
    url(r'^assistants/', assistants),
    url(r'^buildings/', buildings),
    url(r'^tutors/', tutors),
)

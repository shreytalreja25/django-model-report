# -*- coding: utf-8 -*-
try:
    from django.urls import re_path,include
except ImportError:
    from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

from model_report import report
report.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('model_report.urls')),
)

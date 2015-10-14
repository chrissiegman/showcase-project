from django.conf.urls import patterns, url
import biebfeed.views

urlpatterns = patterns('',
                       url(r'^$', biebfeed.views.index),
                       )
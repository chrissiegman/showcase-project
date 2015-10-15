from django.conf.urls import patterns, url
import biebfeed.views

urlpatterns = patterns('biebfeed.views',
                       url(r'^$', biebfeed.views.index, name="index"),
                       )
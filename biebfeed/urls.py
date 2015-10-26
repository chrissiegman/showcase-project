from django.conf.urls import patterns, url
import biebfeed.views

urlpatterns = patterns('biebfeed.views',
                       url(r'^$', biebfeed.views.index, name="index"),
                       url(r'^friends/$', biebfeed.views.friends, name="friends"),
                       url(r'^delete_friend/', biebfeed.views.delete_friend, name="delete_friend"),
                       url(r'^add_friend/', biebfeed.views.add_friend, name="add_friend")
                       )
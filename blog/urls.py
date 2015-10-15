from django.conf.urls import patterns, url
import blog.views

urlpatterns = patterns('blog.views',
                       url(r'^$', blog.views.index, name='index'),
                       )

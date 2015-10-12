from django.conf.urls import patterns, url
from showcase_app import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/', views.about, name='about'),
                       url(r'^contact/', views.contact, name='contact'),
                       url(r'^projects/', views.projects, name='projects'),
                       url(r'^resumee/', views.resumee, name='resumee'),
                       )
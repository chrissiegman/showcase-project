from django.conf.urls import patterns, url
from showcase_app import views
from showcase_app.views import UserProfileDetailView, UserProfileEditView
from django.contrib.auth.decorators import login_required as auth


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^contact/', views.contact, name='contact'),
                       url(r'^projects/', views.projects, name='projects'),
                       url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(template_name="showcase_app/user_profile.html"), name="profile"),
                       url(r'^edit_profile/$', auth(UserProfileEditView.as_view(template_name="showcase_app/edit_profile.html")), name="edit_profile"),
                       )

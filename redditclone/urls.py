from django.conf.urls import url, patterns
from redditclone.views import LinkListView

urlpatterns = patterns('redditclone.views',
                       url(r'^$', LinkListView.as_view(template_name="redditclone/index.html"), name="index")
                       )

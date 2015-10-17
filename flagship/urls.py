from django.conf.urls import url, patterns
import flagship.views

urlpatterns = patterns('flagship.views',
                       url(r'^$', flagship.views.index, name="index")
                       )
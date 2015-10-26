from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(null=True)
    
    def __str__(self):
        return "%s's profile" % self.user

    def get_absolute_url(self):
        return reverse('showcase_app.views.profile', args=[str(self.pk)])
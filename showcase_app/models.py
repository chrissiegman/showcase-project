from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(null=True)
    
    def __str__(self):
        return "%s's profile" % self.user

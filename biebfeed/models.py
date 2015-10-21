from django.db import models
from showcase_app.models import UserProfile
# Create your models here.

class twitter_target(models.Model):
    user = models.ForeignKey(UserProfile)
    target_username = models.CharField(max_length=20)
    def __str__(self):
        return self.target_username
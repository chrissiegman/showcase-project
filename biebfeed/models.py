from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TwitterTarget(models.Model):
    user = models.ForeignKey(User)
    target_username = models.CharField(max_length=20)
    def __str__(self):
        return self.target_username